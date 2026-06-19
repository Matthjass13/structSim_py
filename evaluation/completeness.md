# Completeness — Java to Python Migration

> **Decisions**
> - **Column order:** Java original → Transpiler → Zero-Shot → One-Shot → Chain-of-Thought. Within each LLM group, order is arbitrary.
> - **Row order:** packages in order experimenthandling → interfaces → gluecode → util. Within each package, order is arbitrary.
> - **Aggregation:** **sum** for all tables. The Java original column has no completeness score (it is the reference), so it is omitted from the presence table.
> - **N/A** in ZS/negConst and ZS/onlyTask for the 5 interface files: those classes were not generated → counted as **0** in presence.

## Class Presence (1 = present, 0 = absent)

Whether each class was found in the migrated Python code. **N/A cells do not exist here** — absent classes are **0**.

**Package legend:** 🔵 experimenthandling · 🟣 interfaces · 🟢 gluecode · 🔴 util

**Column groups:** Java = original Java source · Transpiler = auto-transpiler · ZS = Zero-Shot · OS = One-Shot · CoT = Chain-of-Thought

| Class                          | ║ | Transpiler | ║ | ZS/negConst  | ZS/onlyTask  | ZS/persona  | ZS/withCtx  | ║ | OS/aSimHdlr  | OS/concMod  | OS/expPlanGen | ║ | CoT/perClass  | CoT/lenient  | CoT/strict  | CoT/riskFirst |
| ------------------------------ |:--:| ---------- |:--:| ------------ | ------------ | ----------- | ----------- |:--:| ------------ | ----------- | ------------- |:--:| ------------- | ------------ | ----------- | ------------- |
| ══════════════════════════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| 🔵 Environment                  | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🔵 Parameter                    | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🔵 ExperimentPlanGenerator      | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🔵 ExperimentResultHandler      | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🔵 Measure                      | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🔵 ExperimentSimulatorHandler   | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🔵 Options                      | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| ══════════════════════════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| 🟣 AModifier                    | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟣 ASimulationSystemHandler     | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟣 StartProgram                 | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟣 IExtractMeasures             | ║ |     1      | ║ |      0       |      0       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟣 IStopProgram                 | ║ |     1      | ║ |      0       |      0       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟣 IManageParametersFile        | ║ |     1      | ║ |      0       |      0       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟣 IStartSimulation             | ║ |     1      | ║ |      0       |      0       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟣 IManageModifier              | ║ |     1      | ║ |      0       |      0       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| ══════════════════════════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| 🟢 Simulation                   | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟢 MySimulator                  | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟢 ConcreteModifier             | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟢 SimpleSimulationHandler      | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| ══════════════════════════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| 🔴 FileManagement               | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| ****Σ present****                | ║ |     20     | ║ |      15      |      15      |     20      |     20      | ║ |      20      |     20      |      20       | ║ |      20       |      20      |     20      |      20       |


---

## Number of Methods

Count of method definitions (`def` in Python, method declarations in Java).

**Package legend:** 🔵 experimenthandling · 🟣 interfaces · 🟢 gluecode · 🔴 util

**Column groups:** Java = original Java source · Transpiler = auto-transpiler · ZS = Zero-Shot · OS = One-Shot · CoT = Chain-of-Thought

