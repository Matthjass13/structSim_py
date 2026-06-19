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
