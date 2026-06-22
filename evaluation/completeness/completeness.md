# Completeness metrics — Java to Python Migration

**Package legend:** 🔵 experimenthandling · 🟣 interfaces · 🟢 gluecode · 🔴 util
**Column groups:** Java = original Java source · Trans = auto-transpiler · ZS = Zero-Shot · OS = One-Shot · CoT = Chain-of-Thought
**Abbreviations:** ZS/NC = negativeConstraint · ZS/OT = onlyTask · ZS/Pe = persona · ZS/Ctx = withContext · OS/AS = aSimulationSystemHandler · OS/CM = concreteModifier · OS/EP = experimentPlanGenerator · CoT/PC = perClass · CoT/Le = lenient · CoT/St = strict · CoT/RF = riskFirst

## Class Presence (1 = present, 0 = absent)

Whether each class was found in the migrated Python code.

| Class |  ║ | Trans |  ║ | ZS/NC | ZS/OT | ZS/Pe | ZS/Ctx |  ║ | OS/AS | OS/CM | OS/EP |  ║ | CoT/PC | CoT/Le | CoT/St | CoT/RF |
| ------------------------------ | :-: | ----- | :-: | ----- | ----- | ----- | ------ | :-: | ----- | ----- | ----- | :-: | ------ | ------ | ------ | ------ |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| 🔵 Environment |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🔵 Parameter |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🔵 ExperimentPlanGenerator |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🔵 ExperimentResultHandler |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🔵 Measure |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🔵 ExperimentSimulatorHandler |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🔵 Options |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| 🟣 AModifier |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟣 ASimulationSystemHandler |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟣 StartProgram |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟣 IExtractMeasures |  ║ | 1 |  ║ | 0 | 0 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟣 IStopProgram |  ║ | 1 |  ║ | 0 | 0 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟣 IManageParametersFile |  ║ | 1 |  ║ | 0 | 0 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟣 IStartSimulation |  ║ | 1 |  ║ | 0 | 0 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟣 IManageModifier |  ║ | 1 |  ║ | 0 | 0 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| 🟢 Simulation |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟢 MySimulator |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟢 ConcreteModifier |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟢 SimpleSimulationHandler |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| 🔴 FileManagement |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| \***\*Σ present\*\*** |  ║ | 20 |  ║ | 15 | 15 | 20 | 20 |  ║ | 20 | 20 | 20 |  ║ | 20 | 20 | 20 | 20 |

---

## Number of Methods

Count of method definitions (`def` in Python, method declarations in Java).

