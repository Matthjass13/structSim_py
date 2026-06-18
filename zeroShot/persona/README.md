# Persona Migration

## Prompt

You are a senior software architect specializing in Java-to-Python migrations. In the "originalJavaCode" folder of the repository is the source code of a framework. Migrate it to Python in a "persona" folder to be created in the "zeroShot" folder. Add a readme in the created folder with the current prompt written in it.

## Overview

This folder contains a Python migration of the StructuredSimulationFramework originally written in Java (located in `originalJavaCode/`). The migration was performed by a senior software architect with the following design decisions:

- Java interfaces → Python abstract base classes (`abc.ABC`) with `@abstractmethod`
- Java `Vector` → Python `list` (thread-safe access managed at the queue level)
- Java `BlockingQueue` → Python `queue.PriorityQueue` / `queue.Queue`
- Java `Calendar` time arithmetic → Python `datetime.timedelta`
- Java `Properties` files → Python `configparser`-style `.properties` parsing
- Java threads (`Runnable` + `Thread`) → Python `threading.Thread`
- Getters/setters replaced with Python properties where idiomatic, kept as explicit methods where matching the original API contract matters
- Logging via Python `logging` module (replaces Log4j)
- Snake_case naming throughout (PEP 8)

## Structure

```
persona/
├── experimenthandling/
│   ├── parameter.py          # Parameter data class
│   ├── measure.py            # Measure data class
│   ├── environment.py        # Environment (simulation state)
│   ├── options.py            # Configuration options
│   ├── experiment_plan_generator.py   # Thread 1: plan generation
│   ├── experiment_simulator_handler.py # Thread 2: simulation execution
│   └── experiment_result_handler.py   # Thread 3: result processing
├── interfaces/
│   ├── i_start_simulation.py
│   ├── i_stop_program.py
│   ├── i_manage_parameters_file.py
│   ├── i_extract_measures.py
│   ├── i_manage_modifier.py
│   ├── a_modifier.py
│   ├── a_simulation_system_handler.py
│   └── start_program.py
├── util/
│   └── file_management.py
├── gluecode/
│   ├── concrete_modifier.py
│   ├── my_simulator.py
│   ├── simple_simulation_handler.py
│   └── simulation.py
└── README.md
```
