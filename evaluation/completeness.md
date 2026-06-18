# Completeness — Java to Python Migration

**1** = class found in the migrated code | **0** = class absent

Columns abbreviated for readability:
- **CoT/perClass** = chainOfThought/perClass
- **CoT/lenient** = chainOfThought/lenient
- **CoT/strict** = chainOfThought/strict
- **CoT/riskFirst** = chainOfThought/riskFirst
- **ZS/negConst** = zeroShot/negativeConstraint
- **ZS/onlyTask** = zeroShot/onlyTask
- **ZS/persona** = zeroShot/persona
- **ZS/withCtx** = zeroShot/withContext
- **OS/aSimHdlr** = oneShot/aSimulationSystemHandler
- **OS/concMod** = oneShot/concreteModifier
- **OS/expPlanGen** = oneShot/experimentPlanGenerator
- **Transpiler** = transpiler

| Java Class                  | CoT/perClass | CoT/lenient | CoT/strict | CoT/riskFirst | ZS/negConst | ZS/onlyTask | ZS/persona | ZS/withCtx | OS/aSimHdlr | OS/concMod | OS/expPlanGen | Transpiler |
|-----------------------------|:------------:|:-----------:|:----------:|:-------------:|:-----------:|:-----------:|:----------:|:----------:|:-----------:|:----------:|:-------------:|:----------:|
| Environment                 | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| Parameter                   | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| ExperimentPlanGenerator     | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| ExperimentResultHandler     | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| Measure                     | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| ExperimentSimulatorHandler  | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| Options                     | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| ConcreteModifier            | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| AModifier                   | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| Simulation                  | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| MySimulator                 | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| SimpleSimulationHandler     | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| FileManagement              | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| ASimulationSystemHandler    | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| StartProgram                | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| IExtractMeasures            | 1            | 1           | 1          | 1             | 0           | 0           | 1          | 1          | 1           | 1          | 1             | 1          |
| IStopProgram                | 1            | 1           | 1          | 1             | 0           | 0           | 1          | 1          | 1           | 1          | 1             | 1          |
| IManageParametersFile       | 1            | 1           | 1          | 1             | 0           | 0           | 1          | 1          | 1           | 1          | 1             | 1          |
| IStartSimulation            | 1            | 1           | 1          | 1             | 0           | 0           | 1          | 1          | 1           | 1          | 1             | 1          |
| IManageModifier             | 1            | 1           | 1          | 1             | 0           | 0           | 1          | 1          | 1           | 1          | 1             | 1          |

---

## Lines of Code per Class

Total number of lines (including blank lines and comments) in each file. **N/A** = class absent from this migration.

