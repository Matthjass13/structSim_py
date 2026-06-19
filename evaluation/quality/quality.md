# Quality Metrics — Java to Python Migration

> - **N/A** = class absent from this migration, or (for CC) file has a Python syntax error preventing AST parsing (3 transpiler files: MySimulator, SimpleSimulationHandler, FileManagement).
> - The transpiler systematically scores **0.00** in Pylint because it outputs Java-style Python (PascalCase, no docstrings, etc.).

**Package legend:** 🔵 experimenthandling · 🟣 interfaces · 🟢 gluecode · 🔴 util
**Column groups:** Java = original Java source · Transpiler = auto-transpiler · ZS = Zero-Shot · OS = One-Shot · CoT = Chain-of-Thought

## Lines of Code (total, including blanks and comments)

| Class                          |  ║  | Java Orig  |  ║  | Transpiler |  ║  | ZS/negConst  | ZS/onlyTask  | ZS/persona | ZS/withCtx |  ║  | OS/aSimHdlr  | OS/concMod | OS/expPlanGen |  ║  | CoT/perClass | CoT/lenient  | CoT/strict | CoT/riskFirst |
| ------------------------------ | :-: | ---------- | :-: | ---------- | :-: | ------------ | ------------ | ---------- | ---------- | :-: | ------------ | ---------- | ------------- | :-: | ------------ | ------------ | ---------- | ------------- |
| ══════════════════════════════ | ══  | ══════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🔵 Environment                 |  ║  | 171        |  ║  | 174        |  ║  | 63           | 59           | 79         | 73         |  ║  | 81           | 71         | 64            |  ║  | 108          | 62           | 79         | 74            |
| 🔵 Parameter                   |  ║  | 93         |  ║  | 93         |  ║  | 24           | 25           | 25         | 32         |  ║  | 33           | 24         | 11            |  ║  | 51           | 23           | 31         | 25            |
| 🔵 ExperimentPlanGenerator     |  ║  | 208        |  ║  | 174        |  ║  | 103          | 99           | 129        | 130        |  ║  | 122          | 117        | 130           |  ║  | 127          | 104          | 113        | 113           |
| 🔵 ExperimentResultHandler     |  ║  | 104        |  ║  | 100        |  ║  | 33           | 37           | 53         | 45         |  ║  | 40           | 42         | 50            |  ║  | 72           | 39           | 35         | 47            |
| 🔵 Measure                     |  ║  | 88         |  ║  | 85         |  ║  | 20           | 20           | 21         | 21         |  ║  | 21           | 20         | 7             |  ║  | 34           | 19           | 22         | 21            |
| 🔵 ExperimentSimulatorHandler  |  ║  | 114        |  ║  | 102        |  ║  | 50           | 50           | 74         | 63         |  ║  | 66           | 67         | 75            |  ║  | 86           | 55           | 61         | 62            |
| 🔵 Options                     |  ║  | 178        |  ║  | 176        |  ║  | 59           | 60           | 64         | 61         |  ║  | 64           | 60         | 14            |  ║  | 80           | 61           | 58         | 70            |
| ══════════════════════════════ | ══  | ══════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🟣 AModifier                   |  ║  | 100        |  ║  | 106        |  ║  | 24           | 24           | 29         | 29         |  ║  | 43           | 25         | 26            |  ║  | 61           | 23           | 24         | 31            |
| 🟣 ASimulationSystemHandler    |  ║  | 76         |  ║  | 79         |  ║  | 44           | 44           | 36         | 30         |  ║  | 60           | 25         | 31            |  ║  | 50           | 24           | 61         | 39            |
| 🟣 StartProgram                |  ║  | 105        |  ║  | 87         |  ║  | 34           | 38           | 47         | 48         |  ║  | 48           | 50         | 40            |  ║  | 74           | 40           | 48         | 51            |
| 🟣 IExtractMeasures            |  ║  | 48         |  ║  | 49         |  ║  | N/A          | N/A          | 9          | 11         |  ║  | 12           | 8          | 11            |  ║  | 23           | 8            | 8          | 11            |
| 🟣 IStopProgram                |  ║  | 38         |  ║  | 42         |  ║  | N/A          | N/A          | 8          | 10         |  ║  | 9            | 8          | 8             |  ║  | 16           | 7            | 8          | 9             |
| 🟣 IManageParametersFile       |  ║  | 75         |  ║  | 82         |  ║  | N/A          | N/A          | 15         | 22         |  ║  | 20           | 17         | 15            |  ║  | 36           | 16           | 16         | 15            |
| 🟣 IStartSimulation            |  ║  | 39         |  ║  | 41         |  ║  | N/A          | N/A          | 8          | 10         |  ║  | 9            | 8          | 8             |  ║  | 16           | 7            | 8          | 9             |
| 🟣 IManageModifier             |  ║  | 41         |  ║  | 43         |  ║  | N/A          | N/A          | 9          | 11         |  ║  | 10           | 8          | 12            |  ║  | 24           | 8            | 8          | 10            |
| ══════════════════════════════ | ══  | ══════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🟢 Simulation                  |  ║  | 31         |  ║  | 33         |  ║  | 20           | 23           | 25         | 29         |  ║  | 23           | 23         | 25            |  ║  | 45           | 26           | 26         | 33            |
| 🟢 MySimulator                 |  ║  | 35         |  ║  | 26         |  ║  | 20           | 22           | 20         | 25         |  ║  | 25           | 24         | 22            |  ║  | 39           | 23           | 25         | 20            |
| 🟢 ConcreteModifier            |  ║  | 79         |  ║  | 79         |  ║  | 51           | 38           | 43         | 54         |  ║  | 52           | 43         | 46            |  ║  | 62           | 41           | 52         | 57            |
| 🟢 SimpleSimulationHandler     |  ║  | 139        |  ║  | 116        |  ║  | 68           | 68           | 86         | 92         |  ║  | 92           | 86         | 78            |  ║  | 101          | 79           | 106        | 113           |
| ══════════════════════════════ | ══  | ══════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🔴 FileManagement              |  ║  | 439        |  ║  | 383        |  ║  | 152          | 136          | 190        | 209        |  ║  | 191          | 180        | 172           |  ║  | 219          | 154          | 227        | 189           |
| \***\*Σ\*\***                  |  ║  | 2201       |  ║  | 2070       |  ║  | 765          | 743          | 970        | 1005       |  ║  | 1021         | 906        | 845           |  ║  | 1324         | 819          | 1016       | 999           |

