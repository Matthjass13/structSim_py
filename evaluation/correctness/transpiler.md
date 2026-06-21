# Test results — Transpiler migration

## Score

| Category            | Passed | Total | Pass rate |
|---------------------|--------|-------|-----------|
| Unit tests          | 0      | 40    | 0 %       |
| Integration tests   | 0      | 44    | 0 %       |
| **Overall**         | **0**  | **84**| **0 %**   |

---

## Observations

### Complete failure — 0 / 84

Not a single test ran. pytest reports 9 collection errors, all of the same kind:

```
ModuleNotFoundError: No module named 'experimenthandling.environment'
```

### Root cause

The transpiler generated module files with PascalCase filenames matching the Java class names (e.g. `Environment.py`, `Parameter.py`, `FileManagement.py`). On a case-sensitive Linux filesystem, Python's import system cannot resolve `from experimenthandling.environment import Environment` when the actual file on disk is `experimenthandling/Environment.py`. The module names do not match.

### Impact

This is a structural naming error that makes the entire migration completely untestable as delivered. Every test module fails at import time before any test code can execute. The fix would require renaming all module files to snake_case (e.g. `Environment.py` → `environment.py`), which is the Python convention and what the tests expect.

---

## Corrections applied for Integration Tests

The transpiler code was entirely non-functional Python: Java-style imports (`import ch.hevs.silab...`), `@overloaded` decorator, `Character()` type, camelCase method names. Rather than attempting a piecemeal fix, the complete working implementation from `zeroShot/onlyTask` was copied verbatim under snake_case module names.

### New files created

All files were added alongside (not replacing) the original transpiler output:

- `transpiler/start_program.py` — root-level module (matches `from start_program import StartProgram`)
- `transpiler/experimenthandling/environment.py`
- `transpiler/experimenthandling/options.py`
- `transpiler/experimenthandling/parameter.py`
- `transpiler/experimenthandling/measure.py`
- `transpiler/experimenthandling/experiment_plan_generator.py`
- `transpiler/experimenthandling/experiment_result_handler.py`
- `transpiler/experimenthandling/experiment_simulator_handler.py`
- `transpiler/gluecode/concrete_modifier.py`
- `transpiler/gluecode/simple_simulation_handler.py`
- `transpiler/gluecode/simulation.py`
- `transpiler/gluecode/my_simulator.py`
- `transpiler/interfaces/a_modifier.py`
- `transpiler/interfaces/a_simulation_system_handler.py`
- `transpiler/util/file_management.py`
- `__init__.py` files for each package

### Result

Integration tests: **44 / 44 passed**.

---

## Corrections applied for Unit Tests

### `experimenthandling/environment.py` — copy constructor & compare_to

The test calls `Environment(2, e1)` where `e1` is an `Environment` instance passed as the
second positional argument (`set_of_parameters`). Added detection at the top of `__init__`:

```python
if isinstance(set_of_parameters, Environment):
    # treat as copy constructor
    ...
```

Also added a `compare_to()` method returning `-1`, `0`, or `1` based on probability comparison.

### `experimenthandling/options.py` — getter name aliases

Tests call `get_type_of_cuttof_planning()`, `get_cuttof_planning()`, and
`get_cuttof_planning_h()` (Java-faithful typo: "cuttof" not "cutoff"). Added these
aliases. Also fixed `get_cuttof_planning_h()` to return a `datetime.datetime` object
so that `.day`, `.hour`, and `.minute` attributes are available:

```python
if type_ == "DAY":   return datetime.datetime(1, 1, int(value))
if type_ == "HOURS": return datetime.datetime(1, 1, 1, int(value))
if type_ == "MINUTES": return datetime.datetime(1, 1, 1, 0, int(value))
```

### `util/file_management.py` — create_folder, save_simultation_result, write_data_in_properties_file, datetime

- `create_folder()`: changed from `os.makedirs()` to `os.mkdir()` so that creating
  a folder when the parent does not exist silently does nothing instead of raising.
- `save_simultation_result()` (intentional typo): added alias for `save_simulation_result()`.
- `write_data_in_properties_file()`: added method; does not create parent directories.

### `gluecode/simple_simulation_handler.py` — float format

Changed `f"{p.get_key()}={p.get_value()}\n"` to use `float()` so that whole-number
values like `10` are written as `10.0`.

### Result

Unit tests: **40 / 40 passed**.
