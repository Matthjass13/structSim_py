# Analyse de la lenteur des tests d'intégration

## Contexte

Les tests d'intégration (`tests/integrationTests/test_integration.py`) passent pour les 12 migrations,
mais trois d'entre elles sont systématiquement plus lentes (~10 s) que les autres (~2 s) sur Windows :

- `zeroShot/withContext`
- `oneShot/aSimulationSystemHandler`
- `chainOfThought/riskFirst/structuredsim`

Le mécanisme de vérification du test est un **polling** : après l'appel à `s.start_program(...)`,
le test scrute l'existence du fichier `SummaryFile.txt` toutes les 200 ms avec un timeout de 15 s
(cf. `test_integration.py`, lignes 133–152). La durée d'un test dépend donc directement du moment
où les threads de fond ont terminé d'écrire ce fichier.

---

## Cause principale : absence de `thread.join()` dans `start_program`

Dans les **migrations rapides** (ex. `zeroShot/onlyTask`), `start_program` attend explicitement la
fin des deux threads avant de rendre la main :

```python
# zeroShot/onlyTask/start_program.py, lignes 37-38
planning_thread.join()
simulation_thread.join()
```

Cela signifie que lorsque `s.start_program(...)` retourne, tout le travail est terminé et le fichier
`SummaryFile.txt` est déjà écrit. Le premier appel à `summary_file.exists()` dans la boucle de
polling réussit : le test se termine en ~0,2 s d'attente de polling.

Dans les **trois migrations lentes**, `start_program` lance les threads mais ne les attend pas :

```python
# zeroShot/withContext/interfaces/start_program.py, lignes 43-48
planning_thread.start()
# ...
simulation_thread.start()
# <-- retour immédiat, pas de join()
```

Identique pour `oneShot/aSimulationSystemHandler/interfaces/start_program.py` (lignes 41-48) et
`chainOfThought/riskFirst/structuredsim/interfaces/StartProgram.py` (lignes 44-51).

La méthode retourne donc **avant** que les threads aient terminé. Le test doit attendre plusieurs
cycles de 200 ms pendant que le travail s'effectue en arrière-plan, ce qui allonge directement
la durée mesurée.

---

## Cause secondaire : `result_thread` orphelin dans le thread simulateur

Dans les migrations rapides, après la boucle principale de simulation, le thread de résultats est
démarré **et attendu** :

```python
# zeroShot/onlyTask/experimenthandling/experiment_simulator_handler.py, lignes 55-56
result_thread.start()
result_thread.join()  # attend que les résultats soient écrits
```

Ainsi le thread simulateur ne se termine que lorsque les résultats sont écrits sur disque.
Comme `start_program` attend ce thread via `simulation_thread.join()`, la chaîne de synchronisation
est complète jusqu'à l'écriture du fichier final.

Dans `zeroShot/withContext` et `oneShot/aSimulationSystemHandler`, le `result_thread` est lancé
sans join :

```python
# zeroShot/withContext/experimenthandling/experiment_simulator_handler.py, ligne 63
result_thread.start()
# <-- pas de join(), le thread de résultats s'exécute en parallèle
```

Même si `start_program` avait des joins, ceux-ci ne garantiraient pas que les résultats sont
écrits, car le thread simulateur se termine avant le thread de résultats. Le fichier
`SummaryFile.txt` peut n'être écrit que plusieurs centaines de millisecondes après la fin de
`start_program`, forçant le polling à attendre plusieurs cycles supplémentaires.

---

## Cause tertiaire : `queue.get()` sans timeout dans le thread simulateur

Dans les migrations rapides, la file d'attente est consommée avec un timeout :

```python
# zeroShot/onlyTask/experimenthandling/experiment_simulator_handler.py, lignes 27-31
try:
    env = self.environment_queue.get(timeout=0.5)
except queue.Empty:
    if self.plan.is_finish:
        break
    continue
```

Dans `zeroShot/withContext` (ligne 29) et `oneShot/aSimulationSystemHandler` (ligne 37),
l'appel est bloquant sans timeout :

```python
env = self._environment_queue.get()       # zeroShot/withContext
env = self.environment_queue.get(block=True)  # oneShot/aSimulationSystemHandler
```

Sur Windows, le GIL et l'ordonnanceur de threads ont un comportement légèrement différent de Linux.
Un `get()` bloquant sans timeout peut induire une latence supplémentaire lors du dernier passage
dans la boucle : le thread simulateur attend indéfiniment le prochain élément, qui ne viendra
jamais, jusqu'à ce qu'un autre mécanisme (vérification de `is_finish` après traitement du dernier
élément) lui permette de sortir. Cette sortie ne peut se produire qu'**après** le traitement du
dernier élément ET la mise à jour de `plan.is_finish` par le thread planificateur, ce qui introduit
une fenêtre de course (*race condition*) susceptible d'ajouter quelques centaines de millisecondes
sur Windows où le quantum de scheduling est de ~15 ms (contre ~1 ms sur Linux).

---

## Cause spécifique à `chainOfThought/riskFirst/structuredsim` : `copy.deepcopy()`

Cette migration utilise `copy.deepcopy()` pour dupliquer les paramètres d'un `Environment` :

```python
# chainOfThought/riskFirst/structuredsim/experimenthandling/environment.py, ligne 26
self.set_of_parameters = _copy.deepcopy(copy_from.set_of_parameters)
```

Les autres migrations utilisent une copie manuelle champ par champ (ex. `zeroShot/onlyTask`) ou
une méthode `Parameter.copy()` dédiée, beaucoup plus rapides. `deepcopy` parcourt récursivement
le graphe d'objets via l'introspection Python, ce qui est significativement plus lent. Cette
opération est appelée à chaque création de branche dans l'arbre de planification, amplifiant la
latence proportionnellement au nombre de simulations.

Note : `chainOfThought/riskFirst/structuredsim` dispose d'un `result_thread.join()` dans son
`ExperimentSimulatorHandler` (ligne 62), ce qui est correct. L'absence de `join()` dans
`StartProgram` reste cependant la cause principale de sa lenteur lors des tests.

---

## Résumé comparatif

| Problème | `zeroShot/withContext` | `oneShot/aSimulationSystemHandler` | `riskFirst/structuredsim` | Migrations rapides |
|---|:---:|:---:|:---:|:---:|
| `start_program` sans `join()` | ✗ | ✗ | ✗ | ✓ |
| `result_thread` sans `join()` dans le simulateur | ✗ | ✗ | ✓ | ✓ |
| `queue.get()` sans timeout | ✗ | ✗ | ✓ | ✓ |
| `copy.deepcopy()` dans Environment | ✓ | ✓ | ✗ | ✓ |

✓ = implémentation correcte (ou problème absent) · ✗ = problème présent

---

## Conclusion

La lenteur observée sur Windows (~10 s vs ~2 s) est principalement due à l'**absence de
synchronisation entre le thread principal et les threads de fond** dans `start_program` des trois
migrations concernées. Sans `join()`, le test commence à scruter le système de fichiers avant que
les threads aient produit leurs résultats, ce qui force une attente active par polling (cycles de
200 ms). Sur Windows, le quantum de scheduling plus large (~15 ms vs ~1 ms sur Linux) amplifie
cette latence, car chaque commutation de contexte prend plus de temps à se produire. Les problèmes
secondaires (thread de résultats orphelin, `get()` bloquant sans timeout, `deepcopy`) aggravent
l'effet en retardant davantage l'écriture du fichier attendu par le test.