---

## Source Lines of Code (excluding blank lines and comments)

| Class                          |  ║  | Java Orig  |  ║  | Transpiler |  ║  | ZS/negConst  | ZS/onlyTask  | ZS/persona | ZS/withCtx |  ║  | OS/aSimHdlr  | OS/concMod | OS/expPlanGen |  ║  | CoT/perClass | CoT/lenient  | CoT/strict | CoT/riskFirst |
| ------------------------------ | :-: | ---------- | :-: | ---------- | :-: | ------------ | ------------ | ---------- | ---------- | :-: | ------------ | ---------- | ------------- | :-: | ------------ | ------------ | ---------- | ------------- |
| ══════════════════════════════ | ══  | ══════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🔵 Environment                 |  ║  | 69         |  ║  | 71         |  ║  | 45           | 41           | 52         | 52         |  ║  | 62           | 52         | 48            |  ║  | 65           | 47           | 54         | 50            |
| 🔵 Parameter                   |  ║  | 29         |  ║  | 30         |  ║  | 18           | 18           | 18         | 24         |  ║  | 24           | 17         | 10            |  ║  | 25           | 18           | 20         | 19            |
| 🔵 ExperimentPlanGenerator     |  ║  | 114        |  ║  | 93         |  ║  | 77           | 73           | 84         | 97         |  ║  | 95           | 89         | 95            |  ║  | 74           | 77           | 81         | 77            |
| 🔵 ExperimentResultHandler     |  ║  | 39         |  ║  | 28         |  ║  | 27           | 30           | 34         | 35         |  ║  | 33           | 35         | 40            |  ║  | 42           | 34           | 29         | 34            |
| 🔵 Measure                     |  ║  | 25         |  ║  | 24         |  ║  | 14           | 14           | 15         | 15         |  ║  | 15           | 14         | 6             |  ║  | 15           | 14           | 16         | 15            |
| 🔵 ExperimentSimulatorHandler  |  ║  | 52         |  ║  | 42         |  ║  | 39           | 37           | 47         | 49         |  ║  | 54           | 51         | 59            |  ║  | 52           | 43           | 49         | 43            |
| 🔵 Options                     |  ║  | 62         |  ║  | 62         |  ║  | 42           | 42           | 44         | 43         |  ║  | 45           | 42         | 12            |  ║  | 45           | 43           | 42         | 44            |
| ══════════════════════════════ | ══  | ══════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🟣 AModifier                   |  ║  | 30         |  ║  | 33         |  ║  | 16           | 16           | 17         | 17         |  ║  | 30           | 17         | 17            |  ║  | 33           | 16           | 17         | 17            |
| 🟣 ASimulationSystemHandler    |  ║  | 22         |  ║  | 22         |  ║  | 31           | 31           | 24         | 18         |  ║  | 40           | 18         | 23            |  ║  | 29           | 18           | 42         | 25            |
| 🟣 StartProgram                |  ║  | 39         |  ║  | 33         |  ║  | 24           | 25           | 29         | 29         |  ║  | 31           | 36         | 28            |  ║  | 32           | 24           | 30         | 31            |
| 🟣 IExtractMeasures            |  ║  | 6          |  ║  | 9          |  ║  | N/A          | N/A          | 6          | 8          |  ║  | 8            | 5          | 7             |  ║  | 9            | 6            | 6          | 8             |
| 🟣 IStopProgram                |  ║  | 4          |  ║  | 7          |  ║  | N/A          | N/A          | 5          | 7          |  ║  | 6            | 5          | 5             |  ║  | 6            | 5            | 6          | 6             |
| 🟣 IManageParametersFile       |  ║  | 9          |  ║  | 18         |  ║  | N/A          | N/A          | 10         | 10         |  ║  | 14           | 12         | 10            |  ║  | 17           | 9            | 9          | 11            |
| 🟣 IStartSimulation            |  ║  | 4          |  ║  | 7          |  ║  | N/A          | N/A          | 5          | 7          |  ║  | 6            | 5          | 5             |  ║  | 6            | 5            | 6          | 6             |
| 🟣 IManageModifier             |  ║  | 5          |  ║  | 8          |  ║  | N/A          | N/A          | 6          | 8          |  ║  | 7            | 5          | 8             |  ║  | 10           | 6            | 6          | 7             |
| ══════════════════════════════ | ══  | ══════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🟢 Simulation                  |  ║  | 19         |  ║  | 21         |  ║  | 13           | 15           | 13         | 20         |  ║  | 16           | 16         | 16            |  ║  | 18           | 16           | 15         | 19            |
| 🟢 MySimulator                 |  ║  | 29         |  ║  | 20         |  ║  | 16           | 18           | 13         | 21         |  ║  | 21           | 20         | 17            |  ║  | 18           | 20           | 19         | 17            |
| 🟢 ConcreteModifier            |  ║  | 62         |  ║  | 57         |  ║  | 42           | 32           | 32         | 45         |  ║  | 44           | 36         | 39            |  ║  | 35           | 34           | 39         | 42            |
| 🟢 SimpleSimulationHandler     |  ║  | 116        |  ║  | 96         |  ║  | 57           | 58           | 50         | 78         |  ║  | 81           | 74         | 66            |  ║  | 68           | 66           | 71         | 74            |
| ══════════════════════════════ | ══  | ══════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🔴 FileManagement              |  ║  | 265        |  ║  | 207        |  ║  | 124          | 112          | 130        | 154        |  ║  | 162          | 151        | 140           |  ║  | 140          | 124          | 149        | 124           |
| ══════════════════════════════ | ══  | ══════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| \***\*Σ\*\***                  |  ║  | 1000       |  ║  | 888        |  ║  | 585          | 562          | 634        | 737        |  ║  | 794          | 700        | 651           |  ║  | 739          | 625          | 706        | 669           |

