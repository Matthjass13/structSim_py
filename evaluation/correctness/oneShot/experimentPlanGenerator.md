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

### `experimenthandling/experiment_simulator_handler.py` — result thread join timeout (Windows race condition)

The `get(block=True)` call (no timeout in the original) was already wrapped with
`timeout=0.1` in this migration. However `result_thread.join(timeout=30)` capped
the result thread wait at 30 seconds, which caused a race condition on Windows.

On Linux, thread scheduling is fast enough that the result thread finishes writing
the SummaryFile well within the 30-second cap, so all tests passed. On Windows,
thread startup overhead and slower I/O mean the result thread occasionally did not
complete within the timeout. `start_program()` would then return while the result
thread was still writing, and the next test's `_clean_output_directory()` would
race against it: the new simulation would start, the test would read a
partially-written SummaryFile and stop at the first blank line, seeing only 1 line
instead of N. Fixed by changing `result_thread.join(timeout=30)` to an unbounded
`result_thread.join()` so `start_program` only returns once result processing is
fully complete.

### `experimenthandling/experiment_result_handler.py` — unreliable `queue.empty()` check (Windows race condition)

`ExperimentResultHandler.run()` used `results_queue.empty()` to decide whether to
process results. `Queue.empty()` is inherently unreliable in threaded contexts: on
Linux, the simulator thread finishes all `put()` calls before the result thread
starts, so `empty()` reliably returns `False`. On Windows, thread scheduling is
less predictable and memory visibility differs, so `empty()` could return `True`
even when items were present, or return `True` after reading only the first item,
causing the SummaryFile to contain only 1 line instead of N.

Fixed by replacing the `empty()`-based drain with a sentinel-based blocking loop:

- `ExperimentSimulatorHandler` puts `None` into `results_queue` after breaking out
  of the simulation loop (just before starting the result thread).
- `ExperimentResultHandler.run()` uses a blocking `results_queue.get()` loop,
  processing each item until it receives the `None` sentinel, then exits.

This guarantees all results are processed regardless of thread scheduling order.

### Result

Integration tests: **44 / 44 passed**.

---

## Corrections applied for Unit Tests

### `experimenthandling/environment.py` — copy constructor & compare_to

The `__init__` had a 4th `other` parameter for copy construction, but the test calls
`Environment(2, e1)` with `e1` as the second positional arg. Added detection:

```python
if isinstance(set_of_parameters, Environment):
    other = set_of_parameters
```

Also changed the deep-copy to use `copy.deepcopy()` instead of per-class `Parameter(other=p)`
to ensure mutation of the copy does not affect the original. Added `compare_to()` method.

### `experimenthandling/measure.py` — getter methods

`Measure` stored data as plain attributes but lacked `get_key()` and `get_value()` getters.
Added both so that `extract_measures` test results can be queried.

### `experimenthandling/options.py` — full rewrite with correct getter names & datetime

The original `Options` used internal fields (`cut_off_planning`, `type_of_cut_off_planning`)
and exposed no getters. Rewrote to expose:
- `get_type_of_cuttof_planning()` / `set_type_of_cuttof_planning()`
- `get_cuttof_planning()` / `set_cuttof_planning()`
- `get_cuttof_planning_h()` / `set_cuttof_planning_h()`
- All other standard getters/setters

`get_cuttof_planning_h()` returns `datetime.datetime(1, 1, day)`, `datetime.datetime(1, 1, 1, hour)`,
or `datetime.datetime(1, 1, 1, 0, minute)` so `.day`, `.hour`, `.minute` match expectations.

Also kept backward-compat direct attributes (`type_of_cut_off_planning`, `cut_off_planning`)
used by `start_program.py`.

### `util/file_management.py` — multiple fixes

- `create_folder()`: switched from `os.makedirs()` to `os.mkdir()`.
- `save_simultation_result()` (intentional typo): added alias.
- `load_data_from_properties_file()`: updated to call new Options setters and use correct
  `datetime.datetime` construction instead of `timedelta`.

### `gluecode/simple_simulation_handler.py` — float format

Wrapped value in `float()` in `write_parameters_file()` to produce `"val1=10.0"`.

### Result

Unit tests: **40 / 40 passed**.