| Class |  ║ | Java Orig |  ║ | Trans |  ║ | ZS/NC | ZS/OT | ZS/Pe | ZS/Ctx |  ║ | OS/AS | OS/CM | OS/EP |  ║ | CoT/PC | CoT/Le | CoT/St | CoT/RF |
| ------------------------------ | :-: | ---------- | :-: | ----- | :-: | ----- | ----- | ----- | ------ | :-: | ----- | ----- | ----- | :-: | ------ | ------ | ------ | ------ |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| 🔵 Environment |  ║ | 14 |  ║ | 14 |  ║ | 16 | 14 | 16 | 15 |  ║ | 17 | 17 | 14 |  ║ | 19 | 14 | 18 | 14 |
| 🔵 Parameter |  ║ | 7 |  ║ | 7 |  ║ | 6 | 6 | 7 | 8 |  ║ | 9 | 7 | 2 |  ║ | 9 | 6 | 7 | 6 |
| 🔵 ExperimentPlanGenerator |  ║ | 5 |  ║ | 5 |  ║ | 5 | 5 | 5 | 5 |  ║ | 5 | 5 | 5 |  ║ | 5 | 5 | 5 | 5 |
| 🔵 ExperimentResultHandler |  ║ | 2 |  ║ | 2 |  ║ | 2 | 2 | 2 | 2 |  ║ | 2 | 2 | 2 |  ║ | 2 | 2 | 2 | 2 |
| 🔵 Measure |  ║ | 6 |  ║ | 6 |  ║ | 6 | 6 | 6 | 6 |  ║ | 6 | 6 | 2 |  ║ | 6 | 6 | 7 | 6 |
| 🔵 ExperimentSimulatorHandler |  ║ | 1 |  ║ | 2 |  ║ | 2 | 2 | 2 | 2 |  ║ | 2 | 2 | 2 |  ║ | 2 | 2 | 2 | 2 |
| 🔵 Options |  ║ | 17 |  ║ | 17 |  ║ | 17 | 17 | 17 | 17 |  ║ | 17 | 17 | 1 |  ║ | 17 | 17 | 17 | 17 |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| 🟣 AModifier |  ║ | 6 |  ║ | 7 |  ║ | 6 | 6 | 6 | 6 |  ║ | 10 | 6 | 6 |  ║ | 10 | 6 | 6 | 6 |
| 🟣 ASimulationSystemHandler |  ║ | 4 |  ║ | 4 |  ║ | 11 | 11 | 5 | 5 |  ║ | 9 | 5 | 5 |  ║ | 5 | 5 | 11 | 5 |
| 🟣 StartProgram |  ║ | 1 |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟣 IExtractMeasures |  ║ | 1 |  ║ | 1 |  ║ | N/A | N/A | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟣 IStopProgram |  ║ | 1 |  ║ | 1 |  ║ | N/A | N/A | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟣 IManageParametersFile |  ║ | 3 |  ║ | 3 |  ║ | N/A | N/A | 3 | 2 |  ║ | 3 | 3 | 2 |  ║ | 3 | 2 | 2 | 2 |
| 🟣 IStartSimulation |  ║ | 1 |  ║ | 1 |  ║ | N/A | N/A | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟣 IManageModifier |  ║ | 1 |  ║ | 1 |  ║ | N/A | N/A | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| 🟢 Simulation |  ║ | 1 |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 0 | 1 | 1 | 1 |
| 🟢 MySimulator |  ║ | 1 |  ║ | 1 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| 🟢 ConcreteModifier |  ║ | 6 |  ║ | 6 |  ║ | 4 | 3 | 3 | 5 |  ║ | 4 | 5 | 3 |  ║ | 4 | 4 | 3 | 3 |
| 🟢 SimpleSimulationHandler |  ║ | 9 |  ║ | 9 |  ║ | 7 | 7 | 8 | 7 |  ║ | 8 | 8 | 7 |  ║ | 7 | 7 | 7 | 7 |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| 🔴 FileManagement |  ║ | 16 |  ║ | 17 |  ║ | 16 | 14 | 17 | 18 |  ║ | 16 | 18 | 16 |  ║ | 18 | 16 | 17 | 15 |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| \***\*Σ\*\*** |  ║ | 103 |  ║ | 106 |  ║ | 101 | 96 | 104 | 105 |  ║ | 115 | 108 | 74 |  ║ | 113 | 99 | 111 | 97 |

### Analysis

**Systematic over-count vs. Java (+1 for `__init__`)** — The Java count reflects declared methods only. All Python migrations count `__init__` as a method, which has no direct Java counterpart (Java uses constructors, which are not counted by the same regex). This explains why `ExperimentSimulatorHandler` consistently shows 2 in every migration against a Java count of 1: the original has a single `run()` method, and every Python version adds `__init__`.

**`ASimulationSystemHandler` — ZS/negConst and ZS/onlyTask show 11 methods (vs. Java 4)** — Java `ASimulationSystemHandler` is an abstract class that extends 5 interfaces but does not re-declare their abstract methods in its own body (Java enforces contracts at compile time, not at source level). The two zero-shot migrations (`negativeConstraint` and `onlyTask`) explicitly re-declared all 5 or 6 inherited abstract methods (`start_simulation`, `stop_program`, `read_parameters_file`, `write_parameters_file`, `extract_measures`, `initiate_modifier_list`) alongside the 4 concrete ones from the original, producing 10–11 `def` statements. The other migrations (including `CoT/strict`) have the same behaviour for `CoT/strict=11`, confirming this is a recurring pattern when the model tries to be exhaustive about ABC stubs.

**`OS/expPlanGen` — systematically low across `Parameter` (2), `Measure` (2), `Options` (1)** — The `experimentPlanGenerator` one-shot example used in the prompt focused on the `ExperimentPlanGenerator` class itself. The model adopted a minimalist Pythonic style for the remaining classes: it collapsed all getters and setters into plain attribute access, leaving only `__init__` (and `__str__` for `Parameter` and `Measure`). `Options` ends up with a single method — `__init__` — instead of 17.

**`AModifier` — OS/aSimHdlr=10 and CoT/perClass=10 (vs. Java 6)** — These two migrations also re-declare the abstract interface methods in the abstract class body, similar to `ASimulationSystemHandler` above.

