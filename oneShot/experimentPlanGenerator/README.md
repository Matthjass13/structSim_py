In the "originalJavaCode" folder of the repository is the source code of a Java simulation framework (20 classes, Maven project). The framework is used to run structured simulations: it will read a parameter file and a configuration file as inputs and run algorithms, to produce output files with modified parameters. Migrate the entire project to Python and put the output files in a "experimentPlanGenerator" folder to be created in the "oneshot" folder. In this created folder, also put the current prompt in a readme file. The migration must:
•	Preserve the complete class hierarchy and object-oriented architecture
•	Maintain all existing logic without adding or removing functionality
•	Use appropriate Python libraries and modern Python idioms
•	Follow Python naming conventions (snake_case for methods and variables, PascalCase for classes)
•	Produce a requirements.txt in the output folder
Use the following migration as a reference and follow the same patterns. The original Java file is at originalJavaCode/experimenthandling/ExperimentPlanGenerator.java. Its Python migration is provided below, enclosed in triple double quotes:
[... reference migration code for ExperimentPlanGenerator ...]
