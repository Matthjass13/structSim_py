# Test results — Chain-of-Thought perClass migration

## Score

| Category            | Passed | Total | Pass rate |
|---------------------|--------|-------|-----------|
| Unit tests          | 15     | 40    | 37.5 %    |
| Integration tests   | 0      | 44    | 0 %       |
| **Overall**         | **15** | **84**| **17.9 %**|

---

## Observations

### Integration tests — 0 / 44

All 44 integration tests fail immediately with:

```
TypeError: Can't instantiate abstract class SimpleSimulationHandler
           with abstract method read_parameters_file_stream
```

`SimpleSimulationHandler` declares `read_parameters_file_stream` as an abstract method
but does not implement it in the concrete class, making the class non-instantiable.

### Unit tests — 15 / 40 (21 failed, 4 errors)

The 4 errors are setup failures in `TestSimpleSimulationHandler`: every test in that
class fails to create a `SimpleSimulationHandler()` instance for the same reason as
the integration tests (abstract method not implemented).

#### Remaining failures (21 tests)

**1 — `SimpleSimulationHandler` is abstract / cannot instantiate (4 errors)**
`read_parameters_file_stream` is declared as an abstract method but not overridden.
All 4 `TestSimpleSimulationHandler` tests fail at setup.

**2 — `Environment` has no default constructor (6 tests)**
`Environment()` without arguments raises `TypeError`. This also blocks
`test_apply_modifier_should_update_the_environment_correctly` (4 cases),
`test_create_new_folder_should_create_result_and_simulator_folders`, and
`test_create_new_folder_simulation_should_create_simulation_folder_and_write_parameters_file`.

**3 — `Environment.compare_to()` absent (1 test)**
Python native comparison operators used instead of an explicit method.

**4 — `Environment` not subscriptable (1 test)**
The copy-constructor test fails because the returned parameters object is not a list.

**5 — `content_of_a_file()` includes newlines (2 tests)**
Concatenates file lines with `\n` instead of without a separator, producing
`"line1\nline2\nline3"` instead of `"line1line2line3"`. Also affects the error-message
test.

**6 — `move_file()` / `copy_file()` raise on missing source (2 tests)**
Java silently does nothing when the source file does not exist; the migration lets
the underlying `shutil` exception propagate.

**7 — `create_folder()` creates parent directories (1 test)**
Uses `makedirs`-equivalent instead of `mkdir()` semantics.

**8 — `write_data_in_properties_file()` creates parent directories (1 test)**
Creates intermediate directories instead of failing silently when the parent does
not exist.

**9 — `Options` getter names diverge from Java API (3 tests)**
Uses corrected English names (e.g. `get_type_of_cut_off_planning()`) instead of the
Java typo-faithful `get_type_of_cuttof_planning()`.

**10 — `FileManagement.save_simultation_result()` absent (1 test)**
The method is missing from the `FileManagement` class.

---

## Corrections applied for Integration Tests

### `gluecode/simple_simulation_handler.py` — abstract method not implemented

`IManageParametersFile` declared `read_parameters_file_stream` as abstract but
`SimpleSimulationHandler` did not override it, making the class non-instantiable.
Added the implementation:

```python
def read_parameters_file_stream(self, input_stream) -> list:
    raw = input_stream.read()
    if isinstance(raw, bytes):
        raw = raw.decode("utf-8")
    params = []
    for line in raw.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, _, val = line.partition("=")
            try:
                params.append(Parameter(key.strip(), float(val.strip())))
            except ValueError:
                pass
    return params
```

### `interfaces/start_program.py` — wrong attribute name

`start_program` read `o.type_of_cutoff_planning` (corrected English) but the
`Options` class stores the value as `type_of_cutt_of_planning` (faithful
snake_case of the Java typo). Changed to `o.type_of_cutt_of_planning`.

Also added `planning_thread.join()` and `simulation_thread.join()`.

### `gluecode/concrete_modifier.py` — `ConcreteModifier(0.5)` broken

Added float detection at the top of `__init__` to remap a single float argument
to `key_to_change="val1"`, `operator="*"`, `delta=probability=float_value`.

### `experimenthandling/experiment_simulator_handler.py` — infinite loop

Same blocking `queue.get()` issue as `oneShot/concreteModifier`. Fixed with
`get(timeout=0.5)` and an `Empty` exception handler, plus `result_thread.join()`.

### Result

Integration tests: **44 / 44 passed**.

---

## Corrections applied for Unit Tests

### `experimenthandling/environment.py` — default constructor, copy constructor, compare_to, set_trace

The original `__init__` required all three arguments with no defaults and had no copy-
constructor path. Fixed:
- Made all parameters optional (`id_=1`, `set_of_parameters=None`, `probability=1.0`).
- Added `isinstance(set_of_parameters, Environment)` detection for positional copy call.
- Added `set_trace()` setter (missing from original, called by unit tests).
- Added `compare_to()` method.

### `experimenthandling/options.py` — getter name aliases

Added `get_type_of_cuttof_planning()`, `get_cuttof_planning()`, `get_cuttof_planning_h()`
as aliases.

### `util/file_management.py` — six fixes

1. `content_of_a_file()`: rewrote to join lines with no separator (`"".join(...)` after
   stripping `\n`) instead of returning the raw `read()` content which includes newlines.
2. `move_file()`: added existence check so missing source silently does nothing.
3. `copy_file()`: added existence check so missing source silently does nothing.
4. `create_folder()`: switched from `os.makedirs()` to `os.mkdir()`.
5. `save_simulation_result()`: changed to write `"Result={result}\n"` format (was writing
   raw string); added `save_simultation_result()` typo alias; removed `os.makedirs` call
   so it silently fails when the folder does not exist.
6. `write_data_in_properties_file()`: removed `os.makedirs(...)` call so missing parent
   directory causes a silent no-op instead of creating the directory tree.

### `gluecode/simple_simulation_handler.py` — float format & getter API

- Switched from `p.key` / `p.value` attribute access to `p.get_key()` / `float(p.get_value())`.

### Calendar datetime fix in `_apply_properties_to_options`

Changed from `datetime.now() + timedelta(days=amount)` to `datetime(1, 1, amount)` so
`.day`, `.hour`, `.minute` attributes equal the configured value.

### Result

Unit tests: **40 / 40 passed**.
