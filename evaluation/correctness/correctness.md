# Correctness — Java to Python Migration

**Legend:**
- **Trans** = Transpiler · **ZS** = zeroShot · **OS** = oneShot · **CoT** = chainOfThought
- **ZS/NC** = negativeConstraint · **ZS/OT** = onlyTask · **ZS/Pe** = persona · **ZS/Ctx** = withContext
- **OS/AS** = aSimulationSystemHandler · **OS/CM** = concreteModifier · **OS/EP** = experimentPlanGenerator
- **CoT/PC** = perClass · **CoT/Le** = lenient · **CoT/St** = strict · **CoT/RF** = riskFirst

---

## Test Results

| Migration           |  ║  | Unit passed | Unit total | Unit %  |  ║  | Int passed | Int total | Int %   |  ║  | **Overall** | **Total** | **%**     |
| ------------------- | :-: | ----------- | ---------- | ------- | :-: | ---------- | --------- | ------- | :-: | ----------- | --------- | --------- |
| ═══════════════════ | ══  | ═══════════ | ══════════ | ═══════ | ══  | ══════════ | ═════════ | ═══════ | ══  | ═══════════ | ═════════ | ═════════ |
| Trans               |  ║  | 0           | 40         | 0 %     |  ║  | 0          | 44        | 0 %     |  ║  | **0**       | **84**    | **0 %**   |
| ═══════════════════ | ══  | ═══════════ | ══════════ | ═══════ | ══  | ══════════ | ═════════ | ═══════ | ══  | ═══════════ | ═════════ | ═════════ |
| ZS/Pe               |  ║  | 21          | 40         | 52.5 %  |  ║  | 0          | 44        | 0 %     |  ║  | **21**      | **84**    | **25.0 %**|
| ZS/NC               |  ║  | 31          | 40         | 77.5 %  |  ║  | 0          | 44        | 0 %     |  ║  | **31**      | **84**    | **36.9 %**|
| ZS/OT               |  ║  | 0           | 40         | 0 %     |  ║  | 0          | 44        | 0 %     |  ║  | **0**       | **84**    | **0 %**   |
| ZS/Ctx              |  ║  | 30          | 40         | 75 %    |  ║  | 0          | 44        | 0 %     |  ║  | **30**      | **84**    | **35.7 %**|
| ═══════════════════ | ══  | ═══════════ | ══════════ | ═══════ | ══  | ══════════ | ═════════ | ═══════ | ══  | ═══════════ | ═════════ | ═════════ |
| OS/AS               |  ║  | 31          | 40         | 77.5 %  |  ║  | 0          | 44        | 0 %     |  ║  | **31**      | **84**    | **36.9 %**|
| OS/CM               |  ║  | 28          | 40         | 70 %    |  ║  | 1          | 44        | 2.3 %   |  ║  | **29**      | **84**    | **34.5 %**|
| OS/EP               |  ║  | 19          | 40         | 47.5 %  |  ║  | 0          | 44        | 0 %     |  ║  | **19**      | **84**    | **22.6 %**|
| ═══════════════════ | ══  | ═══════════ | ══════════ | ═══════ | ══  | ══════════ | ═════════ | ═══════ | ══  | ═══════════ | ═════════ | ═════════ |
| CoT/Le              |  ║  | 29          | 40         | 72.5 %  |  ║  | 0          | 44        | 0 %     |  ║  | **29**      | **84**    | **34.5 %**|
| CoT/PC              |  ║  | 15          | 40         | 37.5 %  |  ║  | 0          | 44        | 0 %     |  ║  | **15**      | **84**    | **17.9 %**|
| CoT/St              |  ║  | 30          | 40         | 75 %    |  ║  | 0          | 44        | 0 %     |  ║  | **30**      | **84**    | **35.7 %**|
| CoT/RF              |  ║  | 0           | 40         | 0 %     |  ║  | 0          | 44        | 0 %     |  ║  | **0**       | **84**    | **0 %**   |

---

## Post-correction Test Results

Results after all corrections were applied (unit-test fixes, integration-test fixes, Windows race-condition fixes).

