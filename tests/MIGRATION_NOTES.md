# Notes de migration Java → Python

## Structure des fichiers

```
Java (original)                              Python (migré)
─────────────────────────────────────────    ──────────────────────────────────────────────────
unitTests/environment/
  EnvironmentTests.java                  →   unit_tests/environment/test_environment.py

unitTests/fileManagement/
  FileManagementTests.java  (base)       →   unit_tests/file_management/conftest.py  (fixture)
  FileManagementContentTests.java        →   unit_tests/file_management/test_file_management_content.py
  FileManagementExportFilesTests.java    →   unit_tests/file_management/test_file_management_export_files.py
  FileManagementFileOperationsTests.java →   unit_tests/file_management/test_file_management_file_operations.py
  FileManagementPropertiesTests.java     →   unit_tests/file_management/test_file_management_properties.py
  FileManagementSimulationTests.java     →   unit_tests/file_management/test_file_management_simulation.py

unitTests/gluecode/
  ConcreteModifierTests.java             →   unit_tests/gluecode/test_concrete_modifier.py
  SimpleSimulationHandlerTests.java      →   unit_tests/gluecode/test_simple_simulation_handler.py

integrationTests/
  IntegrationTests.java                  →   integration_tests/test_integration.py
```

---

## Correspondances JUnit → pytest

| Java (JUnit 4 / JUnit 5)                     | Python (pytest)                                     | Notes                                  |
|----------------------------------------------|-----------------------------------------------------|----------------------------------------|
| `extends TestCase`                           | —                                                   | Aucun héritage requis en pytest        |
| `@Test`                                      | `def test_*(self):`                                 |                                        |
| `@BeforeEach void setUp()`                   | `@pytest.fixture(autouse=True) def setup(self, …):` |                                        |
| `@TempDir Path tempDir` (champ de classe)    | `tmp_path` injecté dans le setup autouse            |                                        |
| `@TempDir Path tempDir` (paramètre méthode)  | `tmp_path` injecté directement dans la méthode      | Ex : `FileManagementExportFilesTests`  |
| `@ParameterizedTest` + `@CsvSource`          | `@pytest.mark.parametrize`                          |                                        |

---

## Correspondances d'assertions

| Java                                       | Python                                         | Notes                                     |
|--------------------------------------------|------------------------------------------------|-------------------------------------------|
| `assertEquals(double, double, delta)`      | `assert a == pytest.approx(b, abs=DELTA)`      | Flottants uniquement                      |
| `assertEquals(int, int)`                   | `assert a == b`                                | Exact, pas d'approx                       |
| `assertEquals(String, String)`             | `assert a == b`                                |                                           |
| `assertTrue(x)`                            | `assert x`                                     |                                           |
| `assertFalse(x)`                           | `assert not x`                                 |                                           |
| `assertNull(x)`                            | `assert x is None`                             | Ne pas utiliser `assert not x` (faux pos) |
| `assertNotNull(x)`                         | `assert x is not None`                         |                                           |
| `assertDoesNotThrow(() -> method())`       | `method()` (appel direct)                      | Toute exception fait échouer pytest       |
| `assertTrue(msg, cond)` (JUnit 4)          | `assert cond, msg`                             | ⚠️  Ordre inversé en Java JUnit 4 !       |

---

## Correspondances de types

| Java                     | Python           | Notes                                        |
|--------------------------|------------------|----------------------------------------------|
| `Vector<T>`              | `list`           | `.get(i)` → `[i]`                            |
| `ArrayList<T>`           | `list`           |                                              |
| `LinkedHashMap<K, V>`    | `dict`           | Ordonné par insertion depuis Python 3.7      |
| `InputStream`            | `io.BytesIO`     |                                              |
| `Calendar`               | `datetime`       | Voir section dédiée ci-dessous               |
| `Properties`             | `_load_properties()` (helper custom)  | `configparser` avec section `[DEFAULT]` |
| `Path` (java.nio)        | `pathlib.Path`   |                                              |
| `char`                   | `str` (1 car.)   |                                              |

---

## Mockito → unittest.mock

| Java (Mockito)                                         | Python (unittest.mock)                                 |
|--------------------------------------------------------|--------------------------------------------------------|
| `mock(X.class)`                                        | `MagicMock(spec=X)`                                    |
| `verify(mock, times(1)).method(arg)`                   | `mock.method.assert_called_once_with(arg)`             |
| `anyString()`                                          | `ANY`                                                  |
| `eq(value)`                                            | `value` (MagicMock utilise `==` par défaut)            |

---

## Calendar → datetime

`options.get_cut_off_planning_h()` est supposé retourner un `datetime.datetime`.

| Java                          | Python             |
|-------------------------------|--------------------|
| `calendar.get(Calendar.DATE)` | `calendar.day`     |
| `calendar.get(Calendar.HOUR_OF_DAY)` | `calendar.hour` |
| `calendar.get(Calendar.MINUTE)` | `calendar.minute` |

⚠️ À vérifier lors de la migration du code source.

---

## Autres décisions

| Sujet                              | Décision                                                                        |
|------------------------------------|---------------------------------------------------------------------------------|
| Nommage des méthodes               | **snake_case** (standard Python)                                                |
| `saveSimultationResult` (typo Java) | Corrigé en `save_simulation_result`                                            |
| `Thread.sleep(200)`                | `time.sleep(0.2)` (millisecondes → secondes)                                   |
| `Arrays.copyOfRange(arr, 0, n)`    | `arr[:n]` (slice Python)                                                        |
| `FileManagementTests` (base class) | `conftest.py` avec fixture `file_management` + `autouse=True` dans chaque classe |
| `switch` dans test paramétré       | Colonne `expected` dans `@pytest.mark.parametrize` (plus lisible)              |
| Chemin hardcodé integration tests  | Conservé tel quel (`PATH_OUT`), à adapter manuellement                          |

---

## Points d'attention lors de la migration du code source

1. **`get_cut_off_planning_h()`** doit retourner un `datetime.datetime`.
2. **`find_value()`** dans `ConcreteModifier` doit être une `@staticmethod`.
3. **`read_parameters_file()`** dans `SimpleSimulationHandler` doit accepter
   à la fois un `str` (chemin) et un `io.BytesIO` (stream).
4. **`content_of_a_file()`** doit concaténer les lignes **sans** séparateur.
5. **`save_simulation_result()`** (anciennement `saveSimultationResult`) :
   corriger le nom lors de la migration.