### Analysis

**General pattern — Python is shorter than Java across all LLM migrations** — The total SLOC drops from 1000 (Java) to 562–794 (LLM migrations), a 20–45 % reduction. The main drivers are: no type declarations on every line, no explicit getter/setter pairs (replaced by direct attribute access), and no boilerplate Java scaffolding (imports of `java.util.*`, `java.io.*`, etc.). The transpiler (888) stays closest to Java because it is a line-by-line translation.

**`ASimulationSystemHandler` — ZS/negConst=31, ZS/onlyTask=31, OS/aSimHdlr=40, CoT/strict=42 (vs. Java=22)** — All four are above Java. ZS/negConst and ZS/onlyTask inflate because they re-declared 11 methods (including all inherited abstract stubs), adding ~9 extra `def` lines each. OS/aSimHdlr goes further (40 SLOC) because it also adds `@property` decorators, type hints, and private backing attributes (`_options`, `_list_modifier_class`), doubling the accessor code.

**Transpiler interfaces slightly above Java (e.g. IStopProgram Java=4, Transpiler=7)** — The transpiler outputs a `__metaclass__ = ABCMeta` line (Python 2 style), adds an `@abstractmethod` decorator block, and occasionally copies across Java comment stubs that did not exist in the original source SLOC count. This adds 2–3 lines per interface above the Java figure.

**`OS/expPlanGen` very low: Parameter=10 (Java=29), Measure=6 (Java=25), Options=12 (Java=62)** — The one-shot example that was in the prompt focused on `ExperimentPlanGenerator`. The model generalised an extremely minimalist style to the remaining classes: it dropped all getters and setters and kept only `__init__` (and `__str__` for Parameter). Options goes from 62 SLOC (Java, with 8 getters + 8 setters + constructor) to 12 SLOC (Python, `__init__` only, 8 attribute assignments).

---

## Pylint Score (out of 10)

Score from `pylint` (errors, warnings, conventions, refactoring). No Java original. Transpiler = 0.00 by design.