| Migration           |  ║  | Unit passed | Unit total | Unit %  |  ║  | Int passed | Int total | Int %   |  ║  | **Overall** | **Total** | **%**      |
| ------------------- | :-: | ----------- | ---------- | ------- | :-: | ---------- | --------- | ------- | :-: | ----------- | --------- | ---------- |
| ═══════════════════ | ══  | ═══════════ | ══════════ | ═══════ | ══  | ══════════ | ═════════ | ═══════ | ══  | ═══════════ | ═════════ | ══════════ |
| Transpiler          |  ║  | 40          | 40         | 100 %   |  ║  | 44         | 44        | 100 %   |  ║  | **84**      | **84**    | **100 %**  |
| ═══════════════════ | ══  | ═══════════ | ══════════ | ═══════ | ══  | ══════════ | ═════════ | ═══════ | ══  | ═══════════ | ═════════ | ══════════ |
| ZS/persona          |  ║  | 40          | 40         | 100 %   |  ║  | 44         | 44        | 100 %   |  ║  | **84**      | **84**    | **100 %**  |
| ZS/negConst         |  ║  | 40          | 40         | 100 %   |  ║  | 44         | 44        | 100 %   |  ║  | **84**      | **84**    | **100 %**  |
| ZS/onlyTask         |  ║  | 40          | 40         | 100 %   |  ║  | 44         | 44        | 100 %   |  ║  | **84**      | **84**    | **100 %**  |
| ZS/withCtx          |  ║  | 40          | 40         | 100 %   |  ║  | 44         | 44        | 100 %   |  ║  | **84**      | **84**    | **100 %**  |
| ═══════════════════ | ══  | ═══════════ | ══════════ | ═══════ | ══  | ══════════ | ═════════ | ═══════ | ══  | ═══════════ | ═════════ | ══════════ |
| OS/aSimHdlr         |  ║  | 40          | 40         | 100 %   |  ║  | 44         | 44        | 100 %   |  ║  | **84**      | **84**    | **100 %**  |
| OS/concMod          |  ║  | 40          | 40         | 100 %   |  ║  | 44         | 44        | 100 %   |  ║  | **84**      | **84**    | **100 %**  |
| OS/expPlanGen       |  ║  | 40          | 40         | 100 %   |  ║  | 44         | 44        | 100 %   |  ║  | **84**      | **84**    | **100 %**  |
| ═══════════════════ | ══  | ═══════════ | ══════════ | ═══════ | ══  | ══════════ | ═════════ | ═══════ | ══  | ═══════════ | ═════════ | ══════════ |
| CoT/lenient         |  ║  | 40          | 40         | 100 %   |  ║  | 44         | 44        | 100 %   |  ║  | **84**      | **84**    | **100 %**  |
| CoT/perClass        |  ║  | 40          | 40         | 100 %   |  ║  | 44         | 44        | 100 %   |  ║  | **84**      | **84**    | **100 %**  |
| CoT/strict          |  ║  | 40          | 40         | 100 %   |  ║  | 44         | 44        | 100 %   |  ║  | **84**      | **84**    | **100 %**  |
| CoT/riskFirst       |  ║  | 40          | 40         | 100 %   |  ║  | 44         | 44        | 100 %   |  ║  | **84**      | **84**    | **100 %**  |

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

---

## Cross-Migration Correction Analysis

The sections below group the corrections that were applied across migrations to make the test suites pass, separated by test category. Rows are ordered by number of affected migrations (descending).

**Column legend (same as above):**
Trans · ZS/OT · ZS/Pe · ZS/Ctx · ZS/NC · OS/AS · OS/CM · OS/EP · CoT/Le · CoT/PC · CoT/St · CoT/RF

---

### Unit Tests — Correction Matrix

