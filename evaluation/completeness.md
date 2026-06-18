# Completeness — Java to Python Migration

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

## Is the class there or not

**1** = class found in the migrated code | **0** = class absent

| Java Class                 | CoT/perClass | CoT/lenient | CoT/strict | CoT/riskFirst | ZS/negConst | ZS/onlyTask | ZS/persona | ZS/withCtx | OS/aSimHdlr | OS/concMod | OS/expPlanGen | Transpiler |
| -------------------------- | :----------: | :---------: | :--------: | :-----------: | :---------: | :---------: | :--------: | :--------: | :---------: | :--------: | :-----------: | :--------: |
| Environment                |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| Parameter                  |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| ExperimentPlanGenerator    |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| ExperimentResultHandler    |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| Measure                    |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| ExperimentSimulatorHandler |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| Options                    |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| ConcreteModifier           |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| AModifier                  |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| Simulation                 |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| MySimulator                |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| SimpleSimulationHandler    |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| FileManagement             |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| ASimulationSystemHandler   |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| StartProgram               |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| IExtractMeasures           |      1       |      1      |     1      |       1       |      0      |      0      |     1      |     1      |      1      |     1      |       1       |     1      |
| IStopProgram               |      1       |      1      |     1      |       1       |      0      |      0      |     1      |     1      |      1      |     1      |       1       |     1      |
| IManageParametersFile      |      1       |      1      |     1      |       1       |      0      |      0      |     1      |     1      |      1      |     1      |       1       |     1      |
| IStartSimulation           |      1       |      1      |     1      |       1       |      0      |      0      |     1      |     1      |      1      |     1      |       1       |     1      |
| IManageModifier            |      1       |      1      |     1      |       1       |      0      |      0      |     1      |     1      |      1      |     1      |       1       |     1      |

---

## Number of Methods per Class

Count of method definitions (`def` in Python, method declarations in Java). **N/A** = class absent.

| Java Class                 | Original (Java) | CoT/perClass | CoT/lenient | CoT/strict | CoT/riskFirst | ZS/negConst | ZS/onlyTask | ZS/persona | ZS/withCtx | OS/aSimHdlr | OS/concMod | OS/expPlanGen | Transpiler |
| -------------------------- | :-------------: | :----------: | :---------: | :--------: | :-----------: | :---------: | :---------: | :--------: | :--------: | :---------: | :--------: | :-----------: | :--------: |
| Environment                |       14        |      19      |     14      |     18     |      14       |     16      |     14      |     16     |     15     |     17      |     17     |      14       |     14     |
| Parameter                  |        7        |      9       |      6      |     7      |       6       |      6      |      6      |     7      |     8      |      9      |     7      |       2       |     7      |
| ExperimentPlanGenerator    |        5        |      5       |      5      |     5      |       5       |      5      |      5      |     5      |     5      |      5      |     5      |       5       |     5      |
| ExperimentResultHandler    |        2        |      2       |      2      |     2      |       2       |      2      |      2      |     2      |     2      |      2      |     2      |       2       |     2      |
| Measure                    |        6        |      6       |      6      |     7      |       6       |      6      |      6      |     6      |     6      |      6      |     6      |       2       |     6      |
| ExperimentSimulatorHandler |        1        |      2       |      2      |     2      |       2       |      2      |      2      |     2      |     2      |      2      |     2      |       2       |     2      |
| Options                    |       17        |      17      |     17      |     17     |      17       |     17      |     17      |     17     |     17     |     17      |     17     |       1       |     17     |
| ConcreteModifier           |        6        |      4       |      4      |     3      |       3       |      4      |      3      |     3      |     5      |      4      |     5      |       3       |     6      |
| AModifier                  |        6        |      10      |      6      |     6      |       6       |      6      |      6      |     6      |     6      |     10      |     6      |       6       |     7      |
| Simulation                 |        1        |      0       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| MySimulator                |        1        |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| SimpleSimulationHandler    |        9        |      7       |      7      |     7      |       7       |      7      |      7      |     8      |     7      |      8      |     8      |       7       |     9      |
| FileManagement             |       16        |      18      |     16      |     17     |      15       |     16      |     14      |     17     |     18     |     16      |     18     |      16       |     17     |
| ASimulationSystemHandler   |        4        |      5       |      5      |     11     |       5       |     11      |     11      |     5      |     5      |      9      |     5      |       5       |     4      |
| StartProgram               |        1        |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     1      |
| IExtractMeasures           |        1        |      1       |      1      |     1      |       1       |     N/A     |     N/A     |     1      |     1      |      1      |     1      |       1       |     1      |
| IStopProgram               |        1        |      1       |      1      |     1      |       1       |     N/A     |     N/A     |     1      |     1      |      1      |     1      |       1       |     1      |
| IManageParametersFile      |        3        |      3       |      2      |     2      |       2       |     N/A     |     N/A     |     3      |     2      |      3      |     3      |       2       |     3      |
| IStartSimulation           |        1        |      1       |      1      |     1      |       1       |     N/A     |     N/A     |     1      |     1      |      1      |     1      |       1       |     1      |
| IManageModifier            |        1        |      1       |      1      |     1      |       1       |     N/A     |     N/A     |     1      |     1      |      1      |     1      |       1       |     1      |