| Class                          |  ║  | Transpiler |  ║  | ZS/negConst  | ZS/onlyTask  | ZS/persona | ZS/withCtx |  ║  | OS/aSimHdlr  | OS/concMod | OS/expPlanGen |  ║  | CoT/perClass | CoT/lenient  | CoT/strict | CoT/riskFirst |
| ------------------------------ | :-: | ---------- | :-: | ------------ | ------------ | ---------- | ---------- | :-: | ------------ | ---------- | ------------- | :-: | ------------ | ------------ | ---------- | ------------- |
| ══════════════════════════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🔵 Environment                 |  ║  | 0.00       |  ║  | 6.82         | 5.00         | 6.22       | 6.80       |  ║  | 7.35         | 6.60       | 6.38          |  ║  | 6.98         | 5.56         | 7.25       | 6.51          |
| 🔵 Parameter                   |  ║  | 0.00       |  ║  | 6.47         | 6.47         | 6.25       | 7.27       |  ║  | 6.00         | 5.62       | 6.67          |  ║  | 6.50         | 6.47         | 6.84       | 6.47          |
| 🔵 ExperimentPlanGenerator     |  ║  | 0.00       |  ║  | 8.36         | 8.03         | 7.31       | 8.39       |  ║  | 7.97         | 8.85       | 9.47          |  ║  | 7.78         | 6.81         | 9.59       | 8.31          |
| 🔵 ExperimentResultHandler     |  ║  | 0.00       |  ║  | 7.08         | 7.04         | 5.48       | 7.74       |  ║  | 7.86         | 7.42       | 8.67          |  ║  | 7.67         | 7.67         | 8.40       | 7.74          |
| 🔵 Measure                     |  ║  | 0.00       |  ║  | 5.71         | 5.71         | 6.43       | 6.43       |  ║  | 6.43         | 5.71       | 5.00          |  ║  | 7.14         | 5.71         | 6.25       | 5.71          |
| 🔵 ExperimentSimulatorHandler  |  ║  | 0.00       |  ║  | 6.56         | 5.59         | 3.71       | 6.67       |  ║  | 7.27         | 7.11       | 7.44          |  ║  | 6.39         | 5.41         | 8.28       | 7.18          |
| 🔵 Options                     |  ║  | 0.00       |  ║  | 5.48         | 5.48         | 5.81       | 5.71       |  ║  | 5.91         | 5.48       | 6.67          |  ║  | 6.14         | 5.58         | 5.48       | 5.68          |
| ══════════════════════════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🟣 AModifier                   |  ║  | 0.00       |  ║  | 5.33         | 5.33         | 6.00       | 6.00       |  ║  | 6.96         | 5.62       | 5.62          |  ║  | 7.31         | 5.33         | 5.33       | 6.00          |
| 🟣 ASimulationSystemHandler    |  ║  | 0.00       |  ║  | 5.20         | 5.20         | 0.00       | 6.67       |  ║  | 8.21         | 6.47       | 6.67          |  ║  | 0.00         | 0.00         | 8.33       | 6.84          |
| 🟣 StartProgram                |  ║  | 0.00       |  ║  | 7.83         | 0.00         | 0.00       | 8.52       |  ║  | 8.40         | 7.10       | 7.78          |  ║  | 0.33         | 0.00         | 8.33       | 7.86          |
| 🟣 IExtractMeasures            |  ║  | 0.00       |  ║  | N/A          | N/A          | 4.00       | 4.00       |  ║  | 6.00         | 0.00       | 3.33          |  ║  | 0.00         | 2.00         | 0.00       | 4.00          |
| 🟣 IStopProgram                |  ║  | 0.00       |  ║  | N/A          | N/A          | 2.50       | 2.50       |  ║  | 3.33         | 0.00       | 0.00          |  ║  | 5.00         | 0.00         | 0.00       | 0.00          |
| 🟣 IManageParametersFile       |  ║  | 0.00       |  ║  | N/A          | N/A          | 5.56       | 4.29       |  ║  | 7.14         | 3.33       | 2.50          |  ║  | 1.00         | 4.29         | 3.33       | 5.00          |
| 🟣 IStartSimulation            |  ║  | 0.00       |  ║  | N/A          | N/A          | 2.50       | 2.50       |  ║  | 3.33         | 0.00       | 0.00          |  ║  | 5.00         | 0.00         | 0.00       | 0.00          |
| 🟣 IManageModifier             |  ║  | 0.00       |  ║  | N/A          | N/A          | 4.00       | 4.00       |  ║  | 5.00         | 0.00       | 4.29          |  ║  | 5.71         | 2.00         | 0.00       | 2.50          |
| ══════════════════════════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🟢 Simulation                  |  ║  | 0.00       |  ║  | 8.00         | 0.00         | 0.00       | 8.00       |  ║  | 8.18         | 7.50       | 5.83          |  ║  | 0.00         | 0.00         | 8.18       | 5.33          |
| 🟢 MySimulator                 |  ║  | 0.00       |  ║  | 6.67         | 7.06         | 7.50       | 6.84       |  ║  | 6.84         | 6.32       | 5.62          |  ║  | 6.88         | 6.32         | 7.78       | 7.33          |
| 🟢 ConcreteModifier            |  ║  | 0.00       |  ║  | 8.72         | 6.77         | 3.87       | 8.46       |  ║  | 9.39         | 8.06       | 8.93          |  ║  | 5.33         | 4.84         | 9.44       | 8.29          |
| 🟢 SimpleSimulationHandler     |  ║  | 0.00       |  ║  | 8.93         | 4.74         | 3.60       | 8.00       |  ║  | 8.50         | 9.59       | 7.85          |  ║  | 4.85         | 5.69         | 8.57       | 8.77          |
| ══════════════════════════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🔴 FileManagement              |  ║  | 0.00       |  ║  | 8.05         | 7.00         | 7.11       | 8.91       |  ║  | 9.14         | 8.11       | 8.12          |  ║  | 8.70         | 7.67         | 7.99       | 7.72          |
| ══════════════════════════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| \***\*avg\*\***                |  ║  | 0.00       |  ║  | 7.01         | 5.29         | 4.39       | 6.39       |  ║  | 6.96         | 5.44       | 5.84          |  ║  | 4.94         | 4.07         | 5.97       | 5.86          |

