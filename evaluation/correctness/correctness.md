# Correctness — Java to Python Migration

**Column legend:**
- **ZS** = zeroShot · **OS** = oneShot · **CoT** = chainOfThought
- **negConst** = negativeConstraint · **withCtx** = withContext · **onlyTask** = onlyTask
- **aSimHdlr** = aSimulationSystemHandler · **concMod** = concreteModifier · **expPlanGen** = experimentPlanGenerator

---

## Test Results

| Migration           |  ║  | Unit passed | Unit total | Unit %  |  ║  | Int passed | Int total | Int %   |  ║  | **Overall** | **Total** | **%**     |
| ------------------- | :-: | ----------- | ---------- | ------- | :-: | ---------- | --------- | ------- | :-: | ----------- | --------- | --------- |
| ═══════════════════ | ══  | ═══════════ | ══════════ | ═══════ | ══  | ══════════ | ═════════ | ═══════ | ══  | ═══════════ | ═════════ | ═════════ |
| Transpiler          |  ║  | 0           | 40         | 0 %     |  ║  | 0          | 44        | 0 %     |  ║  | **0**       | **84**    | **0 %**   |
| ═══════════════════ | ══  | ═══════════ | ══════════ | ═══════ | ══  | ══════════ | ═════════ | ═══════ | ══  | ═══════════ | ═════════ | ═════════ |
| ZS/persona          |  ║  | 21          | 40         | 52.5 %  |  ║  | 0          | 44        | 0 %     |  ║  | **21**      | **84**    | **25.0 %**|
| ZS/negConst         |  ║  | 31          | 40         | 77.5 %  |  ║  | 0          | 44        | 0 %     |  ║  | **31**      | **84**    | **36.9 %**|
| ZS/onlyTask         |  ║  | 0           | 40         | 0 %     |  ║  | 0          | 44        | 0 %     |  ║  | **0**       | **84**    | **0 %**   |
| ZS/withCtx          |  ║  | 30          | 40         | 75 %    |  ║  | 0          | 44        | 0 %     |  ║  | **30**      | **84**    | **35.7 %**|
| ═══════════════════ | ══  | ═══════════ | ══════════ | ═══════ | ══  | ══════════ | ═════════ | ═══════ | ══  | ═══════════ | ═════════ | ═════════ |
| OS/aSimHdlr         |  ║  | 31          | 40         | 77.5 %  |  ║  | 0          | 44        | 0 %     |  ║  | **31**      | **84**    | **36.9 %**|
| OS/concMod          |  ║  | 28          | 40         | 70 %    |  ║  | 1          | 44        | 2.3 %   |  ║  | **29**      | **84**    | **34.5 %**|
| OS/expPlanGen       |  ║  | 19          | 40         | 47.5 %  |  ║  | 0          | 44        | 0 %     |  ║  | **19**      | **84**    | **22.6 %**|
| ═══════════════════ | ══  | ═══════════ | ══════════ | ═══════ | ══  | ══════════ | ═════════ | ═══════ | ══  | ═══════════ | ═════════ | ═════════ |
| CoT/lenient         |  ║  | 29          | 40         | 72.5 %  |  ║  | 0          | 44        | 0 %     |  ║  | **29**      | **84**    | **34.5 %**|
| CoT/perClass        |  ║  | 15          | 40         | 37.5 %  |  ║  | 0          | 44        | 0 %     |  ║  | **15**      | **84**    | **17.9 %**|
| CoT/strict          |  ║  | 30          | 40         | 75 %    |  ║  | 0          | 44        | 0 %     |  ║  | **30**      | **84**    | **35.7 %**|
| CoT/riskFirst       |  ║  | 0           | 40         | 0 %     |  ║  | 0          | 44        | 0 %     |  ║  | **0**       | **84**    | **0 %**   |

---

## Recurring Failures

The following issues appeared across multiple migrations. Each is annotated with the
migrations it affects.

### 1 — `parameters.txt` loaded as filesystem path instead of classpath resource
**Affects:** OS/aSimHdlr, OS/concMod, OS/expPlanGen, CoT/lenient, CoT/perClass, CoT/strict (all integration tests)

All migrations that have a working `Simulation` class still fail every integration
test. Inside `StartProgram.start_program`, `parameters.txt` is opened with `open(path, "rb")`
where `path` comes from `Options.get_path_parameters()`. In the Java original,
the file was loaded via `Simulation.class.getClassLoader().getResourceAsStream(...)`,
making it independent of the working directory. The Python migrations assume the
file exists at a filesystem path relative to the current working directory, which
is not the case in the test environment.

