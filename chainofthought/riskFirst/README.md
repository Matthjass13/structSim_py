# Original Prompt

In the "originalJavaCode" folder of the repository is the source code of a Java simulation framework (20 classes, Maven project). The framework is used to run structured simulations: it will read a parameter file and a configuration file as inputs and run algorithms, to produce output files with modified parameters. Migrate the entire project to Python. Put the output files in a "riskFirst" folder to be created in the "chainofthought" folder.

Proceed in three steps:
1. Risk Analysis: Identify the 3 to 5 hardest migration challenges in this codebase. For each challenge, write an explicit translation strategy.
2. Migration: Migrate all classes, applying the strategies defined in step 1 consistently. Use the dependency order (foundational classes first).
3. Produce a requirements.txt and a STRATEGY.md, in "riskFirst" folder, summarizing the challenges identified and the strategies applied.
4. Write the current prompt in a readme.md file, also in the "riskFirst" folder