| Class                          | ║ | Java Orig  | ║ | Transpiler | ║ | ZS/negConst  | ZS/onlyTask  | ZS/persona  | ZS/withCtx  | ║ | OS/aSimHdlr  | OS/concMod  | OS/expPlanGen | ║ | CoT/perClass  | CoT/lenient  | CoT/strict  | CoT/riskFirst |
| ------------------------------ |:--:| ---------- |:--:| ---------- |:--:| ------------ | ------------ | ----------- | ----------- |:--:| ------------ | ----------- | ------------- |:--:| ------------- | ------------ | ----------- | ------------- |
| ══════════════════════════════ | ══ | ══════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| 🔵 Environment                  | ║ |     14     | ║ |     14     | ║ |      16      |      14      |     16      |     15      | ║ |      17      |     17      |      14       | ║ |      19       |      14      |     18      |      14       |
| 🔵 Parameter                    | ║ |     7      | ║ |     7      | ║ |      6       |      6       |      7      |      8      | ║ |      9       |      7      |       2       | ║ |       9       |      6       |      7      |       6       |
| 🔵 ExperimentPlanGenerator      | ║ |     5      | ║ |     5      | ║ |      5       |      5       |      5      |      5      | ║ |      5       |      5      |       5       | ║ |       5       |      5       |      5      |       5       |
| 🔵 ExperimentResultHandler      | ║ |     2      | ║ |     2      | ║ |      2       |      2       |      2      |      2      | ║ |      2       |      2      |       2       | ║ |       2       |      2       |      2      |       2       |
| 🔵 Measure                      | ║ |     6      | ║ |     6      | ║ |      6       |      6       |      6      |      6      | ║ |      6       |      6      |       2       | ║ |       6       |      6       |      7      |       6       |
| 🔵 ExperimentSimulatorHandler   | ║ |     1      | ║ |     2      | ║ |      2       |      2       |      2      |      2      | ║ |      2       |      2      |       2       | ║ |       2       |      2       |      2      |       2       |
| 🔵 Options                      | ║ |     17     | ║ |     17     | ║ |      17      |      17      |     17      |     17      | ║ |      17      |     17      |       1       | ║ |      17       |      17      |     17      |      17       |
| ══════════════════════════════ | ══ | ══════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| 🟣 AModifier                    | ║ |     6      | ║ |     7      | ║ |      6       |      6       |      6      |      6      | ║ |      10      |      6      |       6       | ║ |      10       |      6       |      6      |       6       |
| 🟣 ASimulationSystemHandler     | ║ |     4      | ║ |     4      | ║ |      11      |      11      |      5      |      5      | ║ |      9       |      5      |       5       | ║ |       5       |      5       |     11      |       5       |
| 🟣 StartProgram                 | ║ |     1      | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟣 IExtractMeasures             | ║ |     1      | ║ |     1      | ║ |     N/A      |     N/A      |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟣 IStopProgram                 | ║ |     1      | ║ |     1      | ║ |     N/A      |     N/A      |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟣 IManageParametersFile        | ║ |     3      | ║ |     3      | ║ |     N/A      |     N/A      |      3      |      2      | ║ |      3       |      3      |       2       | ║ |       3       |      2       |      2      |       2       |
| 🟣 IStartSimulation             | ║ |     1      | ║ |     1      | ║ |     N/A      |     N/A      |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟣 IManageModifier              | ║ |     1      | ║ |     1      | ║ |     N/A      |     N/A      |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| ══════════════════════════════ | ══ | ══════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| 🟢 Simulation                   | ║ |     1      | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       0       |      1       |      1      |       1       |
| 🟢 MySimulator                  | ║ |     1      | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟢 ConcreteModifier             | ║ |     6      | ║ |     6      | ║ |      4       |      3       |      3      |      5      | ║ |      4       |      5      |       3       | ║ |       4       |      4       |      3      |       3       |
| 🟢 SimpleSimulationHandler      | ║ |     9      | ║ |     9      | ║ |      7       |      7       |      8      |      7      | ║ |      8       |      8      |       7       | ║ |       7       |      7       |      7      |       7       |
| ══════════════════════════════ | ══ | ══════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| 🔴 FileManagement               | ║ |     16     | ║ |     17     | ║ |      16      |      14      |     17      |     18      | ║ |      16      |     18      |      16       | ║ |      18       |      16      |     17      |      15       |
| ****Σ****                        | ║ |    103     | ║ |    106     | ║ |     101      |      96      |     104     |     105     | ║ |     115      |     108     |      74       | ║ |      113      |      99      |     111     |      97       |


---

## Number of Class Attributes

Instance attributes in `__init__` (Python) or class-level fields (Java). N/A = class absent.

**Package legend:** 🔵 experimenthandling · 🟣 interfaces · 🟢 gluecode · 🔴 util

**Column groups:** Java = original Java source · Transpiler = auto-transpiler · ZS = Zero-Shot · OS = One-Shot · CoT = Chain-of-Thought