| Correction                   |  ║  | Trans | ZS/OT | ZS/Pe | ZS/Ctx | ZS/NC | OS/AS | OS/CM | OS/EP | CoT/Le | CoT/PC | CoT/St | CoT/RF |  ║  | Count |
| ---------------------------- | :-: | :---: | :---: | :---: | :----: | :---: | :---: | :---: | :---: | :----: | :----: | :----: | :----: | :-: | :---: |
| ════════════════════════════ | ══  | ═════ | ═════ | ═════ | ══════ | ═════ | ═════ | ═════ | ═════ | ══════ | ══════ | ══════ | ══════ | ══  | ═════ |
| env-copy-ctor                |  ║  |   ✓   |   ✓   |   ✓   |   ✓    |   ✓   |   ✓   |   ✓   |   ✓   |   ✓    |   ✓    |   ✓    |   ✓    |  ║  |  12   |
| env-compare-to               |  ║  |   ✓   |   ✓   |   ✓   |   ✓    |   ✓   |   ✓   |   ✓   |   ✓   |   ✓    |   ✓    |   ✓    |   ✓    |  ║  |  12   |
| options-cuttof-aliases       |  ║  |   ✓   |   ✓   |   ✓   |   ✓    |   ✓   |   ✓   |   ✓   |   ✓   |   ✓    |   ✓    |   ✓    |   ✓    |  ║  |  12   |
| float-format                 |  ║  |   ✓   |   ✓   |   ✓   |   ✓    |   ✓   |   ✓   |   ✓   |   ✓   |   ✓    |   ✓    |   ✓    |   ✓    |  ║  |  12   |
| create-folder-mkdir          |  ║  |   ✓   |   ✓   |   ✓   |   ✓    |   ✓   |   ✓   |   ✓   |   ✓   |   ✓    |   ✓    |   ✓    |   ✓    |  ║  |  12   |
| save-simultation-result      |  ║  |   ✓   |   ✓   |   ✓   |   ✓    |   ✓   |   ✓   |   ✓   |   ✓   |   ✓    |   ✓    |   ✓    |   ✓    |  ║  |  12   |
| datetime-calendar            |  ║  |   ✓   |   ✓   |   ✓   |   ✓    |   ✓   |   ✓   |   ✓   |   ✓   |   ✓    |   ✓    |   ✓    |   ✓    |  ║  |  12   |
| ════════════════════════════ | ══  | ═════ | ═════ | ═════ | ══════ | ═════ | ═════ | ═════ | ═════ | ══════ | ══════ | ══════ | ══════ | ══  | ═════ |
| write-data-properties        |  ║  |   ✓   |   ✓   |   ✓   |        |       |       |       |       |        |   ✓    |        |   ✓    |  ║  |   5   |
| structural-fix               |  ║  |   ✓   |   ✓   |       |        |       |       |       |       |        |        |        |   ✓    |  ║  |   3   |
| bytesio-stream               |  ║  |       |       |   ✓   |        |   ✓   |       |       |       |        |        |        |        |  ║  |   2   |
| content-no-newlines          |  ║  |       |       |   ✓   |        |       |       |       |       |        |   ✓    |        |        |  ║  |   2   |
| env-set-trace                |  ║  |       |       |       |        |       |       |       |       |        |   ✓    |        |        |  ║  |   1   |
| measure-getters              |  ║  |       |       |       |        |       |       |       |   ✓   |        |        |        |        |  ║  |   1   |
| move-copy-silent             |  ║  |       |       |       |        |       |       |       |       |        |   ✓    |        |        |  ║  |   1   |
| simple-sim-getter-api        |  ║  |       |       |       |        |       |       |       |       |        |   ✓    |        |        |  ║  |   1   |

---

### Unit Tests — Correction Glossary

**env-copy-ctor** — `Environment` copy constructor support.  
The Java `Environment` class had a two-argument constructor `Environment(id, other)` where `other` is an existing `Environment` instance to copy from. No migration implemented this path. Fix: detect `isinstance(set_of_parameters, Environment)` at the top of `__init__` and deep-copy the source environment's parameter list.

**env-compare-to** — `Environment.compare_to()` explicit method.  
Migrations relied on Python's native `__lt__`/`__eq__` for comparisons, omitting the Java-style `compare_to()` method. Fix: add `compare_to(other)` returning `-1`, `0`, or `1` based on probability comparison.

**options-cuttof-aliases** — `Options` getter aliases for Java's `cuttof` typo.  
The Java API contains a consistent typo: `typeOfCuttOfPlanning` (one `f`). Most migrations silently corrected it to `cutoff`, causing `AttributeError` on the five properties tests that call the typo-faithful getter names. Fix: add `get_type_of_cuttof_planning()`, `get_cuttof_planning()`, and `get_cuttof_planning_h()` as aliases.

