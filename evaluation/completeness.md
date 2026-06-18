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
