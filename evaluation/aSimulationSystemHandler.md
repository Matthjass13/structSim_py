# Test results — One-Shot aSimulationSystemHandler migration

## Score

| Category            | Passed | Total | Pass rate |
|---------------------|--------|-------|-----------|
| Unit tests          | 31     | 40    | 77.5 %    |
| Integration tests   | 0      | 44    | 0 %       |
| **Overall**         | **31** | **84**| **36.9 %**|

---

## Observations

### Integration tests — 0 / 44

All 44 tests are collected and run but fail at the same point inside
`StartProgram.start_program`: after loading the config, the migration attempts
to open `parameters.txt` as a plain filesystem path rather than as a classpath
resource:

```python
open(o.get_path_parameters(), "rb")   # raises FileNotFoundError
```

In the Java original, `parameters.txt` was loaded via
`Simulation.class.getClassLoader().getResourceAsStream(...)`, making it
independent of the working directory. The migration assumes the file exists in
the current working directory, which is not the case in the test environment.

### Unit tests — 31 / 40

Same overall score as `negativeConstraint` (36.9%). The API is mostly faithful;
the passing areas include all file-system operations, export methods, most
properties tests, `ConcreteModifier`, and most `SimpleSimulationHandler` methods.

#### Remaining failures (9 tests)

**1 — `Environment` has no default constructor / not subscriptable (2 tests)**
`Environment()` without arguments raises `TypeError`. The copy-constructor test
also fails because `Environment.__init__` returns an object that is not
subscriptable when its parameter list is accessed.

**2 — `Environment.compare_to()` absent (1 test)**
Python native comparison operators are used instead of an explicit method.

**3 — `create_folder()` creates parent directories (1 test)**
Uses `makedirs`-equivalent, contrary to Java's `mkdir()` semantics.

**4 — Calendar types stored as `datetime.timedelta` instead of `datetime` (3 tests)**
`Options.get_cuttof_planning_h()` returns a `timedelta` object for DAY/HOURS/MINUTES
planning types. The test accesses `.day`, `.hour`, `.minute`, which are not
attributes of `timedelta`, raising `AttributeError`.

**5 — `FileManagement.save_simultation_result()` absent (1 test)**
The method does not exist on `FileManagement`
(`AttributeError: 'FileManagement' object has no attribute 'save_simultation_result'`).

**6 — `read_parameters_file()` does not accept a stream (1 test)**
The migration only handles string paths, raising
`TypeError: expected str, bytes or os.PathLike object, not BytesIO`.

**7 — `write_parameters_file()` formats integers without decimal (1 test)**
Whole-number floats are written as `10` instead of `10.0`.