### 2 — No `Simulation` class defined
**Affects:** ZS/persona, ZS/negConst, CoT/lenient

`simulation.py` contains only a `main()` function or equivalent, but no `Simulation`
class. The import `from gluecode.simulation import Simulation` fails at collection
time, preventing all 44 integration tests from running.

### 3 — `Environment` has no default (no-argument) constructor
**Affects:** ZS/persona, ZS/negConst, ZS/withCtx, OS/aSimHdlr, OS/concMod, OS/expPlanGen, CoT/lenient, CoT/perClass, CoT/strict

`Environment()` called without arguments raises `TypeError` because `__init__`
requires positional arguments (`id_`, `set_of_parameters`, `probability`). The
Java class has a no-argument constructor used in several unit tests.

### 4 — `Environment` is not subscriptable
**Affects:** ZS/negConst, ZS/withCtx, OS/aSimHdlr, OS/concMod, CoT/perClass, CoT/strict

`e.get_set_of_parameters()[0]` raises `TypeError: 'Environment' object is not
subscriptable`. The copy-constructor test expects the returned parameters list to
support index access, but the migration returns an `Environment` instance or another
non-subscriptable object instead of a `list`.

### 5 — `Environment.compare_to()` absent
**Affects:** ZS/persona, ZS/negConst, ZS/withCtx, OS/aSimHdlr, OS/concMod, OS/expPlanGen, CoT/lenient, CoT/perClass, CoT/strict

Python native comparison operators (`==`, `<`) are used instead of an explicit
`compare_to()` method, causing `AttributeError` when the test calls
`e1.compare_to(e2)`.

### 6 — `Options` getter names corrected away from the Java typo
**Affects:** ZS/persona, ZS/withCtx, OS/concMod, CoT/lenient, CoT/perClass, CoT/strict

The Java API has a typo: `typeOfCuttOfPlanning` (one `f` in `CuttOf`). Faithful
snake_case would be `get_type_of_cuttof_planning()`. Several migrations silently
"fix" the typo to `get_type_of_cut_off_planning()`, causing `AttributeError` on
all five properties-loading tests that call the getter with the original spelling.

### 7 — `FileManagement.save_simultation_result()` absent
**Affects:** ZS/persona, ZS/negConst, ZS/withCtx, OS/aSimHdlr, OS/concMod, OS/expPlanGen, CoT/lenient, CoT/perClass, CoT/strict

The method is missing from `FileManagement`. The Java original has a
`saveSimultationResult` method (with its own typo: `Simultation`). Migrations either
omit it entirely or rename it, causing `AttributeError`.

### 8 — `create_folder()` creates parent directories
**Affects:** ZS/persona, ZS/negConst, ZS/withCtx, OS/aSimHdlr, OS/concMod, OS/expPlanGen, CoT/lenient, CoT/perClass, CoT/strict

`os.makedirs()` (or equivalent) is used instead of `os.mkdir()`. Java's `mkdir()`
returns `false` and does nothing when the parent directory does not exist; `makedirs`
creates the full path. The test asserts the folder is not created when its parent
is missing.

### 9 — `write_parameters_file()` formats whole-number floats without decimal
**Affects:** ZS/persona, OS/aSimHdlr, OS/concMod, CoT/lenient, CoT/strict

Python's default float-to-string conversion renders `10.0` as `"10"` when assigned
from an integer literal. The test asserts `lines[0] == "val1=10.0"`. The fix is to
explicitly format with `f"{value:.1f}"` or equivalent.

### 10 — `read_parameters_file()` does not accept a stream (`BytesIO`)
**Affects:** ZS/negConst, OS/aSimHdlr

The migration only handles string paths. When called with a `BytesIO` object
(emulating Java's `InputStream`), it raises `TypeError: expected str, bytes or
os.PathLike object, not BytesIO`.

### 11 — Structural packaging errors (complete failures)
**Affects:** Transpiler, ZS/onlyTask, CoT/riskFirst

Three migrations fail to collect a single test due to structural errors:

- **Transpiler** — PascalCase filenames (`Environment.py`) on case-sensitive Linux.
  `from experimenthandling.environment import Environment` cannot resolve
  `Environment.py`.
- **ZS/onlyTask** — All imports prefixed with `noStrategy.*`
  (`from noStrategy.experimenthandling.parameter import Parameter`). The
  `noStrategy` package does not exist at the PYTHONPATH root.
- **CoT/riskFirst** — Both errors combined: PascalCase filenames *and* all imports
  prefixed with `structuredsim.*`.
