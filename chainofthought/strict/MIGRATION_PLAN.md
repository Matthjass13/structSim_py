# Migration Plan: Java → Python

## 1. All Classes, Packages, Roles, and Dependencies

| Class | Package | Role | Dependencies |
|---|---|---|---|
| Parameter | experimenthandling | Data object holding a key/value pair (String/double) for simulation parameters | None |
| Measure | experimenthandling | Data object holding a key/value pair (both String) for simulation output measures | None |
| Options | experimenthandling | Configuration container: paths, cutoff planning type, stop criteria | None |
| Environment | experimenthandling | Represents one simulation scenario: id, parameter set, probability, trace of applied modifiers | Parameter |
| IExtractMeasures | interfaces | Interface: extract measures from a results file | Measure |
| IManageModifier | interfaces | Interface: initiate the modifier list | AModifier |
| IManageParametersFile | interfaces | Interface: read/write parameter files | Parameter |
| IStartSimulation | interfaces | Interface: start the external simulator | None |
| IStopProgram | interfaces | Interface: stop the program | None |
| AModifier | interfaces | Abstract base: a scenario modifier with a probability and a name; declares applyModifier | Environment |
| ASimulationSystemHandler | interfaces | Abstract base implementing all 5 interfaces; holds Options and modifier list | Options, AModifier, all 5 interfaces |
| FileManagement | util | Utility: file I/O (read, copy, move, create folders, load/save properties, write measures/modifiers) | Options, Environment, Measure, ASimulationSystemHandler |
| ExperimentPlanGenerator | experimenthandling | Runnable: BFS expansion of Environment tree, queues environments for simulation | Environment, Options, ASimulationSystemHandler, FileManagement, AModifier |
| ExperimentResultHandler | experimenthandling | Runnable: drains results queue, extracts measures, writes measures files | ASimulationSystemHandler, FileManagement, Options, Measure |
| ExperimentSimulatorHandler | experimenthandling | Runnable: drives simulation loop; consumes environment queue, triggers simulator, feeds results queue | Environment, Options, ASimulationSystemHandler, FileManagement, ExperimentPlanGenerator, ExperimentResultHandler |
| ConcreteModifier | gluecode | Concrete AModifier: applies arithmetic operator (+,-,*,/) to a named parameter | AModifier, Environment, Parameter |
| MySimulator | gluecode | Static utility: reads a param file, computes val1*val2, writes result file | None |
| SimpleSimulationHandler | gluecode | Concrete ASimulationSystemHandler: implements all abstract methods for file-based simulation | ASimulationSystemHandler, Parameter, Measure, AModifier, Options |
| StartProgram | interfaces | Static utility class: wires up threads (planning + simulator) and starts the experiment | FileManagement, Options, Environment, ExperimentPlanGenerator, ExperimentSimulatorHandler, ASimulationSystemHandler |
| Simulation | gluecode | Main entry point: creates modifiers, SimpleSimulationHandler, calls startProgram | StartProgram, ConcreteModifier, SimpleSimulationHandler |

---

## 2. Java Pattern → Python Equivalent Mapping

| Java Pattern | Python Equivalent |
|---|---|
| `interface` | `abc.ABC` with all methods decorated `@abstractmethod` |
| `abstract class` | `abc.ABC` with `@abstractmethod` on abstract methods; concrete methods defined normally |
| Multiple constructors | `__init__` with default `None` parameters + `@classmethod` factory methods where needed |
| `implements Runnable` | Subclass `threading.Thread`, override `run()` |
| `Vector<T>` | `list` |
| `BlockingQueue<T>` / `PriorityBlockingQueue<T>` | `queue.Queue` (thread-safe FIFO; priority ordering not critical to correctness here) |
| `synchronized` / thread-safe queue ops | `queue.Queue` methods are inherently thread-safe |
| `Comparable<T>` / `compareTo` | `__lt__` (and optionally `functools.total_ordering`) on the class |
| `Properties` file (key=value) | Manual line-by-line parsing or `configparser` with injected `[DEFAULT]` section header |
| `Calendar` / date arithmetic | `datetime.datetime` |
| `System.currentTimeMillis()` | `time.time() * 1000` |
| `TimeUnit.X.toMillis(n)` | Explicit multiplication constants |
| `Files.copy` / `Files.move` | `shutil.copy2` / `shutil.move` |
| `new File(path).mkdir()` | `os.makedirs(path, exist_ok=True)` |
| `System.getProperty("line.separator")` | `os.linesep` |
| `Collections.reverseOrder()` sort | `list.sort(reverse=True)` |
| `BufferedReader` / `FileReader` | `open(path, 'r', encoding='utf-8')` |
| `BufferedWriter` / `FileWriter` | `open(path, 'w', encoding='utf-8')` |
| `FileOutputStream` (append) | `open(path, 'a')` |
| `InputStream` | file path string or `io.IOBase` file-like object |
| `static` utility methods | `@staticmethod` or module-level functions |
| `Log4j Logger` | Python `logging` module |
| `Thread.currentThread().interrupt()` | `return` (no direct equivalent needed) |
| Getter/setter methods | Python `@property` / `@x.setter`, or plain attributes |

---

## 3. Maven Dependencies → Python Replacements

| Maven Dependency | Python Replacement | Justification |
|---|---|---|
| JDK standard library (`java.util.*`, `java.io.*`, `java.nio.*`) | Python stdlib: `os`, `shutil`, `pathlib`, `io`, `queue`, `threading`, `time`, `datetime`, `configparser` | All needed functionality exists in Python stdlib |
| `java.util.concurrent` (BlockingQueue, PriorityBlockingQueue) | `queue.Queue` | Thread-safe FIFO queue; PriorityQueue semantics not critical here |
| `java.util.logging` / Log4j (implied) | `logging` (stdlib) | Standard Python logging |
| No external Maven deps detected beyond JDK | No external pip packages required | The project only uses JDK built-ins |

**requirements.txt content**: No third-party packages needed; only Python stdlib is used. The file will be present but empty (or contain a comment).

---

## 4. Migration Order (Most Foundational First)

1. **Parameter** — no deps
2. **Measure** — no deps
3. **Options** — no deps
4. **IExtractMeasures** — no deps (interface)
5. **IManageModifier** — no deps (interface, references AModifier forward)
6. **IManageParametersFile** — depends on Parameter (interface)
7. **IStartSimulation** — no deps (interface)
8. **IStopProgram** — no deps (interface)
9. **AModifier** — depends on Environment (forward ref acceptable); abstract base
10. **Environment** — depends on Parameter
11. **ASimulationSystemHandler** — depends on all 5 interfaces, Options, AModifier
12. **FileManagement** — depends on Options, Environment, Measure, ASimulationSystemHandler
13. **ExperimentResultHandler** — depends on ASimulationSystemHandler, FileManagement, Options, Measure
14. **ExperimentPlanGenerator** — depends on Environment, Options, ASimulationSystemHandler, FileManagement, AModifier
15. **ExperimentSimulatorHandler** — depends on all above + ExperimentPlanGenerator, ExperimentResultHandler
16. **ConcreteModifier** — depends on AModifier, Environment, Parameter
17. **MySimulator** — no external deps
18. **SimpleSimulationHandler** — depends on ASimulationSystemHandler, Parameter, Measure, AModifier, Options
19. **StartProgram** — depends on FileManagement, Options, Environment, ExperimentPlanGenerator, ExperimentSimulatorHandler, ASimulationSystemHandler
20. **Simulation** — depends on StartProgram, ConcreteModifier, SimpleSimulationHandler (main entry point)
