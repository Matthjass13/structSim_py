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
