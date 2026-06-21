# Test results — Zero-Shot Only Task migration

## Score

| Category            | Passed | Total | Pass rate |
|---------------------|--------|-------|-----------|
| Unit tests          | 0      | 40    | 0 %       |
| Integration tests   | 0      | 44    | 0 %       |
| **Overall**         | **0**  | **84**| **0 %**   |

---

## Observations

### Complete failure — 0 / 84

Not a single test ran. Every module in the migration uses internal absolute
imports prefixed with `noStrategy.*`:

```python
# experimenthandling/environment.py
from noStrategy.experimenthandling.parameter import Parameter
```

All files across `experimenthandling/`, `gluecode/`, `interfaces/`, and `util/`
share this pattern. When pytest tries to import any test module, Python
immediately raises `ModuleNotFoundError: No module named 'noStrategy'`, causing
9 collection errors that abort the entire session.

### Root cause

The migration was generated assuming it would live inside a parent package named
`noStrategy`. The expected project structure was presumably:

```
noStrategy/
    experimenthandling/
    gluecode/
    interfaces/
    util/
```

But the files were placed directly at the PYTHONPATH root without the `noStrategy`
wrapper directory. As a result, the cross-module imports are all broken. No
behaviour can be tested at all.

### Impact

This is the most severe failure mode observed: a structural packaging error that
makes the migration completely untestable as delivered. The fix would require
either adding a `noStrategy/` parent package and adjusting PYTHONPATH, or
replacing all `from noStrategy.X import Y` imports with `from X import Y`.

---

## Corrections applied for Integration Tests

### `interfaces/start_program.py` — `parameters.txt` path and thread joins

The migration opened the parameters file via `open(o.get_path_parameters(), "rb")`
which failed because `get_path_parameters()` returned a relative path and the
working directory during tests is the repo root. This was fixed by passing the
path string directly to `read_parameters_file(o.get_path_parameters())` so the
handler resolves it using the absolute path stored in the config.

Additionally, `planning_thread.join()` and `simulation_thread.join()` were added
so that `start_program` waits for the full pipeline before returning.

The internal `noStrategy.*` import prefix issue documented above was resolved
separately by fixing all imports to use relative (`from X import Y`) form
throughout the migration.

### Result

Integration tests: **44 / 44 passed**.

---

## Corrections applied for Unit Tests

### `experimenthandling/environment.py` — copy constructor & compare_to

Added detection of `isinstance(set_of_parameters, Environment)` in `__init__` to handle
the positional copy constructor call `Environment(2, e1)` used in unit tests.
Added `compare_to()` method returning `-1`, `0`, or `1`.

### `experimenthandling/options.py` — getter name aliases & datetime calendar

Added `get_type_of_cuttof_planning()`, `get_cuttof_planning()`, and `get_cuttof_planning_h()`
aliases (Java-faithful "cuttof" typo). `get_cuttof_planning_h()` returns a `datetime.datetime`
object constructed as `datetime(1, 1, day)`, `datetime(1, 1, 1, hour)`, or
`datetime(1, 1, 1, 0, minute)` so the `.day`, `.hour`, `.minute` attributes match expectations.

### `util/file_management.py` — create_folder, save_simultation_result, write_data_in_properties_file

- `create_folder()`: switched from `os.makedirs()` to `os.mkdir()`.
- `save_simultation_result()` (intentional typo): added alias.
- `write_data_in_properties_file()`: added method without parent-directory creation.

### `gluecode/simple_simulation_handler.py` — float format

Wrapped `p.get_value()` in `float()` so `10.0` is written instead of `10`.

### Result

Unit tests: **40 / 40 passed**.
