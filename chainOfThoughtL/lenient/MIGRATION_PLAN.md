# Migration Plan: Java → Python (StructuredSimulationFramework)

## 1. Class Inventory

### Package: `ch.hevs.silab.structuredsim.experimenthandling`

| Java Class | Python Module | Role | Dependencies |
|---|---|---|---|
| `Parameter` | `experimenthandling/parameter.py` | Value object holding a key-value pair for simulation parameters | None |
| `Measure` | `experimenthandling/measure.py` | Value object holding key-value measurement results | None |
| `Options` | `experimenthandling/options.py` | Configuration container loaded from properties file | None |
| `Environment` | `experimenthandling/environment.py` | Simulation state at instant T: ID, parameters, probability | `Parameter` |
| `ExperimentPlanGenerator` | `experimenthandling/experiment_plan_generator.py` | Thread 1: generates tree of environments by applying modifiers | `Environment`, `Options`, `AModifier`, `FileManagement` |
| `ExperimentSimulatorHandler` | `experimenthandling/experiment_simulator_handler.py` | Thread 2: dequeues environments and runs simulator | `Environment`, `Options`, `ExperimentResultHandler`, `FileManagement` |
| `ExperimentResultHandler` | `experimenthandling/experiment_result_handler.py` | Thread 3: extracts measures from result files and writes measures files | `Measure`, `Options`, `FileManagement` |

### Package: `ch.hevs.silab.structuredsim.interfaces`

| Java Class | Python Module | Role | Dependencies |
|---|---|---|---|
| `IStartSimulation` | `interfaces/i_start_simulation.py` | Interface: `start_simulation(path)` | None |
| `IStopProgram` | `interfaces/i_stop_program.py` | Interface: `stop_program()` | None |
| `IManageParametersFile` | `interfaces/i_manage_parameters_file.py` | Interface: read/write parameters files | `Parameter` |
| `IExtractMeasures` | `interfaces/i_extract_measures.py` | Interface: `extract_measures(path)` | `Measure` |
| `IManageModifier` | `interfaces/i_manage_modifier.py` | Interface: `initiate_modifier_list()` | `AModifier` |
| `AModifier` | `interfaces/a_modifier.py` | Abstract class: applies algorithmic modification to an Environment | `Environment` |
| `ASimulationSystemHandler` | `interfaces/a_simulation_system_handler.py` | Abstract class implementing all 5 interfaces; base for glue code | All interfaces, `AModifier`, `Options` |
| `StartProgram` | `interfaces/start_program.py` | Concrete entry-point: loads config, bootstraps threads | All above |

### Package: `ch.hevs.silab.structuredsim.util`

| Java Class | Python Module | Role | Dependencies |
|---|---|---|---|
| `FileManagement` | `util/file_management.py` | File I/O utilities: copy/move/create folders, load properties, write measures | `Options`, `Environment`, `Measure` |

### Package: `ch.hevs.silab.structuredsim.gluecode`

| Java Class | Python Module | Role | Dependencies |
|---|---|---|---|
| `ConcreteModifier` | `gluecode/concrete_modifier.py` | Concrete modifier: applies +/-/×/÷ delta to a named parameter | `AModifier`, `Environment`, `Parameter` |
| `SimpleSimulationHandler` | `gluecode/simple_simulation_handler.py` | Concrete glue code: reads/writes param files, runs simulator, extracts measures | `ASimulationSystemHandler`, `AModifier`, `Parameter`, `Measure` |
| `MySimulator` | `gluecode/my_simulator.py` | Standalone mock simulator: reads params, computes val1×val2, writes result | None |
| `Simulation` | `gluecode/simulation.py` | Main entry point: wires up modifiers and launches StartProgram | `ConcreteModifier`, `SimpleSimulationHandler`, `StartProgram` |

---

## 2. Java Pattern → Python Equivalent