| Java Class                  | Original (Java) | CoT/perClass | CoT/lenient | CoT/strict | CoT/riskFirst | ZS/negConst | ZS/onlyTask | ZS/persona | ZS/withCtx | OS/aSimHdlr | OS/concMod | OS/expPlanGen | Transpiler |
|-----------------------------|:---------------:|:------------:|:-----------:|:----------:|:-------------:|:-----------:|:-----------:|:----------:|:----------:|:-----------:|:----------:|:-------------:|:----------:|
| Environment                 | 171             | 108          | 62          | 79         | 74            | 63          | 59          | 79         | 73         | 81          | 71         | 64            | 174        |
| Parameter                   | 93              | 51           | 23          | 31         | 25            | 24          | 25          | 25         | 32         | 33          | 24         | 11            | 93         |
| ExperimentPlanGenerator     | 208             | 127          | 104         | 113        | 113           | 103         | 99          | 129        | 130        | 122         | 117        | 130           | 174        |
| ExperimentResultHandler     | 104             | 72           | 39          | 35         | 47            | 33          | 37          | 53         | 45         | 40          | 42         | 50            | 100        |
| Measure                     | 88              | 34           | 19          | 22         | 21            | 20          | 20          | 21         | 21         | 21          | 20         | 7             | 85         |
| ExperimentSimulatorHandler  | 114             | 86           | 55          | 61         | 62            | 50          | 50          | 74         | 63         | 66          | 67         | 75            | 102        |
| Options                     | 178             | 80           | 61          | 58         | 70            | 59          | 60          | 64         | 61         | 64          | 60         | 14            | 176        |
| ConcreteModifier            | 79              | 62           | 41          | 52         | 57            | 51          | 38          | 43         | 54         | 52          | 43         | 46            | 79         |
| AModifier                   | 100             | 61           | 23          | 24         | 31            | 24          | 24          | 29         | 29         | 43          | 25         | 26            | 106        |
| Simulation                  | 31              | 45           | 26          | 26         | 33            | 20          | 23          | 25         | 29         | 23          | 23         | 25            | 33         |
| MySimulator                 | 35              | 39           | 23          | 25         | 20            | 20          | 22          | 20         | 25         | 25          | 24         | 22            | 26         |
| SimpleSimulationHandler     | 139             | 101          | 79          | 106        | 113           | 68          | 68          | 86         | 92         | 92          | 86         | 78            | 116        |
| FileManagement              | 439             | 219          | 154         | 227        | 189           | 152         | 136         | 190        | 209        | 191         | 180        | 172           | 383        |
| ASimulationSystemHandler    | 76              | 50           | 24          | 61         | 39            | 44          | 44          | 36         | 30         | 60          | 25         | 31            | 79         |
| StartProgram                | 105             | 74           | 40          | 48         | 51            | 34          | 38          | 47         | 48         | 48          | 50         | 40            | 87         |
| IExtractMeasures            | 48              | 23           | 8           | 8          | 11            | N/A         | N/A         | 9          | 11         | 12          | 8          | 11            | 49         |
| IStopProgram                | 38              | 16           | 7           | 8          | 9             | N/A         | N/A         | 8          | 10         | 9           | 8          | 8             | 42         |
| IManageParametersFile       | 75              | 36           | 16          | 16         | 15            | N/A         | N/A         | 15         | 22         | 20          | 17         | 15            | 82         |
| IStartSimulation            | 39              | 16           | 7           | 8          | 9             | N/A         | N/A         | 8          | 10         | 9           | 8          | 8             | 41         |
| IManageModifier             | 41              | 24           | 8           | 8          | 10            | N/A         | N/A         | 9          | 11         | 10          | 8          | 12            | 43         |

---

## Number of Methods per Class

Count of method definitions (`def` in Python, method declarations in Java). **N/A** = class absent.

| Java Class                  | Original (Java) | CoT/perClass | CoT/lenient | CoT/strict | CoT/riskFirst | ZS/negConst | ZS/onlyTask | ZS/persona | ZS/withCtx | OS/aSimHdlr | OS/concMod | OS/expPlanGen | Transpiler |
|-----------------------------|:---------------:|:------------:|:-----------:|:----------:|:-------------:|:-----------:|:-----------:|:----------:|:----------:|:-----------:|:----------:|:-------------:|:----------:|
| Environment                 | 14              | 19           | 14          | 18         | 14            | 16          | 14          | 16         | 15         | 17          | 17         | 14            | 14         |
| Parameter                   | 7               | 9            | 6           | 7          | 6             | 6           | 6           | 7          | 8          | 9           | 7          | 2             | 7          |
| ExperimentPlanGenerator     | 5               | 5            | 5           | 5          | 5             | 5           | 5           | 5          | 5          | 5           | 5          | 5             | 5          |
| ExperimentResultHandler     | 2               | 2            | 2           | 2          | 2             | 2           | 2           | 2          | 2          | 2           | 2          | 2             | 2          |
| Measure                     | 6               | 6            | 6           | 7          | 6             | 6           | 6           | 6          | 6          | 6           | 6          | 2             | 6          |
| ExperimentSimulatorHandler  | 1               | 2            | 2           | 2          | 2             | 2           | 2           | 2          | 2          | 2           | 2          | 2             | 2          |
| Options                     | 17              | 17           | 17          | 17         | 17            | 17          | 17          | 17         | 17         | 17          | 17         | 1             | 17         |
| ConcreteModifier            | 6               | 4            | 4           | 3          | 3             | 4           | 3           | 3          | 5          | 4           | 5          | 3             | 6          |
| AModifier                   | 6               | 10           | 6           | 6          | 6             | 6           | 6           | 6          | 6          | 10          | 6          | 6             | 7          |
| Simulation                  | 1               | 0            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| MySimulator                 | 1               | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| SimpleSimulationHandler     | 9               | 7            | 7           | 7          | 7             | 7           | 7           | 8          | 7          | 8           | 8          | 7             | 9          |
| FileManagement              | 16              | 18           | 16          | 17         | 15            | 16          | 14          | 17         | 18         | 16          | 18         | 16            | 17         |
| ASimulationSystemHandler    | 4               | 5            | 5           | 11         | 5             | 11          | 11          | 5          | 5          | 9           | 5          | 5             | 4          |
| StartProgram                | 1               | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 1          |
| IExtractMeasures            | 1               | 1            | 1           | 1          | 1             | N/A         | N/A         | 1          | 1          | 1           | 1          | 1             | 1          |
| IStopProgram                | 1               | 1            | 1           | 1          | 1             | N/A         | N/A         | 1          | 1          | 1           | 1          | 1             | 1          |
| IManageParametersFile       | 3               | 3            | 2           | 2          | 2             | N/A         | N/A         | 3          | 2          | 3           | 3          | 2             | 3          |
| IStartSimulation            | 1               | 1            | 1           | 1          | 1             | N/A         | N/A         | 1          | 1          | 1           | 1          | 1             | 1          |
| IManageModifier             | 1               | 1            | 1           | 1          | 1             | N/A         | N/A         | 1          | 1          | 1           | 1          | 1             | 1          |

