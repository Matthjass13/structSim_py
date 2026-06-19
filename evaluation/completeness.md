# Completeness — Java to Python Migration

> **Decisions**
> - **Column order:** Java original → Transpiler → Zero-Shot → One-Shot → Chain-of-Thought. Within each LLM group, order is arbitrary.
> - **Row order:** packages in order experimenthandling → interfaces → gluecode → util. Within each package, order is arbitrary.
> - **Aggregation:** **sum** = total number of classes present (out of 20). The Java original column has no meaningful completeness score (it is the reference), so it is omitted from the table.
> - **N/A** in ZS/negConst and ZS/onlyTask for the 5 interface files: those classes were not generated → counted as **0**.

## Class Presence (1 = present, 0 = absent)

Whether each class was found in the migrated Python code. **N/A cells do not exist here** — absent classes are **0**.

**Package legend:** 🔵 experimenthandling · 🟣 interfaces · 🟢 gluecode · 🔴 util

**Column groups:** Java = original Java source · Transpiler = auto-transpiler · ZS = Zero-Shot · OS = One-Shot · CoT = Chain-of-Thought

| Class                          | ║ | Transpiler | ║ | ZS/negConst  | ZS/onlyTask  | ZS/persona  | ZS/withCtx  | ║ | OS/aSimHdlr  | OS/concMod  | OS/expPlanGen | ║ | CoT/perClass  | CoT/lenient  | CoT/strict  | CoT/riskFirst |
| ------------------------------ |:--:| ---------- |:--:| ------------ | ------------ | ----------- | ----------- |:--:| ------------ | ----------- | ------------- |:--:| ------------- | ------------ | ----------- | ------------- |
| 🔵 Environment                  | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🔵 Parameter                    | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🔵 ExperimentPlanGenerator      | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🔵 ExperimentResultHandler      | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🔵 Measure                      | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🔵 ExperimentSimulatorHandler   | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🔵 Options                      | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| ══════════════════════════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
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
| ══════════════════════════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| 🟢 Simulation                   | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟢 MySimulator                  | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟢 ConcreteModifier             | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| 🟢 SimpleSimulationHandler      | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| ══════════════════════════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| ══════════════════════════════ | ══ | ══════════ | ══ | ════════════ | ════════════ | ══════════ | ══════════ | ══ | ════════════ | ══════════ | ════════════ | ══ | ════════════ | ════════════ | ══════════ | ════════════ |
| 🔴 FileManagement               | ║ |     1      | ║ |      1       |      1       |      1      |      1      | ║ |      1       |      1      |       1       | ║ |       1       |      1       |      1      |       1       |
| ****Σ present****                | ║ |     20     | ║ |      15      |      15      |     20      |     20      | ║ |      20      |     20      |      20       | ║ |      20       |      20      |     20      |      20       |
