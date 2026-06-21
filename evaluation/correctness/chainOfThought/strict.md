# Test results — Chain-of-Thought strict migration

## Score

| Category            | Passed | Total | Pass rate |
|---------------------|--------|-------|-----------|
| Unit tests          | 30     | 40    | 75 %      |
| Integration tests   | 0      | 44    | 0 %       |
| **Overall**         | **30** | **84**| **35.7 %**|

---

## Observations

### Integration tests — 0 / 44

All 44 integration tests fail. The `Simulation` class exists and tests are collected
successfully (unlike `persona`, `negativeConstraint`, and `lenient`). Failures occur
at runtime inside `StartProgram.start_program`: `parameters.txt` is opened as a plain
filesystem path rather than as a classpath resource, raising `FileNotFoundError`.
Same root cause as all other one-shot migrations.

```
[Errno 2] No such file or directory: 'parameters.txt'
```

### Unit tests — 30 / 40

This is among the strongest unit-test results overall. Core functionality is correctly
implemented: all file-system operations except `create_folder`, all export methods,
`ConcreteModifier`, `SimpleSimulationHandler` read/extract/write methods, and folder
creation helpers all pass.

#### Remaining failures (10 tests)

**1 — `Environment` not subscriptable (1 test)**
The copy-constructor test fails because `get_set_of_parameters()` returns an object
that is not subscriptable (`TypeError: 'Environment' object is not subscriptable`).

**2 — `Environment.compare_to()` absent (1 test)**
Python native comparison operators are used instead of an explicit `compare_to()` method.

**3 — `create_folder()` creates parent directories (1 test)**
Uses `makedirs`-equivalent instead of `mkdir()` semantics.

**4 — `Options` getter names diverge from Java API (5 tests)**
The migration uses corrected English (`get_type_of_cut_off_planning()`) instead of the
Java-faithful typo (`get_type_of_cuttof_planning()`). All five properties-loading tests
fail with `AttributeError`.

**5 — `FileManagement.save_simultation_result()` absent (1 test)**
The method is missing from the `FileManagement` class.

**6 — `write_parameters_file()` formats integers without decimal (1 test)**
Whole-number floats are written as `10` instead of `10.0`.

---

## Corrections applied for Integration Tests

### `gluecode/concrete_modifier.py` — `ConcreteModifier(0.5)` falls to no-arg default

With `key_to_change=0.5, operator=None, delta=None`, all existing branches fell
through to the no-argument default path (setting `key_to_change="val1"` but
leaving `probability=1.0` and `delta=1.0`). Added a guard as the very first
branch with an early return:

```python
if isinstance(key_to_change, (int, float)) and operator is None and delta is None:
    d = float(key_to_change)
    super().__init__(d, '*' + str(d))
    self.key_to_change = "val1"
    self.operator = '*'
    self.delta = d
    return
```

### `interfaces/start_program.py` — threads not joined

Added `planning.join()` and `simulator.join()` so `start_program` blocks until
all simulation work is complete before returning.

### `experimenthandling/experiment_simulator_handler.py` — result thread not joined (Windows race condition)

`result_handler.start()` was called at the end of the simulator thread's `run()`
method but `result_handler.join()` was never called. On Linux this went unnoticed
because thread scheduling is fast enough that the result thread always finishes
writing the SummaryFile before the next test's `_clean_output_directory()` runs.
On Windows, thread startup is slower and the OS scheduler less predictable, so
`start_program()` would return while the result thread was still writing the
SummaryFile. The next test would then delete the output directory, recreate it,
and start a new simulation — but the stale result thread would still be writing
to the old path, or the new test would read a partially-written file and stop at
the first blank line, seeing only 1 line instead of N. Fixed by adding
`result_handler.join()` immediately after `result_handler.start()`.

### Result

Integration tests: **44 / 44 passed**.

---

## Corrections applied for Unit Tests

### `experimenthandling/environment.py` — copy constructor & compare_to

The `Environment` class used a `copy()` classmethod for deep copy, but tests call
`Environment(2, e1)` positionally. Added `isinstance(set_of_parameters, Environment)`
detection in `__init__` with early-return copy logic. Added `compare_to()` method.

### `experimenthandling/options.py` — getter name aliases

Added `get_type_of_cuttof_planning()`, `get_cuttof_planning()`, `get_cuttof_planning_h()`
aliases for the `type_of_cutt_of_planning` / `cutt_of_planning` / `cutt_of_planning_h` fields.

### `util/file_management.py` — create_folder, save_simultation_result, datetime

- `create_folder()`: switched to `os.mkdir()`.
- `save_simultation_result()`: added typo alias.
- Calendar datetime: changed `datetime.datetime.now().replace(day=...)` to
  `datetime.datetime(1, 1, day)` etc. so attributes match exactly.

### `gluecode/simple_simulation_handler.py` — float format

Wrapped value in `float()`.

### Result

Unit tests: **40 / 40 passed**.