---

## Number of Class Attributes per Class

Count of instance attributes declared in `__init__` (Python) or as class-level fields (Java). **N/A** = class absent.

| Java Class                  | Original (Java) | CoT/perClass | CoT/lenient | CoT/strict | CoT/riskFirst | ZS/negConst | ZS/onlyTask | ZS/persona | ZS/withCtx | OS/aSimHdlr | OS/concMod | OS/expPlanGen | Transpiler |
|-----------------------------|:---------------:|:------------:|:-----------:|:----------:|:-------------:|:-----------:|:-----------:|:----------:|:----------:|:-----------:|:----------:|:-------------:|:----------:|
| Environment                 | 5               | 5            | 5           | 5          | 5             | 5           | 5           | 5          | 5          | 5           | 5          | 5             | 3          |
| Parameter                   | 2               | 2            | 2           | 2          | 2             | 2           | 2           | 2          | 2          | 2           | 2          | 2             | 2          |
| ExperimentPlanGenerator     | 9               | 6            | 7           | 9          | 7             | 9           | 7           | 7          | 8          | 7           | 7          | 9             | 5          |
| ExperimentResultHandler     | 5               | 4            | 4           | 4          | 4             | 4           | 4           | 4          | 4          | 4           | 4          | 4             | 4          |
| Measure                     | 2               | 2            | 2           | 2          | 2             | 2           | 2           | 2          | 2          | 2           | 2          | 2             | 2          |
| ExperimentSimulatorHandler  | 7               | 6            | 6           | 6          | 6             | 6           | 6           | 6          | 6          | 6           | 6          | 6             | 6          |
| Options                     | 8               | 8            | 8           | 8          | 8             | 8           | 8           | 8          | 8          | 8           | 8          | 8             | 0          |
| ConcreteModifier            | 1               | 3            | 3           | 3          | 3             | 3           | 3           | 3          | 4          | 3           | 3          | 3             | 4          |
| AModifier                   | 2               | 2            | 2           | 2          | 2             | 2           | 2           | 2          | 2          | 2           | 2          | 2             | 2          |
| Simulation                  | 0               | 0            | 0           | 0          | 0             | 0           | 0           | 0          | 0          | 0           | 0          | 0             | 0          |
| MySimulator                 | 0               | 0            | 0           | 0          | 0             | 0           | 0           | 0          | 0          | 0           | 0          | 0             | 0          |
| SimpleSimulationHandler     | 1               | 1            | 1           | 1          | 1             | 1           | 1           | 1          | 1          | 1           | 1          | 1             | 0          |
| FileManagement              | 4               | 4            | 4           | 4          | 4             | 4           | 4           | 2          | 4          | 4           | 4          | 4             | 0          |
| ASimulationSystemHandler    | 2               | 2            | 2           | 2          | 2             | 2           | 2           | 2          | 2          | 2           | 2          | 2             | 0          |
| StartProgram                | 0               | 0            | 0           | 0          | 0             | 0           | 0           | 0          | 0          | 0           | 0          | 0             | 0          |
| IExtractMeasures            | 0               | 0            | 0           | 0          | 0             | N/A         | N/A         | 0          | 0          | 0           | 0          | 0             | 0          |
| IStopProgram                | 0               | 0            | 0           | 0          | 0             | N/A         | N/A         | 0          | 0          | 0           | 0          | 0             | 0          |
| IManageParametersFile       | 0               | 0            | 0           | 0          | 0             | N/A         | N/A         | 0          | 0          | 0           | 0          | 0             | 0          |
| IStartSimulation            | 0               | 0            | 0           | 0          | 0             | N/A         | N/A         | 0          | 0          | 0           | 0          | 0             | 0          |
| IManageModifier             | 0               | 0            | 0           | 0          | 0             | N/A         | N/A         | 0          | 0          | 0           | 0          | 0             | 0          |

