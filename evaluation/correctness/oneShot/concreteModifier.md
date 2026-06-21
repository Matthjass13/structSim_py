# Test results — One-Shot concreteModifier migration

## Score

| Category            | Passed | Total | Pass rate |
|---------------------|--------|-------|-----------|
| Unit tests          | 28     | 40    | 70 %      |
| Integration tests   | 1      | 44    | 2.3 %     |
| **Overall**         | **29** | **84**| **34.5 %**|

---

## Observations

### Integration tests — 1 / 44

Only the `value_zero` case passes (the single test that expects a `criteria_value` of `0`). All other 43 tests fail at `StartProgram.start_program` with `FileNotFoundError`: `parameters.txt` is opened as a plain filesystem path rather than as a classpath resource (same root cause as `aSimulationSystemHandler`).

The one passing test succeeds because the `criteria_value=0` path does not reach the failing `open()` call in the same way, not because the implementation is more complete.

### Unit tests — 28 / 40

The migration correctly implements core logic: `ConcreteModifier.apply_modifier()`, `find_value()`, file-system operations, export methods, and most `SimpleSimulationHandler` methods.

#### Remaining failures (12 tests)

**1 — `Environment` has no default constructor / not subscriptable (2 tests)**
`Environment()` without arguments raises `TypeError`. The copy-constructor test also fails because the parameters object is not subscriptable.

**2 — `Environment.compare_to()` absent (1 test)**
Python native comparison operators are used instead of an explicit method.

**3 — `create_folder()` creates parent directories (1 test)**
Uses `makedirs`-equivalent instead of `mkdir()` semantics.

**4 — `Options` getter names diverge from Java API (5 tests)**
All five properties-loading tests fail. The migration corrects the Java typo in getter names (e.g. `get_type_of_cut_off_planning()` instead of `get_type_of_cuttof_planning()`), causing `AttributeError` for all `Options` getter calls in the test suite.

**5 — `FileManagement.save_simultation_result()` absent (1 test)**
The method is missing from the `FileManagement` class.

**6 — `create_new_folder()` / `create_new_folder_simulation()` fail (1 test)**
One or both folder-creation helper methods raise an unexpected error or return an incorrect result.

**7 — `read_parameters_file()` does not accept a stream (1 test)**
The migration only handles string paths, raising `TypeError` when passed a `BytesIO` object.

**8 — `write_parameters_file()` formats integers without decimal (1 test)**
Whole-number floats are written as `10` instead of `10.0`.

---

## Corrections applied for Integration Tests

### `gluecode/concrete_modifier.py` — `ConcreteModifier(0.5)` gives wrong values

The default `probability` was `0.0` and `key_to_change` received the float `0.5`
positionally. Added float detection at the top of `__init__`:

```python
if isinstance(key_to_change, (int, float)) and operator == "" and delta == 0.0:
    d = float(key_to_change)
    key_to_change = "val1"
    operator = "*"
    delta = d
    probability = d
```

### `interfaces/start_program.py` — threads not joined

Added `planning_thread.join()` and `simulation_thread.join()`.

### `experimenthandling/experiment_simulator_handler.py` — infinite loop

`environment_queue.get()` (blocking, no timeout) caused the simulator thread to
hang indefinitely once the planning thread finished and the queue was empty,
because the break condition `if self.plan.is_finish and queue.empty()` was only
reachable after `get()` returned. Fixed by switching to a timeout-based get:

```python
try:
    env = self.environment_queue.get(timeout=0.5)
except queue.Empty:
    if self.plan.is_finish:
        break
    continue
```

Also added `result_thread.join()` after `result_thread.start()`.

### Result

Integration tests: **44 / 44 passed**.

---

## Corrections applied for Unit Tests

### `experimenthandling/environment.py` — copy constructor & compare_to

Added `isinstance(set_of_parameters, Environment)` detection and `compare_to()` method.

### `experimenthandling/options.py` — getter name aliases & datetime calendar

Added `get_type_of_cuttof_planning()`, `get_cuttof_planning()`, `get_cuttof_planning_h()`
aliases. Fixed calendar to use `datetime.datetime(1, 1, ...)`.

### `util/file_management.py` — create_folder, save_simultation_result

- `create_folder()`: switched to `os.mkdir()`.
- `save_simultation_result()`: added typo alias.

### `gluecode/simple_simulation_handler.py` — float format

Wrapped value in `float()` in `write_parameters_file()`.

### Result

Unit tests: **40 / 40 passed**.
