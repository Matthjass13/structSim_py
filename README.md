# structSim_py

## Project Description

This repository was used in the context of the bachelor thesis "MAIgration : How can generative AI support developpers in software migration projects ?", done in 2026 by Matthias Gaillard. In this project, a framework of the SiLab group made in Java (https://github.com/SiLab-group/structSim/tree/master) was studied and migrated in Python in multiple attempts using generative AI. Every code is in this repository.

## Project Structure

The repository consists of 7 folders :
- **originalJavaCode** : the original source code of the framework, including unit and integration tests made specifically for this thesis
- **tests** : migrated Python tests from the Java tests
- **zeroShot** : migrated code of 4 migrations using zero-shot prompts
- **oneShot** : migrated code of 3 migrations using one-shot prompts
- **chainOfThought** : migrated code of 4 migrations using chain-of-thought prompts
- **transpiler** : migrated code of a migration using the JavaToPython transpiler (https://github.com/natural/java2python)
- **evaluation** : information about the completeness, correctness and quality of all migrations. Metrics used :
  - Completeness : Number of classes, methods and attributes,
  - Correctness : Proportion of passing unit and integration tests and effort needed to make failing tests pass
  - Quality : Number of lines of code, pyling score, pyright error count, cyclomatic complexity

## Contributors

- Matthias Gaillard
- Claude Code