### Analysis

**Transpiler = 0.00 by construction** — The transpiler outputs Java naming conventions (PascalCase methods, no docstrings, `camelCase` variables) which trigger hundreds of convention and warning messages. For most files the score turns negative under Pylint's formula (capped at 0). This is an expected and documented artefact.

**Pylint=0.00 in non-transpiler files: two distinct causes**

1. *Unresolvable imports (dominant cause for most 0.00 scores)* — Pylint was run on each file in isolation without adjusting `PYTHONPATH`. Files that use package-relative imports such as `from gluecode.concrete_modifier import ConcreteModifier` or `from noStrategy.experimenthandling.environment import Environment` (e.g. `ZS/onlyTask/start_program.py` which sits at the repository root and imports via a `noStrategy.*` namespace) trigger `E0401` import-error. A single `E0401` is an error-category message and heavily penalises the formula `10 − (5·E + W + R + C) / statements`. For files with few statements, this drives the score to 0. This explains the 0.00 for `Simulation` (CoT/perClass), `StartProgram` (ZS/onlyTask, ZS/persona, CoT/lenient, CoT/perClass), and `ASimulationSystemHandler` (ZS/persona, CoT/perClass, CoT/lenient).

2. *Too few statements in small interface files* — `IStopProgram`, `IStartSimulation`, `IExtractMeasures`, and `IManageModifier` are 6–7 SLOC with a single `@abstractmethod`. Pylint flags missing module docstring (C0114), missing class docstring (C0115), and missing method docstring (C0116) — 3 convention messages for a file with ≈3 statements. The penalty formula yields 0 or below. This explains the scattered 0.00 and near-0 scores in the interfaces block.

**`ZS/persona` is the lowest-scoring LLM strategy (avg 4.39)** — The persona prompt produced files without docstrings in many classes (triggering C0114/C0115/C0116 across large files), used non-idiomatic names (still sometimes camelCase), and for `ExperimentSimulatorHandler` generated a 3.71 score due to several missing type annotations and a deeply nested `run` method flagged for refactoring.

**`OS/expPlanGen` peaks for `ExperimentPlanGenerator` (9.47) and `CoT/strict` peaks for the same class (9.59)** — Both migrations produced well-structured, fully documented, PEP-8 compliant code for `ExperimentPlanGenerator`, the class used as the one-shot example. This is the highest individual Pylint score in the table and shows that the one-shot example class received particular care.

**`Options` is consistently the lowest-scoring experimenthandling class (5.48–6.67)** — Options has 17 methods (8 getters + 8 setters). Pylint penalises each missing docstring individually, and with 17 methods the absolute penalty is high even if relative quality is moderate.

---

## Pyright Error Count

Type errors from `pyright` per file in isolation. Warnings and info were 0 across all files.