| Java Pattern | Python Equivalent | Justification |
|---|---|---|
| `abstract class` | `ABC` + `@abstractmethod` from `abc` module | Direct equivalent; enforces method implementation in subclasses |
| `interface` (single-method) | `ABC` with `@abstractmethod` | Python has no separate interface keyword; ABC is idiomatic |
| Multiple constructors | Single `__init__` with default `None` parameters + `@classmethod` factories where needed | Python does not support overloading; defaults cover all constructor variants |
| `implements` multiple interfaces | Multiple inheritance from ABC classes | Python supports multiple inheritance cleanly |
| `BlockingQueue<E>` / `PriorityBlockingQueue<E>` | `queue.Queue` / `queue.PriorityQueue` | Standard library equivalents with blocking `put`/`get` |
| `Thread` + `Runnable` | `threading.Thread` with `target` function or subclass | `threading` module is the direct equivalent |
| `Vector<E>` | `list` | Python list is thread-safe for append/read in CPython; `Vector` was Java's legacy synchronized list |
| `ArrayList<E>` / `List<E>` | `list` | Standard Python list |
| `Properties` file loading | `configparser.ConfigParser` | Built-in; reads `.properties`-style key=value files |
| `Calendar` (time cutoff arithmetic) | `datetime` + `timedelta` | Standard library; more ergonomic than Java Calendar |
| `System.currentTimeMillis()` | `time.time() * 1000` or `time.monotonic()` | Direct equivalent |
| Apache Log4j2 Logger | `logging` module | Standard Python logging; no external dependency required |
| `Comparable<T>` + `compareTo` | `__lt__` (or `functools.total_ordering`) | Python uses rich comparison methods; `PriorityQueue` uses `<` |
| `InputStream` | file path string or `io.IOBase` | Python opens files directly; InputStream is replaced by file-like objects |
| `BufferedReader` / `BufferedWriter` | `open()` with default buffering | Python's built-in file open already buffers |
| `Files.copy` / `Files.move` | `shutil.copy2` / `shutil.move` | `shutil` is the standard file-operations library |
| `new File(path).mkdir()` | `os.makedirs(path, exist_ok=True)` | `os.makedirs` creates all intermediate directories |
| `System.lineSeparator()` | `os.linesep` or `\n` in text mode | Python text-mode files handle line endings automatically |

---

## 3. Maven Dependencies → Python Replacements

| Maven Dependency | Python Replacement | Justification |
|---|---|---|
| `log4j-core` / `log4j-api` (Apache Log4j 2) | `logging` (stdlib) | Python's built-in logging covers all log4j use cases (levels, handlers, formatters) with no external package needed |
| Java standard library (`java.util`, `java.io`, `java.nio`) | Python stdlib (`os`, `io`, `shutil`, `pathlib`, `configparser`, `threading`, `queue`, `datetime`) | All Java stdlib functionality is covered by Python stdlib |

**No third-party Python packages are required.** The `requirements.txt` will be empty (or contain only stdlib notes).

---

## 4. Migration Order (most foundational first)

1. `Parameter` — leaf, no deps
2. `Measure` — leaf, no deps
3. `Options` — leaf, no deps
4. `Environment` — depends on `Parameter`
5. `IStartSimulation` — leaf interface
6. `IStopProgram` — leaf interface
7. `IManageParametersFile` — depends on `Parameter`
8. `IExtractMeasures` — depends on `Measure`
9. `AModifier` — depends on `Environment`, `Options`, `Parameter`
10. `IManageModifier` — depends on `AModifier`
11. `ASimulationSystemHandler` — depends on all interfaces + `AModifier`, `Options`
12. `FileManagement` — depends on `Options`, `Environment`, `Measure`
13. `ExperimentResultHandler` — depends on `FileManagement`, `Options`, `ASimulationSystemHandler`
14. `ExperimentPlanGenerator` — depends on `Environment`, `Options`, `AModifier`, `FileManagement`
15. `ExperimentSimulatorHandler` — depends on `Environment`, `Options`, `ExperimentResultHandler`, `ExperimentPlanGenerator`, `FileManagement`
16. `StartProgram` — depends on all experiment handling classes + `FileManagement`
17. `ConcreteModifier` — depends on `AModifier`, `Environment`, `Parameter`
18. `MySimulator` — standalone, no framework deps
19. `SimpleSimulationHandler` — depends on `ASimulationSystemHandler`, `Parameter`, `Measure`, `AModifier`
20. `Simulation` — top-level entry point, depends on everything