---

## Source Lines of Code per Class (excluding blank lines and comments)

**N/A** = class absent from this migration.

| Java Class                  | Original (Java) | CoT/perClass | CoT/lenient | CoT/strict | CoT/riskFirst | ZS/negConst | ZS/onlyTask | ZS/persona | ZS/withCtx | OS/aSimHdlr | OS/concMod | OS/expPlanGen | Transpiler |
|-----------------------------|:---------------:|:------------:|:-----------:|:----------:|:-------------:|:-----------:|:-----------:|:----------:|:----------:|:-----------:|:----------:|:-------------:|:----------:|
| Environment                 | 69              | 65           | 47          | 54         | 50            | 45          | 41          | 52         | 52         | 62          | 52         | 48            | 71         |
| Parameter                   | 29              | 25           | 18          | 20         | 19            | 18          | 18          | 18         | 24         | 24          | 17         | 10            | 30         |
| ExperimentPlanGenerator     | 114             | 74           | 77          | 81         | 77            | 77          | 73          | 84         | 97         | 95          | 89         | 95            | 93         |
| ExperimentResultHandler     | 39              | 42           | 34          | 29         | 34            | 27          | 30          | 34         | 35         | 33          | 35         | 40            | 28         |
| Measure                     | 25              | 15           | 14          | 16         | 15            | 14          | 14          | 15         | 15         | 15          | 14         | 6             | 24         |
| ExperimentSimulatorHandler  | 52              | 52           | 43          | 49         | 43            | 39          | 37          | 47         | 49         | 54          | 51         | 59            | 42         |
| Options                     | 62              | 45           | 43          | 42         | 44            | 42          | 42          | 44         | 43         | 45          | 42         | 12            | 62         |
| ConcreteModifier            | 62              | 35           | 34          | 39         | 42            | 42          | 32          | 32         | 45         | 44          | 36         | 39            | 57         |
| AModifier                   | 30              | 33           | 16          | 17         | 17            | 16          | 16          | 17         | 17         | 30          | 17         | 17            | 33         |
| Simulation                  | 19              | 18           | 16          | 15         | 19            | 13          | 15          | 13         | 20         | 16          | 16         | 16            | 21         |
| MySimulator                 | 29              | 18           | 20          | 19         | 17            | 16          | 18          | 13         | 21         | 21          | 20         | 17            | 20         |
| SimpleSimulationHandler     | 116             | 68           | 66          | 71         | 74            | 57          | 58          | 50         | 78         | 81          | 74         | 66            | 96         |
| FileManagement              | 265             | 140          | 124         | 149        | 124           | 124         | 112         | 130        | 154        | 162         | 151        | 140           | 207        |
| ASimulationSystemHandler    | 22              | 29           | 18          | 42         | 25            | 31          | 31          | 24         | 18         | 40          | 18         | 23            | 22         |
| StartProgram                | 39              | 32           | 24          | 30         | 31            | 24          | 25          | 29         | 29         | 31          | 36         | 28            | 33         |
| IExtractMeasures            | 6               | 9            | 6           | 6          | 8             | N/A         | N/A         | 6          | 8          | 8           | 5          | 7             | 9          |
| IStopProgram                | 4               | 6            | 5           | 6          | 6             | N/A         | N/A         | 5          | 7          | 6           | 5          | 5             | 7          |
| IManageParametersFile       | 9               | 17           | 9           | 9          | 11            | N/A         | N/A         | 10         | 10         | 14          | 12         | 10            | 18         |
| IStartSimulation            | 4               | 6            | 5           | 6          | 6             | N/A         | N/A         | 5          | 7          | 6           | 5          | 5             | 7          |
| IManageModifier             | 5               | 10           | 6           | 6          | 7             | N/A         | N/A         | 6          | 8          | 7           | 5          | 8             | 8          |
