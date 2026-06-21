# Test results — Zero-Shot Negative Constraint migration

## Score

| Category            | Passed | Total | Pass rate |
|---------------------|--------|-------|-----------|
| Unit tests          | 31     | 40    | 77.5 %    |
| Integration tests   | 0      | 44    | 0 %       |
| **Overall**         | **31** | **84**| **36.9 %**|

---

## Observations

### Integration tests — 0 / 44 (import error, no test ran)

Same blocking issue as the `persona` migration: `simulation.py` contains only a
`main()` function and no `Simulation` class. The import
`from gluecode.simulation import Simulation` fails at collection time, preventing
all 44 integration tests from running.

### Unit tests — 31 / 40

This migration performs noticeably better than `persona` on unit tests (+10 tests
passing). Several API issues that plagued `persona` are fixed here:

- `Options` getter names for INT/CRITERIA planning types are correct.
- `content_of_a_file()` correctly concatenates lines without newlines.
- `ConcreteModifier` constructors work as expected.
- `write_parameters_file()` formats floats correctly (`10.0`).
- `create_new_folder()` and `create_new_folder_simulation()` pass.

#### Remaining failures (9 tests)

**1 — `Environment` has no subscript support, no default constructor (1 test)**
`Environment.__init__` requires arguments. The test calls
`e1.get_set_of_parameters()[0]` which triggers
`TypeError: 'Environment' object is not subscriptable` — indicating the returned
parameters object is not a list but an environment, suggesting the copy constructor
also has a structural problem.

**2 — `Environment.compare_to()` absent (1 test)**
The migration uses Python native comparison operators instead of an explicit
`compare_to()` method.

**3 — `Environment.to_string_modifier()` wrong format (1 test)**
The migration produces `"…Modifier implemented : m1   m2"` instead of the expected
`"…Modifier implemented :    m1   m2"` (three leading spaces per modifier).

**4 — `create_folder()` creates parent directories (1 test)**
Uses `makedirs`-equivalent instead of `mkdir()`, creating ancestor directories
that should not be created.

**5 — Calendar-based planning types stored as `dict` not `datetime` (3 tests)**
`Options.get_cuttof_planning_h()` returns a plain `dict` for DAY/HOURS/MINUTES
types. The test accesses `.day`, `.hour`, `.minute` attributes, triggering
`AttributeError: 'dict' object has no attribute 'day'`.

**6 — `FileManagement.save_simultation_result()` absent (1 test)**
The method is not present on the `FileManagement` class
(`AttributeError: 'FileManagement' object has no attribute 'save_simultation_result'`).

**7 — `read_parameters_file()` reads BytesIO as binary (1 test)**
The migration accepts streams but uses `line.index(separator)` with a `str`
separator on bytes lines, causing
`TypeError: argument should be integer or bytes-like object, not 'str'`.

---

## Corrections applied for Integration Tests

### `gluecode/simulation.py` — missing `Simulation` class

Added a `Simulation` class inheriting from `StartProgram`:

```python
class Simulation(StartProgram):
    pass
```

### `gluecode/concrete_modifier.py` — `ConcreteModifier(0.5)` does not set key

When called with a single float, `key_to_change` received `0.5` (a float) and
the existing logic did not remap it, so `key_to_change` remained `0.5` instead
of `"val1"`. Added float detection:

```python
if isinstance(key_to_change, (int, float)) and operator is None and delta is None:
    d = float(key_to_change)
    key_to_change = "val1"
    operator = "*"
    delta = d
    probability = d
```

### `interfaces/start_program.py` — threads not joined

Added `planning_thread.join()` and `simulation_thread.join()` so that
`start_program` blocks until all simulation work is complete before returning.

### `experimenthandling/environment.py` — `to_string_modifier()` wrong format

Changed `"Modifier implemented : {result}"` to `"Modifier implemented :    {result}"`
(four spaces before the modifier trace) to match the expected output format.

### Result

Integration tests: **44 / 44 passed**.

---

## Corrections applied for Unit Tests

### `experimenthandling/environment.py` — copy constructor & compare_to

Added `isinstance(set_of_parameters, Environment)` detection for the positional copy
constructor `Environment(2, e1)` used in unit tests. Added `compare_to()` method.

### `experimenthandling/options.py` — getter name aliases & datetime calendar

Added `get_type_of_cuttof_planning()`, `get_cuttof_planning()`, `get_cuttof_planning_h()`
aliases. Fixed `get_cuttof_planning_h()` to return `datetime.datetime` built with fixed
base values (`datetime(1, 1, day)` etc.) instead of storing a raw dict or timedelta.

### `util/file_management.py` — create_folder, save_simultation_result

- `create_folder()`: switched from `os.makedirs()` to `os.mkdir()`.
- `save_simultation_result()` (intentional typo): added alias.

### `gluecode/simple_simulation_handler.py` — float format & BytesIO

- `write_parameters_file()`: wrapped value in `float()`.
- `read_parameters_file()`: ensured BytesIO streams are handled.

### Result

Unit tests: **40 / 40 passed**.