**float-format** — `write_parameters_file()` serialises whole-number floats with decimal.  
Python converts `10.0` to `"10"` when the value originates from an integer literal. The test asserts `lines[0] == "val1=10.0"`. Fix: wrap the value in `float()` (or format with `f"{value:.1f}"`) before writing.

**create-folder-mkdir** — `create_folder()` uses `os.mkdir()` not `os.makedirs()`.  
Java's `File.mkdir()` silently returns `false` and does nothing when the parent directory does not exist. Migrations used `os.makedirs()` (or `Path.mkdir(parents=True)`), which creates the full path hierarchy. Fix: switch to `os.mkdir()` and catch `FileNotFoundError`/`FileExistsError` silently.

**save-simultation-result** — `FileManagement.save_simultation_result()` typo alias.  
The Java source spells the method `saveSimultationResult` (typo: *Simultation*). Migrations either renamed it to the correctly-spelled `save_simulation_result` or omitted it entirely. Fix: add `save_simultation_result()` as an alias (or primary method name) to match the Java API.

**datetime-calendar** — `get_cuttof_planning_h()` returns a `datetime` object, not a `timedelta` or `dict`.  
When the planning type is `DAY`/`HOURS`/`MINUTES`, tests access `.day`, `.hour`, or `.minute` on the returned value. Migrations returned a `timedelta`, a `dict`, or called `datetime.now() + timedelta(...)`, none of which expose the expected attributes with the expected values. Fix: return `datetime.datetime(1, 1, day)`, `datetime.datetime(1, 1, 1, hour)`, or `datetime.datetime(1, 1, 1, 0, minute)` so the attribute equals exactly the configured integer value.

**write-data-properties** — `write_data_in_properties_file()` does not create parent directories.  
The method was either missing or, when present, called `os.makedirs()` for the parent path. Java's equivalent silently does nothing when the target directory does not exist. Fix: add the method and write key=value pairs directly without any directory-creation call.

**structural-fix** — Snake_case module names and correct import prefixes.  
Three migrations could not collect a single test: Transpiler used PascalCase filenames (`Environment.py`), ZS/onlyTask prefixed all imports with `noStrategy.*`, and CoT/riskFirst combined PascalCase filenames with a `structuredsim.*` prefix. Fix varies per migration: renaming files to snake_case, adding snake_case wrapper modules that re-export classes, stripping the spurious package prefix from all internal imports, or copying a working implementation wholesale.

**bytesio-stream** — `read_parameters_file()` accepts a `BytesIO` stream.  
The Java method accepted an `InputStream`; the test passes an `io.BytesIO` object. Migrations only implemented the `(path: str)` overload, raising `TypeError` on stream input. Fix: detect `BytesIO` (or any file-like object), call `.read()`, decode bytes to UTF-8, then parse the resulting string.

**content-no-newlines** — `content_of_a_file()` concatenates lines without separator.  
The Java implementation concatenates all lines with no separator, producing `"line1line2line3"`. Migrations joined with `"\n"`, changing the return value. Fix: use `"".join(lines)` after stripping trailing newlines from each line.

**env-set-trace** — `Environment.set_trace()` setter added.  
CoT/perClass omitted this setter, which is called by unit tests to configure the modifier trace before asserting `to_string_modifier()`. Fix: add `set_trace(self, trace)` to store the trace string.

**measure-getters** — `Measure.get_key()` and `Measure.get_value()` getters added.  
OS/expPlanGenerator stored measure data as plain attributes without providing Java-style getters, causing `AttributeError` in tests that read measure properties. Fix: add `get_key()` and `get_value()` methods.

**move-copy-silent** — `move_file()` and `copy_file()` are silent on missing source.  
Java silently does nothing when the source does not exist. CoT/perClass let the underlying `shutil` exception propagate. Fix: add an existence check before the operation; skip silently if the source file is absent.

**simple-sim-getter-api** — `SimpleSimulationHandler` uses getter methods, not direct attribute access.  
CoT/perClass accessed `p.key` / `p.value` directly instead of `p.get_key()` / `p.get_value()`, causing `AttributeError` when `Parameter` objects expose only the getter API. Fix: switch to the method calls.

---

### Integration Tests — Correction Matrix

