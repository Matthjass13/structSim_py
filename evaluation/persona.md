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