---

## Number of Class Attributes per Class

Count of instance attributes declared in `__init__` (Python) or as class-level fields (Java). **N/A** = class absent.

| Java Class                 | Original (Java) | CoT/perClass | CoT/lenient | CoT/strict | CoT/riskFirst | ZS/negConst | ZS/onlyTask | ZS/persona | ZS/withCtx | OS/aSimHdlr | OS/concMod | OS/expPlanGen | Transpiler |
| -------------------------- | :-------------: | :----------: | :---------: | :--------: | :-----------: | :---------: | :---------: | :--------: | :--------: | :---------: | :--------: | :-----------: | :--------: |
| Environment                |        5        |      5       |      5      |     5      |       5       |      5      |      5      |     5      |     5      |      5      |     5      |       5       |     3      |
| Parameter                  |        2        |      2       |      2      |     2      |       2       |      2      |      2      |     2      |     2      |      2      |     2      |       2       |     2      |
| ExperimentPlanGenerator    |        9        |      6       |      7      |     9      |       7       |      9      |      7      |     7      |     8      |      7      |     7      |       9       |     5      |
| ExperimentResultHandler    |        5        |      4       |      4      |     4      |       4       |      4      |      4      |     4      |     4      |      4      |     4      |       4       |     4      |
| Measure                    |        2        |      2       |      2      |     2      |       2       |      2      |      2      |     2      |     2      |      2      |     2      |       2       |     2      |
| ExperimentSimulatorHandler |        7        |      6       |      6      |     6      |       6       |      6      |      6      |     6      |     6      |      6      |     6      |       6       |     6      |
| Options                    |        8        |      8       |      8      |     8      |       8       |      8      |      8      |     8      |     8      |      8      |     8      |       8       |     0      |
| ConcreteModifier           |        1        |      3       |      3      |     3      |       3       |      3      |      3      |     3      |     4      |      3      |     3      |       3       |     4      |
| AModifier                  |        2        |      2       |      2      |     2      |       2       |      2      |      2      |     2      |     2      |      2      |     2      |       2       |     2      |
| Simulation                 |        0        |      0       |      0      |     0      |       0       |      0      |      0      |     0      |     0      |      0      |     0      |       0       |     0      |
| MySimulator                |        0        |      0       |      0      |     0      |       0       |      0      |      0      |     0      |     0      |      0      |     0      |       0       |     0      |
| SimpleSimulationHandler    |        1        |      1       |      1      |     1      |       1       |      1      |      1      |     1      |     1      |      1      |     1      |       1       |     0      |
| FileManagement             |        4        |      4       |      4      |     4      |       4       |      4      |      4      |     2      |     4      |      4      |     4      |       4       |     0      |
| ASimulationSystemHandler   |        2        |      2       |      2      |     2      |       2       |      2      |      2      |     2      |     2      |      2      |     2      |       2       |     0      |
| StartProgram               |        0        |      0       |      0      |     0      |       0       |      0      |      0      |     0      |     0      |      0      |     0      |       0       |     0      |
| IExtractMeasures           |        0        |      0       |      0      |     0      |       0       |     N/A     |     N/A     |     0      |     0      |      0      |     0      |       0       |     0      |
| IStopProgram               |        0        |      0       |      0      |     0      |       0       |     N/A     |     N/A     |     0      |     0      |      0      |     0      |       0       |     0      |
| IManageParametersFile      |        0        |      0       |      0      |     0      |       0       |     N/A     |     N/A     |     0      |     0      |      0      |     0      |       0       |     0      |
| IStartSimulation           |        0        |      0       |      0      |     0      |       0       |     N/A     |     N/A     |     0      |     0      |      0      |     0      |       0       |     0      |
| IManageModifier            |        0        |      0       |      0      |     0      |       0       |     N/A     |     N/A     |     0      |     0      |      0      |     0      |       0       |     0      |

---
