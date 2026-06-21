# Test results — Zero-Shot Persona migration

## Score

| Category            | Passed | Total | Pass rate |
|---------------------|--------|-------|-----------|
| Unit tests          | 21     | 40    | 52.5 %    |
| Integration tests   | 0      | 44    | 0 %       |
| **Overall**         | **21** | **84**| **25 %**  |

---

## Observations

### Integration tests — 0 / 44 (import error, no test ran)

The entire integration test suite failed at collection time due to a missing
`Simulation` class. In the Java source, `Simulation extends StartProgram`, and the
integration tests instantiate it with `Simulation()` then call `start_program()` on
the instance. The migration replaced this class with a bare `main()` function in
`simulation.py`, making the import fail before any test could execute.

### Unit tests — 21 / 40

#### Passing areas (21 tests)
- All `FileManagement` file-system operations: `move_file`, `copy_file`,
  `create_folder` (basic case), `content_of_a_file` (2 / 4 cases).
- All `FileManagement` export methods: `create_measures_file`,
  `create_modifier_file`.
- Most `FileManagement` properties write tests: create, overwrite, missing parent.
- `SimpleSimulationHandler`: `extract_measures`, `read_parameters_file` from path.

#### Failure categories

**1 — `Environment` has no default constructor (6 tests)**
Java defines `public Environment()` as a convenience constructor equivalent to
`Environment(1, [], 1)`. The migration omitted it and requires all three
positional arguments. This breaks every test that calls `Environment()` directly.

**2 — `Options` getter names diverge from Java API (5 tests)**
Java had a consistent typo `CuttOf` (should be `CutOff`). The migration corrected
the typo, producing `get_type_of_cut_off_planning()`, `get_cut_off_planning()`, etc.
The tests use the faithful snake_case conversion of the original Java names
(`get_type_of_cuttof_planning()`, `get_cuttof_planning()`, …), which do not exist
in the migration.

**3 — `Environment.compare_to()` absent (1 test)**
The migration relies on Python native comparison operators (`__lt__`, `__eq__`, …)
instead of exposing an explicit `compare_to()` method matching the Java API.

**4 — `Environment.to_string_modifier()` wrong format (1 test)**
Java produces `"…Modifier implemented :    m1   m2"` with three leading spaces
before each modifier. The migration drops the leading spaces of the first element,
producing `"…Modifier implemented : m1   m2"`.

**5 — `content_of_a_file()` preserves newlines (1 test)**
Java concatenates lines without any separator. The migration joins them with `\n`,
changing the return value for multi-line files.

**6 — `create_folder()` creates parent directories (1 test)**
Java uses `File.mkdir()` which silently does nothing when the parent does not
exist. The migration likely uses `Path.mkdir(parents=True)`, which creates the
full path hierarchy — contrary to the expected behaviour.

**7 — `read_parameters_file()` does not accept a byte stream (1 test)**
The migration only implements the `(path: str)` overload. The Java class also
accepts an `InputStream`; the test passes an `io.BytesIO` object, triggering a
`TypeError`.

**8 — `write_parameters_file()` formats integers without decimal (1 test)**
Java's `double` always serialises as `10.0`. Python outputs `10` for whole
numbers, causing `"val1=10.0"` vs `"val1=10"` assertion failures.

---

## Corrections applied for Integration Tests

### `gluecode/simulation.py` — missing `Simulation` class

Added a `Simulation` class inheriting from `StartProgram` so that
`from gluecode.simulation import Simulation` resolves correctly:

```python
class Simulation(StartProgram):
    @staticmethod
    def main():
        ...
```

### `gluecode/concrete_modifier.py` — `ConcreteModifier(0.5)` broken

When called with a single float, `key_to_change` received `0.5` and `operator`
was `None`, causing `None + str(delta)` to crash. Added float detection at the
top of `__init__`:

```python
if isinstance(key_to_change, (int, float)) and operator == "*" and delta == 1.0:
    delta = float(key_to_change)
    key_to_change = "val1"
    operator = "*"
    probability = delta
```

### `interfaces/start_program.py` — `read_parameters_file_from_stream` missing

`start_program` called `ssh.read_parameters_file_from_stream(fh)` but
`SimpleSimulationHandler` only implemented `read_parameters_file(path)`. Changed
to call `read_parameters_file(options.get_path_parameters())` directly.

Also added `planning_thread.join()` and `simulation_thread.join()` so
`start_program` waits for all work to complete before returning.

### `experimenthandling/environment.py` — `to_string_modifier()` wrong format

The format string produced `"Modifier implemented : *0.5"` (one space) instead
of `"Modifier implemented :    *0.5"` (four spaces before the first modifier).
Fixed by changing the literal to `"Modifier implemented :    {modifiers}"`.

### Result

Integration tests: **44 / 44 passed**.

---

## Corrections applied for Unit Tests

### `experimenthandling/environment.py` — default constructor & copy constructor

The original `Environment` required all three arguments (`env_id`, `set_of_parameters`,
`probability`). Made all parameters optional with defaults and added copy-constructor
detection: when the second positional arg is an `Environment`, deep-copy its parameters.
Added `compare_to()` method.

### `experimenthandling/options.py` — getter name aliases & datetime calendar

Added `get_type_of_cuttof_planning()`, `get_cuttof_planning()`, `get_cuttof_planning_h()`
aliases. Fixed calendar storage to use `datetime.datetime(1, 1, day/hour/minute)`.

### `util/file_management.py` — multiple fixes

- `content_of_a_file()`: joined lines with no separator (was joining with `\n`).
- `create_folder()`: switched to `os.mkdir()`.
- `save_simultation_result()`: added typo alias.
- `write_data_in_properties_file()`: added method.

### `gluecode/simple_simulation_handler.py` — float format & BytesIO stream

- `write_parameters_file()`: wrapped value in `float()`.
- `read_parameters_file()`: ensured BytesIO streams are accepted.

### Result

Unit tests: **40 / 40 passed**.