| Correction                   |  ║  | Trans | ZS/OT | ZS/Pe | ZS/Ctx | ZS/NC | OS/AS | OS/CM | OS/EP | CoT/Le | CoT/PC | CoT/St | CoT/RF |  ║  | Count |
| ---------------------------- | :-: | :---: | :---: | :---: | :----: | :---: | :---: | :---: | :---: | :----: | :----: | :----: | :----: | :-: | :---: |
| ════════════════════════════ | ══  | ═════ | ═════ | ═════ | ══════ | ═════ | ═════ | ═════ | ═════ | ══════ | ══════ | ══════ | ══════ | ══  | ═════ |
| threads-join                 |  ║  |       |   ✓   |   ✓   |        |   ✓   |   ✓   |   ✓   |   ✓   |   ✓    |   ✓    |   ✓    |        |  ║  |   9   |
| concrete-modifier-float      |  ║  |       |       |   ✓   |   ✓    |   ✓   |       |   ✓   |   ✓   |   ✓    |   ✓    |   ✓    |   ✓    |  ║  |   9   |
| ════════════════════════════ | ══  | ═════ | ═════ | ═════ | ══════ | ═════ | ═════ | ═════ | ═════ | ══════ | ══════ | ══════ | ══════ | ══  | ═════ |
| simulation-class             |  ║  |       |       |   ✓   |        |   ✓   |       |       |       |   ✓    |        |        |        |  ║  |   3   |
| structural-fix               |  ║  |   ✓   |   ✓   |       |        |       |       |       |       |        |        |        |   ✓    |  ║  |   3   |
| parameters-txt-path          |  ║  |       |   ✓   |   ✓   |        |       |   ✓   |       |       |        |        |        |        |  ║  |   3   |
| to-string-modifier           |  ║  |       |       |   ✓   |        |   ✓   |       |       |       |   ✓    |        |        |        |  ║  |   3   |
| result-thread-join           |  ║  |       |       |       |        |       |       |   ✓   |   ✓   |        |        |   ✓    |        |  ║  |   3   |
| ════════════════════════════ | ══  | ═════ | ═════ | ═════ | ══════ | ═════ | ═════ | ═════ | ═════ | ══════ | ══════ | ══════ | ══════ | ══  | ═════ |
| result-queue-sentinel        |  ║  |       |       |       |        |       |       |       |   ✓   |        |        |   ✓    |        |  ║  |   2   |
| simulator-queue-timeout      |  ║  |       |       |       |        |       |       |   ✓   |       |        |   ✓    |        |        |  ║  |   2   |
| ════════════════════════════ | ══  | ═════ | ═════ | ═════ | ══════ | ═════ | ═════ | ═════ | ═════ | ══════ | ══════ | ══════ | ══════ | ══  | ═════ |
| abstract-method-impl         |  ║  |       |       |       |        |       |       |       |       |        |   ✓    |        |        |  ║  |   1   |
| bfs-ordering                 |  ║  |       |       |       |   ✓    |       |       |       |       |        |        |        |        |  ║  |   1   |
| options-attribute-name-int   |  ║  |       |       |       |        |       |       |       |       |        |   ✓    |        |        |  ║  |   1   |
| parameter-getters-int        |  ║  |       |       |       |        |       |       |       |   ✓   |        |        |        |        |  ║  |   1   |

---

### Integration Tests — Correction Glossary

**threads-join** — Planning and simulator threads joined before `start_program` returns.  
`start_program` spawned a planning thread and a simulator thread but returned before they completed. Tests then checked output files that had not yet been written. Fix: add `planning_thread.join()` and `simulation_thread.join()` at the end of `start_program` so the function only returns once the full simulation pipeline has finished.

**concrete-modifier-float** — `ConcreteModifier(delta)` single-float constructor.  
The Java class defines a one-argument convenience constructor `ConcreteModifier(double delta)` that sets `key_to_change="val1"`, `operator="*"`, and `probability=delta`. Python's keyword defaults caused the float to land in `key_to_change`, leaving `operator=None` and triggering `TypeError: NoneType + str`. Fix: detect `isinstance(key_to_change, (int, float))` at the top of `__init__` and remap the arguments to the correct fields.