**`Simulation` — CoT/perClass=0** — The class is present (presence = 1) but defined as `class Simulation(StartProgram): pass` with no body. The model delegated all behaviour to the parent class and generated no `def` statement of its own, matching its role in the design (a thin concrete subclass), but losing the single `start()` method from the Java original.

**`ConcreteModifier` — all migrations below Java (3–5 vs. 6)** — Java counts 6 methods; Python versions count 3–5. The discrepancy comes from getters and setters: Java declares explicit `getKey()`, `setKey()`, `getOperator()`, `setOperator()`, `getDelta()`, `setDelta()` (6 methods + constructor). Python migrations use direct attribute access and keep only `__init__`, `modify()`, and sometimes a `__str__` or `__repr__`.

---

## Number of Class Attributes

Instance attributes in `__init__` (Python) or class-level fields (Java). N/A = class absent.

| Class |  ║ | Java Orig |  ║ | Trans |  ║ | ZS/NC | ZS/OT | ZS/Pe | ZS/Ctx |  ║ | OS/AS | OS/CM | OS/EP |  ║ | CoT/PC | CoT/Le | CoT/St | CoT/RF |
| ------------------------------ | :-: | ---------- | :-: | ----- | :-: | ----- | ----- | ----- | ------ | :-: | ----- | ----- | ----- | :-: | ------ | ------ | ------ | ------ |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| 🔵 Environment |  ║ | 5 |  ║ | 3 |  ║ | 5 | 5 | 5 | 5 |  ║ | 5 | 5 | 5 |  ║ | 5 | 5 | 5 | 5 |
| 🔵 Parameter |  ║ | 2 |  ║ | 2 |  ║ | 2 | 2 | 2 | 2 |  ║ | 2 | 2 | 2 |  ║ | 2 | 2 | 2 | 2 |
| 🔵 ExperimentPlanGenerator |  ║ | 9 |  ║ | 5 |  ║ | 9 | 7 | 7 | 8 |  ║ | 7 | 7 | 9 |  ║ | 6 | 7 | 9 | 7 |
| 🔵 ExperimentResultHandler |  ║ | 5 |  ║ | 4 |  ║ | 4 | 4 | 4 | 4 |  ║ | 4 | 4 | 4 |  ║ | 4 | 4 | 4 | 4 |
| 🔵 Measure |  ║ | 2 |  ║ | 2 |  ║ | 2 | 2 | 2 | 2 |  ║ | 2 | 2 | 2 |  ║ | 2 | 2 | 2 | 2 |
| 🔵 ExperimentSimulatorHandler |  ║ | 7 |  ║ | 6 |  ║ | 6 | 6 | 6 | 6 |  ║ | 6 | 6 | 6 |  ║ | 6 | 6 | 6 | 6 |
| 🔵 Options |  ║ | 8 |  ║ | 0 |  ║ | 8 | 8 | 8 | 8 |  ║ | 8 | 8 | 8 |  ║ | 8 | 8 | 8 | 8 |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| 🟣 AModifier |  ║ | 2 |  ║ | 2 |  ║ | 2 | 2 | 2 | 2 |  ║ | 2 | 2 | 2 |  ║ | 2 | 2 | 2 | 2 |
| 🟣 ASimulationSystemHandler |  ║ | 2 |  ║ | 0 |  ║ | 2 | 2 | 2 | 2 |  ║ | 2 | 2 | 2 |  ║ | 2 | 2 | 2 | 2 |
| 🟣 StartProgram |  ║ | 0 |  ║ | 0 |  ║ | 0 | 0 | 0 | 0 |  ║ | 0 | 0 | 0 |  ║ | 0 | 0 | 0 | 0 |
| 🟣 IExtractMeasures |  ║ | 0 |  ║ | 0 |  ║ | N/A | N/A | 0 | 0 |  ║ | 0 | 0 | 0 |  ║ | 0 | 0 | 0 | 0 |
| 🟣 IStopProgram |  ║ | 0 |  ║ | 0 |  ║ | N/A | N/A | 0 | 0 |  ║ | 0 | 0 | 0 |  ║ | 0 | 0 | 0 | 0 |
| 🟣 IManageParametersFile |  ║ | 0 |  ║ | 0 |  ║ | N/A | N/A | 0 | 0 |  ║ | 0 | 0 | 0 |  ║ | 0 | 0 | 0 | 0 |
| 🟣 IStartSimulation |  ║ | 0 |  ║ | 0 |  ║ | N/A | N/A | 0 | 0 |  ║ | 0 | 0 | 0 |  ║ | 0 | 0 | 0 | 0 |
| 🟣 IManageModifier |  ║ | 0 |  ║ | 0 |  ║ | N/A | N/A | 0 | 0 |  ║ | 0 | 0 | 0 |  ║ | 0 | 0 | 0 | 0 |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| 🟢 Simulation |  ║ | 0 |  ║ | 0 |  ║ | 0 | 0 | 0 | 0 |  ║ | 0 | 0 | 0 |  ║ | 0 | 0 | 0 | 0 |
| 🟢 MySimulator |  ║ | 0 |  ║ | 0 |  ║ | 0 | 0 | 0 | 0 |  ║ | 0 | 0 | 0 |  ║ | 0 | 0 | 0 | 0 |
| 🟢 ConcreteModifier |  ║ | 1 |  ║ | 4 |  ║ | 3 | 3 | 3 | 4 |  ║ | 3 | 3 | 3 |  ║ | 3 | 3 | 3 | 3 |
| 🟢 SimpleSimulationHandler |  ║ | 1 |  ║ | 0 |  ║ | 1 | 1 | 1 | 1 |  ║ | 1 | 1 | 1 |  ║ | 1 | 1 | 1 | 1 |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| 🔴 FileManagement |  ║ | 4 |  ║ | 0 |  ║ | 4 | 4 | 2 | 4 |  ║ | 4 | 4 | 4 |  ║ | 4 | 4 | 4 | 4 |
| ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ | ══ |
| \***\*Σ\*\*** |  ║ | 48 |  ║ | 28 |  ║ | 48 | 46 | 44 | 48 |  ║ | 46 | 46 | 48 |  ║ | 45 | 46 | 48 | 46 |

