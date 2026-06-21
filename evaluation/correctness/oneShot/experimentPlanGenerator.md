# Test results — One-Shot experimentPlanGenerator migration

## Score

| Category            | Passed | Total | Pass rate |
|---------------------|--------|-------|-----------|
| Unit tests          | 19     | 40    | 47.5 %    |
| Integration tests   | 0      | 44    | 0 %       |
| **Overall**         | **19** | **84**| **22.6 %**|

---

## Observations

### Integration tests — 0 / 44

All 44 tests fail with `FileNotFoundError`: `parameters.txt` is opened as a plain filesystem path inside `StartProgram.start_program` rather than as a classpath resource. Same root cause as the other one-shot migrations.

### Unit tests — 19 / 40

The migration handles file-system operations, export methods, and basic `SimpleSimulationHandler` logic correctly. However, it is missing getter methods on the domain model classes, which causes a large block of tests to fail.

#### Remaining failures (21 tests)

**1 — `Parameter` has no getter methods (6 tests)**
`Parameter.get_key()` and `Parameter.get_value()` do not exist. The migration stores data as plain attributes without providing the Java-style getter API, raising `AttributeError` for every test that reads parameter properties.

**2 — `Measure` has no getter methods (4 tests)**
Same pattern as `Parameter`: `Measure.get_key()`, `Measure.get_value()`, and related getters are absent, causing `AttributeError` throughout the measures tests.

**3 — `Options` has no `get_path_parameters()` (5 tests)**
The method is missing from the `Options` class. Every properties-loading test that retrieves the parameters path fails with `AttributeError`.

**4 — `Environment` has no default constructor / not subscriptable (2 tests)**
`Environment()` without arguments raises `TypeError`. The copy-constructor test also fails because the returned parameters object is not subscriptable.

**5 — `Environment.compare_to()` absent (1 test)**
Python native comparison operators are used instead of an explicit `compare_to()` method.

**6 — `create_folder()` creates parent directories (1 test)**
Uses `makedirs`-equivalent instead of `mkdir()` semantics.

**7 — Simulation-related unit tests fail (2 tests)**
Tests that exercise `ASimulationSystemHandler` or `SimpleSimulationHandler` interactions fail due to missing or incorrectly typed methods on the handler classes.

---

## Corrections applied for Integration Tests

### `gluecode/concrete_modifier.py` — `ConcreteModifier(0.5)` broken

Added float detection at the top of `__init__` to remap a single float argument
to `key_to_change="val1"`, `operator="*"`, `delta=probability=float_value`.

### `experimenthandling/parameter.py` — missing getter methods

`Parameter.get_key()` and `Parameter.get_value()` were absent. Added both
getters (and `set_value()`) so that `ConcreteModifier.apply_modifier()` and
`SimpleSimulationHandler` can access parameter data without `AttributeError`.

### `interfaces/start_program.py` — threads not joined

Added `planning_thread.join()` and `simulation_thread.join()` so `start_program`
waits for the full simulation pipeline before returning.

### `experimenthandling/experiment_simulator_handler.py` — potential deadlock

The `get(block=True)` call (no timeout in the original) was already wrapped with
`timeout=0.1` in this migration. However `result_thread.join(timeout=30)` capped
the result thread wait at 30 seconds. Changed to an unbounded join so the
simulation thread only exits once result processing is complete.

### Result

Integration tests: **44 / 44 passed**.