| Class                          | ║ | Java Orig  | ║ | Transpiler | ║ | ZS/negConst  | ZS/onlyTask  | ZS/persona  | ZS/withCtx  | ║ | OS/aSimHdlr  | OS/concMod  | OS/expPlanGen | ║ | CoT/perClass  | CoT/lenient  | CoT/strict  | CoT/riskFirst |
| ------------------------------ |:--:| ---------- |:--:| ---------- |:--:| ------------ | ------------ | ----------- | ----------- |:--:| ------------ | ----------- | ------------- |:--:| ------------- | ------------ | ----------- | ------------- |
| ══════════════════════════════ | ══ | ══════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| 🔵 Environment                  | ║ |     5      | ║ |     3      | ║ |      5       |      5       |      5      |      5      | ║ |      5       |      5      |       5       | ║ |       5       |      5       |      5      |       5       |
| 🔵 Parameter                    | ║ |     2      | ║ |     2      | ║ |      2       |      2       |      2      |      2      | ║ |      2       |      2      |       2       | ║ |       2       |      2       |      2      |       2       |
| 🔵 ExperimentPlanGenerator      | ║ |     9      | ║ |     5      | ║ |      9       |      7       |      7      |      8      | ║ |      7       |      7      |       9       | ║ |       6       |      7       |      9      |       7       |
| 🔵 ExperimentResultHandler      | ║ |     5      | ║ |     4      | ║ |      4       |      4       |      4      |      4      | ║ |      4       |      4      |       4       | ║ |       4       |      4       |      4      |       4       |
| 🔵 Measure                      | ║ |     2      | ║ |     2      | ║ |      2       |      2       |      2      |      2      | ║ |      2       |      2      |       2       | ║ |       2       |      2       |      2      |       2       |
| 🔵 ExperimentSimulatorHandler   | ║ |     7      | ║ |     6      | ║ |      6       |      6       |      6      |      6      | ║ |      6       |      6      |       6       | ║ |       6       |      6       |      6      |       6       |
| 🔵 Options                      | ║ |     8      | ║ |     0      | ║ |      8       |      8       |      8      |      8      | ║ |      8       |      8      |       8       | ║ |       8       |      8       |      8      |       8       |
| ══════════════════════════════ | ══ | ══════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| 🟣 AModifier                    | ║ |     2      | ║ |     2      | ║ |      2       |      2       |      2      |      2      | ║ |      2       |      2      |       2       | ║ |       2       |      2       |      2      |       2       |
| 🟣 ASimulationSystemHandler     | ║ |     2      | ║ |     0      | ║ |      2       |      2       |      2      |      2      | ║ |      2       |      2      |       2       | ║ |       2       |      2       |      2      |       2       |
| 🟣 StartProgram                 | ║ |     0      | ║ |     0      | ║ |      0       |      0       |      0      |      0      | ║ |      0       |      0      |       0       | ║ |       0       |      0       |      0      |       0       |
| 🟣 IExtractMeasures             | ║ |     0      | ║ |     0      | ║ |     N/A      |     N/A      |      0      |      0      | ║ |      0       |      0      |       0       | ║ |       0       |      0       |      0      |       0       |
| 🟣 IStopProgram                 | ║ |     0      | ║ |     0      | ║ |     N/A      |     N/A      |      0      |      0      | ║ |      0       |      0      |       0       | ║ |       0       |      0       |      0      |       0       |
| 🟣 IManageParametersFile        | ║ |     0      | ║ |     0      | ║ |     N/A      |     N/A      |      0      |      0      | ║ |      0       |      0      |       0       | ║ |       0       |      0       |      0      |       0       |
| 🟣 IStartSimulation             | ║ |     0      | ║ |     0      | ║ |     N/A      |     N/A      |      0      |      0      | ║ |      0       |      0      |       0       | ║ |       0       |      0       |      0      |       0       |
| 🟣 IManageModifier              | ║ |     0      | ║ |     0      | ║ |     N/A      |     N/A      |      0      |      0      | ║ |      0       |      0      |       0       | ║ |       0       |      0       |      0      |       0       |
| ══════════════════════════════ | ══ | ══════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| 🟢 Simulation                   | ║ |     0      | ║ |     0      | ║ |      0       |      0       |      0      |      0      | ║ |      0       |      0      |       0       | ║ |       0       |      0       |      0      |       0       |
| 🟢 MySimulator                  | ║ |     0      | ║ |     0      | ║ |      0       |      0       |      0      |      0      | ║ |      0       |      0      |       0       | ║ |       0       |      0       |      0      |       0       |
| 🟢 ConcreteModifier             | ║ |     1      | ║ |     4      | ║ |      3       |      3       |      3      |      4      | ║ |      3       |      3      |       3       | ║ |       3       |      3       |      3      |       3       |
| 🟢 SimpleSimulationHandler      | ║ |     1      | ║ |     0      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| ══════════════════════════════ | ══ | ══════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| 🔴 FileManagement               | ║ |     4      | ║ |     0      | ║ |      4       |      4       |      2      |      4      | ║ |      4       |      4      |       4       | ║ |       4       |      4       |      4      |       4       |
| ****Σ****                        | ║ |     48     | ║ |     28     | ║ |      48      |      46      |     44      |     48      | ║ |      46      |     46      |      48       | ║ |      45       |      46      |     48      |      46       |