**simulation-class** — Missing `Simulation` class in `simulation.py`.  
Three migrations implemented `simulation.py` as a bare `main()` function, omitting the `Simulation` class that the integration tests import via `from gluecode.simulation import Simulation`. Fix: add `class Simulation(StartProgram): pass` (or with a `main()` static method) so the import resolves.

**structural-fix** — Snake_case module filenames and correct import prefixes (integration).  
Same root cause as in unit tests: Transpiler, ZS/onlyTask, and CoT/riskFirst could not be imported at all. For integration tests the fixes were: copying a working implementation wholesale (Transpiler), stripping the `noStrategy.*` prefix from all imports (ZS/onlyTask), and both stripping the `structuredsim.*` prefix and adding snake_case wrapper modules (CoT/riskFirst).

**parameters-txt-path** — `parameters.txt` resolved as a filesystem path, not a classpath resource.  
The Java code loaded `parameters.txt` via `getClass().getClassLoader().getResourceAsStream(...)`, making the path independent of the working directory. Migrations opened it with `open(o.get_path_parameters(), "rb")` relative to the current working directory, which raises `FileNotFoundError` in the test environment. Fix: pass the absolute path string directly to `read_parameters_file()` and let the handler open the file, or resolve the path from the config object.

**to-string-modifier** — `to_string_modifier()` format string has wrong number of leading spaces.  
The expected output is `"Modifier implemented :    *0.5"` (four spaces before the first modifier). Migrations produced `"Modifier implemented : *0.5"` (one space). Fix: change the format string to use four leading spaces before the modifier trace.

**result-thread-join** — Result handler thread joined after start.  
`result_thread.start()` was called without a subsequent `result_thread.join()`, so `start_program` could return while the thread was still writing the SummaryFile. The next test would then delete or partially read the file. Fix: add `result_thread.join()` immediately after `result_thread.start()`.

**result-queue-sentinel** — `ExperimentResultHandler` drain loop uses a sentinel, not `queue.empty()`.  
`Queue.empty()` is unreliable under concurrent access: the inner drain loop could exit early, writing only partial results to the SummaryFile. Fix: have `ExperimentSimulatorHandler` put `None` into the queue after the simulation loop ends, then have `ExperimentResultHandler` use a blocking `queue.get()` loop that exits on the `None` sentinel, guaranteeing all results are processed.

**simulator-queue-timeout** — `ExperimentSimulatorHandler` queue.get() uses a timeout.  
A blocking `environment_queue.get()` (no timeout) caused the simulator thread to hang indefinitely once the planning thread had finished and the queue was drained, because the exit condition was only reachable after `get()` returned. Fix: switch to `get(timeout=0.5)`, catch `queue.Empty`, and break when `plan.is_finish` is true and the queue is empty.

**abstract-method-impl** — `SimpleSimulationHandler.read_parameters_file_stream()` implemented.  
CoT/perClass declared `read_parameters_file_stream` as an abstract method on the interface but never overrode it in `SimpleSimulationHandler`, making the class non-instantiable. Fix: provide a concrete implementation that reads bytes from the stream, decodes to UTF-8, and parses key=value lines into `Parameter` objects.

**bfs-ordering** — `Environment.__lt__` tiebreaker removed for stable FIFO ordering.  
ZS/withContext used `self.id < other.id` as a tiebreaker when probabilities were equal, which, combined with `sort(reverse=True)`, caused higher-ID (newer) environments to be explored before lower-ID (older) ones. The Java reference uses FIFO order for equal probabilities. Fix: remove the id-based tiebreaker so Python's stable sort preserves insertion order.

**options-attribute-name-int** — `start_program` reads the correct internal attribute name.  
CoT/perClass stored the planning type as `type_of_cutt_of_planning` (faithful to the Java typo) but `start_program` read `type_of_cutoff_planning` (corrected English), causing `AttributeError` at runtime. Fix: change the read site to `o.type_of_cutt_of_planning`.

**parameter-getters-int** — `Parameter.get_key()` and `get_value()` added for integration tests.  
OS/expPlanGenerator stored parameter data as plain attributes without Java-style getters. `ConcreteModifier.apply_modifier()` and `SimpleSimulationHandler` called `p.get_key()` / `p.get_value()`, raising `AttributeError`. Fix: add both getter methods (and `set_value()`) to the `Parameter` class.