| Class                          |  ║  | Transpiler |  ║  | ZS/negConst  | ZS/onlyTask  | ZS/persona | ZS/withCtx |  ║  | OS/aSimHdlr  | OS/concMod | OS/expPlanGen |  ║  | CoT/perClass | CoT/lenient  | CoT/strict | CoT/riskFirst |
| ------------------------------ | :-: | ---------- | :-: | ------------ | ------------ | ---------- | ---------- | :-: | ------------ | ---------- | ------------- | :-: | ------------ | ------------ | ---------- | ------------- |
| ══════════════════════════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🔵 Environment                 |  ║  | 19         |  ║  | 0            | 1            | 0          | 3          |  ║  | 1            | 1          | 1             |  ║  | 0            | 3            | 0          | 0             |
| 🔵 Parameter                   |  ║  | 4          |  ║  | 2            | 0            | 0          | 0          |  ║  | 0            | 0          | 1             |  ║  | 0            | 0            | 0          | 1             |
| 🔵 ExperimentPlanGenerator     |  ║  | 45         |  ║  | 0            | 1            | 3          | 0          |  ║  | 6            | 3          | 1             |  ║  | 6            | 1            | 0          | 4             |
| 🔵 ExperimentResultHandler     |  ║  | 18         |  ║  | 0            | 0            | 1          | 0          |  ║  | 1            | 0          | 0             |  ║  | 2            | 0            | 0          | 1             |
| 🔵 Measure                     |  ║  | 0          |  ║  | 0            | 0            | 0          | 0          |  ║  | 0            | 0          | 0             |  ║  | 0            | 0            | 0          | 0             |
| 🔵 ExperimentSimulatorHandler  |  ║  | 22         |  ║  | 0            | 1            | 3          | 0          |  ║  | 1            | 0          | 1             |  ║  | 9            | 0            | 0          | 4             |
| 🔵 Options                     |  ║  | 2          |  ║  | 0            | 0            | 0          | 5          |  ║  | 0            | 1          | 0             |  ║  | 0            | 6            | 0          | 0             |
| ══════════════════════════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🟣 AModifier                   |  ║  | 6          |  ║  | 0            | 0            | 0          | 0          |  ║  | 0            | 0          | 0             |  ║  | 0            | 0            | 0          | 0             |
| 🟣 ASimulationSystemHandler    |  ║  | 12         |  ║  | 0            | 0            | 0          | 0          |  ║  | 0            | 0          | 0             |  ║  | 0            | 0            | 0          | 0             |
| 🟣 StartProgram                |  ║  | 22         |  ║  | 1            | 4            | 2          | 0          |  ║  | 3            | 2          | 0             |  ║  | 3            | 0            | 0          | 1             |
| 🟣 IExtractMeasures            |  ║  | 4          |  ║  | N/A          | N/A          | 0          | 0          |  ║  | 0            | 0          | 0             |  ║  | 0            | 0            | 0          | 0             |
| 🟣 IStopProgram                |  ║  | 2          |  ║  | N/A          | N/A          | 0          | 0          |  ║  | 0            | 0          | 0             |  ║  | 0            | 0            | 0          | 0             |
| 🟣 IManageParametersFile       |  ║  | 10         |  ║  | N/A          | N/A          | 0          | 0          |  ║  | 0            | 0          | 0             |  ║  | 0            | 0            | 0          | 0             |
| 🟣 IStartSimulation            |  ║  | 2          |  ║  | N/A          | N/A          | 0          | 0          |  ║  | 0            | 0          | 0             |  ║  | 0            | 0            | 0          | 0             |
| 🟣 IManageModifier             |  ║  | 3          |  ║  | N/A          | N/A          | 0          | 0          |  ║  | 0            | 0          | 0             |  ║  | 0            | 0            | 0          | 0             |
| ══════════════════════════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🟢 Simulation                  |  ║  | 13         |  ║  | 2            | 3            | 1          | 0          |  ║  | 1            | 0          | 1             |  ║  | 2            | 0            | 0          | 0             |
| 🟢 MySimulator                 |  ║  | 15         |  ║  | 0            | 0            | 0          | 0          |  ║  | 0            | 0          | 0             |  ║  | 0            | 0            | 0          | 0             |
| 🟢 ConcreteModifier            |  ║  | 14         |  ║  | 0            | 1            | 0          | 2          |  ║  | 0            | 0          | 12            |  ║  | 0            | 1            | 0          | 0             |
| 🟢 SimpleSimulationHandler     |  ║  | 67         |  ║  | 4            | 3            | 2          | 3          |  ║  | 6            | 2          | 3             |  ║  | 3            | 2            | 1          | 7             |
| ══════════════════════════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🔴 FileManagement              |  ║  | 106        |  ║  | 9            | 9            | 10         | 7          |  ║  | 7            | 0          | 0             |  ║  | 13           | 7            | 11         | 8             |
| ══════════════════════════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| \***\*Σ\*\***                  |  ║  | 386        |  ║  | 18           | 23           | 22         | 20         |  ║  | 26           | 9          | 20            |  ║  | 38           | 20           | 12         | 26            |

### Analysis

**Transpiler total=386 — one order of magnitude worse than any LLM migration** — The transpiler output is syntactically invalid Python in several files (Java `import` statements left verbatim, Java-style casts, raw `instanceof` keywords). Pyright cannot resolve any type in such files and reports a type error for every expression. `FileManagement` alone accounts for 106 of the 386 errors. The remaining high-error transpiler files (`ExperimentPlanGenerator`=45, `SimpleSimulationHandler`=67) contain the same class of structural defect.

**`Measure` = 0 errors across all migrations** — `Measure` is a simple data class: two attributes (`name: str`, `value: float`) and four accessors with no complex type interactions. There is nothing for Pyright to flag — no generics, no optional chaining, no polymorphism.

**`AModifier`, `ASimulationSystemHandler`, `MySimulator` = 0 across all LLM migrations** — These abstract and thin classes have trivial signatures. `AModifier` declares `modify(env: Environment) → Environment`; `ASimulationSystemHandler` stores `options` and `list_modifier_class` with loose types; `MySimulator.run()` works with plain `dict` and `str`. None of these create type ambiguity.

