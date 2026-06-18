# Original prompt

In the "originalJavaCode" folder of the repository is the source code of a Java simulation framework (20 classes, Maven project). The framework is used to run structured simulations: it will read a parameter file and a configuration file as inputs and run algorithms, to produce output files with modified parameters. Migrate the entire project to Python. Put the output files in a "perClass" folder to be created in the "chainofthought" folder. 

For each class, in dependency order (most foundational first), follow this reasoning sequence before writing the code:
1. List the Java-specific constructs present in this class (abstract methods, threading, collections, etc.)
2. State the Python equivalent you will use for each, with justification
3. Identify any risk or deviation from a literal translation
4. Write the migrated Python file
Repeat this sequence for every class. Produce a requirements.txt when done. Write the current prompt in a readme file in the "perClass" folder.
