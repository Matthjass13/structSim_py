In the "originalJavaCode" folder of the repository is the source code of a Java simulation framework (20 classes, Maven project). The framework is used to run structured simulations: it will read a parameter file and a configuration file as inputs and run algorithms, to produce output files with modified parameters. Migrate the entire project to Python. Put the output files in a "strict" folder to be created in the "chainofthought" folder.

Follow the steps I give you just after exactly in the order given. Do not begin Phase 2 until Phase 1 is fully complete and written to MIGRATION_PLAN.md. Do not skip, merge, or reorder any step.
1. Analysis & Planning:
·         List all classes, their package, their role, and their dependencies on other classes
·         For each Java pattern found (abstract classes, interfaces, multiple constructors, threading, etc.), identify the Python equivalent you will use
·         List all Maven dependencies and propose a Python replacement for each, with justification
·         Determine the migration order based on class dependencies (most foundational classes first)
·         Write the results of this analysis to chainOfThought/MIGRATION_PLAN.md
2. Migration:
·         Migrate each class in the order established in Phase 1
·         Preserve the complete class hierarchy and object-oriented architecture
·         Maintain all existing logic without adding or removing functionality
·         Follow Python naming conventions (snake_case for methods and variables, PascalCase for classes)
·         Apply the Python equivalents identified in Phase 1 consistently across all classes
·         Produce a requirements.txt in the output folder
· Write the current prompt in a readme file in the newly created folder "strict".