### Analysis

**Transpiler systematically under-counts (total 28 vs. Java 48)** — The transpiler declares attributes at *class level* rather than inside `__init__`, e.g. `pathParameters = str()` instead of `self.pathParameters = ""`. The metric counts only `self.attr` assignments in `__init__`, so these class-level stubs register as 0. This affects `Options` (0 vs. 8), `ASimulationSystemHandler` (0 vs. 2), `SimpleSimulationHandler` (0 vs. 1), `FileManagement` (0 vs. 4), `Environment` (3 vs. 5), and `ExperimentPlanGenerator` (5 vs. 9).

**`ExperimentResultHandler` — all migrations show 4 (vs. Java 5)** — The fifth Java field is `logger`, a `static` logger instance (`private static final Logger`). Python migrations replace it with a module-level variable (`logging.getLogger(__name__)`) outside the class, so it never appears in `__init__` and is not counted as an instance attribute. This is a consistent and correct Pythonic translation.

**`ExperimentSimulatorHandler` — all migrations show 6 (vs. Java 7)** — Similar to the logger case: Java declares a `logger` field on the class, while Python puts the logger at module level.

**`ConcreteModifier` — all migrations show 3–4 (vs. Java 1)** — This is the inverse surprise. Java declares only 1 field directly in `ConcreteModifier` (`keyToChange`; `operator` and `delta` are inherited from `AModifier` in Java source). Python migrations explicitly re-declare all three (`self.key_to_change`, `self.operator`, `self.delta`) in `ConcreteModifier.__init__` because Python's `super().__init__()` usage is less strict and models tend to list all attributes explicitly. This inflates the count to 3 (or 4 when an extra attribute is added).

**`ExperimentPlanGenerator` — Transpiler=5 (vs. Java 9, others 6–9)** — The transpiler generated only 5 `self.` assignments in `__init__`, omitting 4 of the 9 Java fields. The missing fields are typically those initialised via method calls (`new LinkedList<>()`, complex constructors) that the transpiler left as class-level stubs.

**`FileManagement` — ZS/persona=2 (vs. Java 4, others 4)** — The `persona` migration assigns only `self.options` and `self.filename` in `__init__`, computing `path_result` and `path_simulator` dynamically inside individual methods rather than storing them as attributes.

**`Options` — Transpiler=0 (vs. Java 8, all others 8)** — See transpiler note above; most extreme case because `Options` is a pure data-holder with 8 fields, all declared as class-level type annotations by the transpiler.