**`ConcreteModifier` OS/expPlanGen = 12 errors** — This is the highest error count for any LLM migration cell. The file uses a `match/case` statement (Python 3.10+ syntax) for operator dispatch. Pyright defaults to checking against the project's minimum supported Python version; if that is set below 3.10, every `case` branch is flagged as a syntax/type error. No other migration uses `match/case` for this class.

**`CoT/perClass` total=38 — highest among LLM migrations** — The chain-of-thought per-class strategy produced more complex implementations with richer type interactions (generics, `Optional`, cross-class calls), which increases the surface area for Pyright to find mismatches. `ExperimentSimulatorHandler` (9) and `ExperimentPlanGenerator` (6) are the main contributors.

**`OS/concMod` total=9 — lowest among LLM migrations** — The concrete-modifier one-shot example favoured simple, well-typed code. The only errors come from `SimpleSimulationHandler` (2) and a handful of minor annotation gaps. No class in this migration uses advanced typing constructs that could introduce errors.

---

## Cyclomatic Complexity (Radon-equivalent)

Total CC of all functions per file: CC = Σ (1 + decision points). Computed via AST (Python) / decision-point regex (Java).

| Class                          |  ║  | Java Orig  |  ║  | Transpiler |  ║  | ZS/negConst  | ZS/onlyTask  | ZS/persona | ZS/withCtx |  ║  | OS/aSimHdlr  | OS/concMod | OS/expPlanGen |  ║  | CoT/perClass | CoT/lenient  | CoT/strict | CoT/riskFirst |
| ------------------------------ | :-: | ---------- | :-: | ---------- | :-: | ------------ | ------------ | ---------- | ---------- | :-: | ------------ | ---------- | ------------- | :-: | ------------ | ------------ | ---------- | ------------- |
| ══════════════════════════════ | ══  | ══════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🔵 Environment                 |  ║  | 14         |  ║  | 17         |  ║  | 19           | 17           | 18         | 21         |  ║  | 21           | 21         | 19            |  ║  | 22           | 18           | 22         | 19            |
| 🔵 Parameter                   |  ║  | 5          |  ║  | 7          |  ║  | 7            | 7            | 7          | 8          |  ║  | 9            | 7          | 3             |  ║  | 9            | 7            | 8          | 7             |
| 🔵 ExperimentPlanGenerator     |  ║  | 19         |  ║  | 19         |  ║  | 19           | 19           | 19         | 21         |  ║  | 18           | 20         | 15            |  ║  | 16           | 18           | 19         | 17            |
| 🔵 ExperimentResultHandler     |  ║  | 3          |  ║  | 4          |  ║  | 5            | 6            | 6          | 6          |  ║  | 5            | 6          | 4             |  ║  | 5            | 6            | 6          | 6             |
| 🔵 Measure                     |  ║  | 5          |  ║  | 6          |  ║  | 6            | 6            | 6          | 6          |  ║  | 6            | 6          | 2             |  ║  | 6            | 6            | 7          | 6             |
| 🔵 ExperimentSimulatorHandler  |  ║  | 5          |  ║  | 7          |  ║  | 6            | 6            | 6          | 6          |  ║  | 6            | 6          | 6             |  ║  | 5            | 8            | 6          | 8             |
| 🔵 Options                     |  ║  | 16         |  ║  | 17         |  ║  | 17           | 17           | 17         | 17         |  ║  | 17           | 17         | 1             |  ║  | 17           | 17           | 17         | 17            |
| ══════════════════════════════ | ══  | ══════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🟣 AModifier                   |  ║  | 4          |  ║  | 7          |  ║  | 6            | 6            | 6          | 6          |  ║  | 10           | 6          | 6             |  ║  | 10           | 6            | 6          | 6             |
| 🟣 ASimulationSystemHandler    |  ║  | 4          |  ║  | 4          |  ║  | 11           | 11           | 5          | 5          |  ║  | 9            | 5          | 5             |  ║  | 5            | 5            | 11         | 5             |
| 🟣 StartProgram                |  ║  | 3          |  ║  | 3          |  ║  | 4            | 3            | 4          | 3          |  ║  | 3            | 5          | 3             |  ║  | 5            | 3            | 3          | 3             |
| 🟣 IExtractMeasures            |  ║  | 1          |  ║  | 1          |  ║  | N/A          | N/A          | 1          | 1          |  ║  | 1            | 1          | 1             |  ║  | 1            | 1            | 1          | 1             |
| 🟣 IStopProgram                |  ║  | 1          |  ║  | 1          |  ║  | N/A          | N/A          | 1          | 1          |  ║  | 1            | 1          | 1             |  ║  | 1            | 1            | 1          | 1             |
| 🟣 IManageParametersFile       |  ║  | 1          |  ║  | 3          |  ║  | N/A          | N/A          | 3          | 2          |  ║  | 3            | 3          | 2             |  ║  | 3            | 2            | 2          | 2             |
| 🟣 IStartSimulation            |  ║  | 1          |  ║  | 1          |  ║  | N/A          | N/A          | 1          | 1          |  ║  | 1            | 1          | 1             |  ║  | 1            | 1            | 1          | 1             |
| 🟣 IManageModifier             |  ║  | 1          |  ║  | 1          |  ║  | N/A          | N/A          | 1          | 1          |  ║  | 1            | 1          | 1             |  ║  | 1            | 1            | 1          | 1             |
| ══════════════════════════════ | ══  | ══════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🟢 Simulation                  |  ║  | 1          |  ║  | 1          |  ║  | 1            | 1            | 1          | 1          |  ║  | 2            | 1          | 1             |  ║  | 1            | 1            | 1          | 2             |
| 🟢 MySimulator                 |  ║  | 3          |  ║  | N/A        |  ║  | 5            | 6            | 5          | 6          |  ║  | 6            | 6          | 5             |  ║  | 6            | 6            | 6          | 5             |
| 🟢 ConcreteModifier            |  ║  | 10         |  ║  | 14         |  ║  | 17           | 14           | 11         | 15         |  ║  | 12           | 9          | 7             |  ║  | 12           | 12           | 18         | 14            |
| 🟢 SimpleSimulationHandler     |  ║  | 16         |  ║  | N/A        |  ║  | 18           | 20           | 20         | 24         |  ║  | 23           | 23         | 19            |  ║  | 25           | 21           | 23         | 25            |
| ══════════════════════════════ | ══  | ══════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| 🔴 FileManagement              |  ║  | 46         |  ║  | N/A        |  ║  | 38           | 40           | 47         | 53         |  ║  | 55           | 57         | 47            |  ║  | 44           | 44           | 62         | 44            |
| ══════════════════════════════ | ══  | ══════════ | ══  | ══════════ | ══  | ════════════ | ════════════ | ══════════ | ══════════ | ══  | ════════════ | ══════════ | ════════════  | ══  | ════════════ | ════════════ | ══════════ | ════════════  |
| \***\*Σ\*\***                  |  ║  | 159        |  ║  | 113        |  ║  | 179          | 179          | 185        | 204        |  ║  | 209          | 202        | 149           |  ║  | 195          | 184          | 221        | 190           |

