# Migration Strategy — Java → Python (riskFirst approach)

## Step 1 — Risk Analysis

### Challenge 1 — Multi-threaded BlockingQueue architecture

**Java pattern**  
Three `Runnable` threads communicate through two `PriorityBlockingQueue` instances:
- Planning thread → `BlockingQueue<Environment>` → Simulation thread → `BlockingQueue<String>` → Result thread.

`BlockingQueue.add()` is non-blocking (throws on full); `BlockingQueue.take()` blocks until an item is available.
The simulation thread checks `plan.isFinish && queue.isEmpty()` to know when to stop.

**Translation strategy**  
- `PriorityBlockingQueue<Environment>` → `queue.Queue()` (FIFO; ordering is applied by the planning thread via `list.sort(reverse=True)` before enqueuing, preserving the Java BFS-most-probable-first behaviour).
- `BlockingQueue.add()` → `queue.Queue.put_nowait()`.
- `BlockingQueue.take()` → `queue.Queue.get(block=True, timeout=0.5)` inside a `while True` loop; on `queue.Empty` with `plan.is_finish` set, the loop exits.
- `Runnable.run()` is preserved as an instance method `run()` started in `threading.Thread(target=obj.run)`.

---

### Challenge 2 — Java interfaces and abstract classes → Python ABCs

**Java pattern**  
`AModifier` and `ASimulationSystemHandler` are abstract classes; five `I*` types are interfaces.
`SimpleSimulationHandler` extends `ASimulationSystemHandler` which implements all five interfaces.
Java enforces method implementation at compile time.

**Translation strategy**  
- All interfaces (`IExtractMeasures`, `IManageModifier`, `IManageParametersFile`, `IStartSimulation`, `IStopProgram`) are translated as `ABC` subclasses with `@abstractmethod`.
- `AModifier` → `ABC` with `@abstractmethod apply_modifier()`.
- `ASimulationSystemHandler` → `ABC` inheriting all five interface ABCs (multiple inheritance). Python's MRO resolves this cleanly.
- Concrete classes (`SimpleSimulationHandler`, `ConcreteModifier`) override every abstract method; Python raises `TypeError` at instantiation if any is missing, replicating compile-time enforcement.

---

### Challenge 3 — Java Properties file and Calendar for time-based cutoffs

**Java pattern**  
`java.util.Properties.load(InputStream)` reads a `key = value` format without section headers.
`java.util.Calendar` stores a day/hour/minute offset that is later compared with `System.currentTimeMillis()`.

**Translation strategy**  
- `Properties` → `configparser.RawConfigParser` (no interpolation). Because `.properties` files have no section header, the file content is prefixed with `[DEFAULT]` before parsing.
- `Calendar.set(HOUR_OF_DAY, n)` used as a deadline → `datetime.now() + timedelta(hours=n)` stored in `Options.cut_off_planning_h`. The planning thread checks `datetime.now() < deadline` instead of `System.currentTimeMillis() < endTime`.
- Both a `str` path and a binary stream overload are supported (needed by tests that write a temp config file and open it as `rb`).

---

### Challenge 4 — Java ClassLoader resource loading

**Java pattern**  
`Simulation.class.getClassLoader().getResourceAsStream("config.properties")` and `getResourceAsStream(o.getPathParameters())` load files bundled inside the JAR from the classpath.

**Translation strategy**  
- Bundled resources are placed in `structuredsim/resources/` with an `__init__.py` marker, making it a proper Python package.
- `importlib.resources.open_binary("structuredsim.resources", filename)` replaces `getResourceAsStream`.
- For `pathParameters`, the value in `config.properties` is treated as a plain filesystem path first; if it is a bare filename (no path separator), it is resolved relative to the package resources directory.
- Test code passes an open binary stream directly, which `SimpleSimulationHandler.read_parameters_file()` accepts by detecting `isinstance(source, IOBase)`.

---

### Challenge 5 — Java generics and Vector<T>

**Java pattern**  
`Vector<Parameter>`, `List<AModifier>`, and `BlockingQueue<Environment>` use compile-time generic types.
`Vector` provides thread-safe access; it is used here only for sequential iteration.

**Translation strategy**  
- `Vector<T>` → `list` (Python list is sufficient; thread safety is provided by the queue layer, not the data structures).
- Generic type hints are expressed with Python's `typing` module (`List[Parameter]`, `List[AModifier]`, `queue.Queue`) for IDE support and documentation, without runtime enforcement overhead.
- `Collections.sort(list, reverseOrder())` → `list.sort(reverse=True)`, relying on `Environment.__lt__` (which delegates to probability comparison) to satisfy Python's sort protocol.

---

## Step 2 — Migration summary

All 20 Java classes were migrated following the dependency order below:

| Order | Java class | Python module |
|-------|-----------|---------------|
| 1 | `Parameter` | `experimenthandling/Parameter.py` |
| 2 | `Measure` | `experimenthandling/Measure.py` |
| 3 | `Options` | `experimenthandling/Options.py` |
| 4 | `Environment` | `experimenthandling/Environment.py` |
| 5 | `AModifier` | `interfaces/AModifier.py` |
| 6 | `IExtractMeasures` | `interfaces/IExtractMeasures.py` |
| 7 | `IManageModifier` | `interfaces/IManageModifier.py` |
| 8 | `IManageParametersFile` | `interfaces/IManageParametersFile.py` |
| 9 | `IStartSimulation` | `interfaces/IStartSimulation.py` |
| 10 | `IStopProgram` | `interfaces/IStopProgram.py` |
| 11 | `ASimulationSystemHandler` | `interfaces/ASimulationSystemHandler.py` |
| 12 | `FileManagement` | `util/FileManagement.py` |
| 13 | `ExperimentPlanGenerator` | `experimenthandling/ExperimentPlanGenerator.py` |
| 14 | `ExperimentResultHandler` | `experimenthandling/ExperimentResultHandler.py` |
| 15 | `ExperimentSimulatorHandler` | `experimenthandling/ExperimentSimulatorHandler.py` |
| 16 | `ConcreteModifier` | `gluecode/ConcreteModifier.py` |
| 17 | `MySimulator` | `gluecode/MySimulator.py` |
| 18 | `SimpleSimulationHandler` | `gluecode/SimpleSimulationHandler.py` |
| 19 | `StartProgram` | `interfaces/StartProgram.py` |
| 20 | `Simulation` | `gluecode/Simulation.py` |

## Step 3 — Naming conventions

| Java | Python |
|------|--------|
| `camelCase` methods | `snake_case` methods |
| `CamelCase` classes | `CamelCase` classes (unchanged) |
| `isFinish` | `is_finish` |
| `cuttOfPlanning` | `cutt_of_planning` |
| `applyModifier` | `apply_modifier` |
| `startSimulation` | `start_simulation` |

## Step 4 — No third-party runtime dependencies

The migration relies exclusively on the Python standard library:
`abc`, `configparser`, `datetime`, `logging`, `os`, `queue`, `shutil`, `threading`.
`pytest` is the only external dependency and is development-only.
