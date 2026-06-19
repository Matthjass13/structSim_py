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
