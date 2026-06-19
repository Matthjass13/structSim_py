# Test results — Zero-Shot With Context migration

## Score

| Category            | Passed | Total | Pass rate |
|---------------------|--------|-------|-----------|
| Unit tests          | 30     | 40    | 75 %      |
| Integration tests   | 0      | 44    | 0 %       |
| **Overall**         | **30** | **84**| **35.7 %**|

---

## Observations

### Integration tests — 0 / 44 (runtime error)

Unlike `persona` and `negativeConstraint`, the `Simulation` class exists and the
tests are collected successfully. All 44 tests fail at runtime because
`ConcreteModifier(delta)` — the single-argument convenience constructor used in
`_return_modifiers_from_scenario()` — is broken. The migration defines:

```python
def __init__(self, key_to_change=None, operator=None, delta=0.0, probability=1.0):
    if key_to_change is None and operator is None:
        ...  # default path
    else:
        super().__init__(probability, operator + str(delta))  # crashes
```

When called as `ConcreteModifier(0.5)`, `key_to_change` receives `0.5` and
`operator` is `None`, so the `else` branch executes and
`None + str(0.0)` raises `TypeError`. The shorthand constructor that Java defined
as `ConcreteModifier(double delta)` was not faithfully translated.

### Unit tests — 30 / 40

This is the strongest unit-test result across all four zero-shot migrations. Many
areas of the API are correctly implemented:

- `content_of_a_file()` concatenates without newlines ✓
- All file-system operations (move, copy, create_folder basic) ✓
- All measures/modifier file exports ✓
- All `write_data_in_properties_file` variants ✓
- `ConcreteModifier.apply_modifier()` with explicit constructor ✓
- `ConcreteModifier.find_value()` ✓
- All three `SimpleSimulationHandler` read/extract methods ✓
- `create_new_folder()` and `create_new_folder_simulation()` ✓

#### Remaining failures (10 tests)

**1 — `Environment` has no subscript support, no default constructor (2 tests)**
Same pattern as the other migrations: `Environment()` requires three positional
arguments, and `TypeError: 'Environment' object is not subscriptable` surfaces
when the copy constructor test tries to index into the parameter list.

**2 — `Environment.compare_to()` absent (1 test)**
Python native comparison operators are used instead of an explicit `compare_to()`
method.

**3 — `create_folder()` creates parent directories (1 test)**
Uses `makedirs`-equivalent, creating ancestor directories that should not be
created per the Java `mkdir()` semantics.

**4 — `Options` getter names diverge from Java API (5 tests)**
Same typo-correction issue as `persona`: the migration uses `get_type_of_cut_off_planning()`
(corrected English), whereas the test expects `get_type_of_cuttof_planning()`
(faithful snake_case of Java's original `typeOfCuttOfPlanning`). All five
properties-loading tests that query `Options` getters fail with `AttributeError`.

**5 — `FileManagement.save_simultation_result()` absent (1 test)**
The method is missing from the `FileManagement` class.

**6 — `write_parameters_file()` formats integers without decimal (1 test)**
Python outputs `10` for whole-number floats instead of the Java-style `10.0`,
causing the assertion `lines[0] == "val1=10.0"` to fail.