### Analysis

**LLM migrations are universally more complex than Java (total 179–221 vs. 159)** — The transpiler is the only migration *below* Java (113), because it contains syntax errors that prevent AST parsing for three files (`MySimulator`, `SimpleSimulationHandler`, `FileManagement` → all N/A), drastically reducing its countable total.

**`Options` OS/expPlanGen = 1 (vs. Java=16, all others=17)** — Options has 17 getters and setters in Java; each trivial `return field` contributes CC=1, summing to 17. The OS/expPlanGen version collapses Options to a single `__init__` method → CC=1. This is the starkest CC outlier in the table and is a direct consequence of eliminating accessor methods.

**`AModifier` and `ASimulationSystemHandler` — same migrations inflated in CC as in methods** — OS/aSimHdlr and CoT/perClass show CC=10 for `AModifier` (vs. Java=4), and ZS/negConst/ZS/onlyTask/CoT/strict show CC=11 for `ASimulationSystemHandler` (vs. Java=4). This is mechanically explained by the extra abstract method stubs discussed in the Methods analysis: each additional `def` with a single `pass` body still contributes CC=1, so 6–7 extra stubs translate directly to +6/+7 CC.

**`MySimulator` — Java=3 vs. Python=5–6** — The Java version has one `while` loop and one `try/catch` → CC=3. Python migrations rewrite file I/O using `with open(...) as f: for line in f:` — the `for` loop is +1, and many migrations also add an explicit `if "val1" in params and "val2" in params:` guard before the multiplication to avoid a `KeyError`, which adds another +1 or +2. The result is CC=5–6 despite semantically equivalent logic.

**`SimpleSimulationHandler` and `FileManagement` — Python consistently higher than Java** — Both Java classes use checked exceptions (try/catch blocks counted once) and compact loops. Python rewrites use `isinstance` checks (each +1), multiple `except` clauses (each +1), and explicit `if path: / if not path:` null-guard patterns that Java handles via type safety. `FileManagement` is the most complex class overall; CoT/strict reaches CC=62 (vs. Java=46) because it adds more fine-grained error-path branches (e.g. separate `except OSError`, `except ValueError`, `except IOError` blocks where Java had a single `catch (Exception e)`).

**`OS/expPlanGen` total=149 — lowest LLM migration** — The minimalist style (no getters/setters for Options, Parameter, Measure) removes dozens of trivial CC=1 functions. The total CC is structurally lower, not because the logic is simpler, but because large parts of the API surface were omitted.
