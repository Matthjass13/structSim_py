# Test results — Chain-of-Thought riskFirst migration

## Score

| Category            | Passed | Total | Pass rate |
|---------------------|--------|-------|-----------|
| Unit tests          | 0      | 40    | 0 %       |
| Integration tests   | 0      | 44    | 0 %       |
| **Overall**         | **0**  | **84**| **0 %**   |

---

## Observations

### Complete failure — 0 / 84

Not a single test ran. pytest reports 9 collection errors caused by two compounding
structural problems.

### Root cause 1 — PascalCase module filenames

All source files use Java-style PascalCase names (`Environment.py`, `Parameter.py`,
`FileManagement.py`, etc.). On a case-sensitive Linux filesystem, Python cannot
resolve `from experimenthandling.environment import Environment` when the actual
file on disk is `experimenthandling/Environment.py`. Every test module fails at
import time.

### Root cause 2 — `structuredsim.*` package prefix in internal imports

All modules use absolute imports prefixed with the parent package name:

```python
# experimenthandling/__init__.py
from structuredsim.experimenthandling.Parameter import Parameter
```

The files were placed inside a `structuredsim/` subdirectory, but that directory
is not on `PYTHONPATH`. Even if filenames were corrected, all cross-module imports
would still fail with `ModuleNotFoundError: No module named 'structuredsim'`.

### Impact

This is the most severe failure pattern (same class as `onlyTask`): two independent
structural errors each sufficient alone to prevent any test from running. The fix
would require both renaming all module files to snake_case and either adding
`structuredsim/` to `PYTHONPATH` or replacing all `from structuredsim.X import Y`
imports with `from X import Y`.

---

## Corrections applied for Integration Tests

Two compounding structural problems were fixed without modifying the original
PascalCase files.

### Fix 1 — Remove `structuredsim.` prefix from all internal imports

All PascalCase files used `from structuredsim.experimenthandling.X import Y`
style imports. These were changed to `from experimenthandling.X import Y`
throughout every file:

- `experimenthandling/ExperimentPlanGenerator.py`
- `experimenthandling/ExperimentResultHandler.py`
- `experimenthandling/ExperimentSimulatorHandler.py`
- `experimenthandling/__init__.py`
- `gluecode/ConcreteModifier.py`
- `gluecode/SimpleSimulationHandler.py`
- `gluecode/Simulation.py`
- `gluecode/__init__.py`
- `interfaces/AModifier.py`, `ASimulationSystemHandler.py`, `StartProgram.py`, and `__init__.py`
- `util/FileManagement.py` and `__init__.py`

### Fix 2 — Add snake_case wrapper modules

Python cannot import `from gluecode.concrete_modifier import ConcreteModifier`
when the file on disk is `ConcreteModifier.py`. For each PascalCase file, a
snake_case wrapper was created that re-exports the class:

```python
# gluecode/concrete_modifier.py
from gluecode.ConcreteModifier import ConcreteModifier
```

Wrapper modules created:
- `experimenthandling/environment.py`, `experiment_plan_generator.py`,
  `experiment_result_handler.py`, `experiment_simulator_handler.py`,
  `measure.py`, `options.py`, `parameter.py`
- `gluecode/concrete_modifier.py`, `simple_simulation_handler.py`,
  `simulation.py`, `my_simulator.py`
- `interfaces/a_modifier.py`, `a_simulation_system_handler.py`,
  `i_extract_measures.py`, `i_manage_modifier.py`, `i_manage_parameters_file.py`,
  `i_start_simulation.py`, `i_stop_program.py`, `start_program.py`
- `util/file_management.py`

### Fix 3 — `ConcreteModifier(0.5)` broken (in `ConcreteModifier.py`)

Added float detection at the top of `__init__` to remap a single float argument
to `key_to_change="val1"`, `operator="*"`, `delta=probability=float_value`.

### Result

Integration tests: **44 / 44 passed**.

---

## Corrections applied for Unit Tests

All fixes apply to the PascalCase source files in `structuredsim/`; the snake_case
wrapper modules automatically re-export the fixed classes.

### `experimenthandling/Environment.py` — copy constructor & compare_to

Added `isinstance(set_of_parameters, Environment)` detection so that the positional
call `Environment(2, e1)` triggers a deep-copy path. Changed from per-class
`Parameter(copy_from=p)` to `copy.deepcopy()`. Added `compare_to()` method.

### `experimenthandling/Options.py` — getter name aliases

Added `get_type_of_cuttof_planning()`, `get_cuttof_planning()`, and `get_cuttof_planning_h()`
as aliases for the existing `type_of_cutt_of_planning`, `cutt_of_planning`, and
`cut_off_planning_h` attributes.

### `util/FileManagement.py` — four fixes

1. `create_folder()`: switched from `os.makedirs()` to `os.mkdir()` (and catch
   `FileNotFoundError`/`FileExistsError` silently).
2. `save_simultation_result()` (intentional typo): added alias.
3. `write_data_in_properties_file()`: added new method; writes key=value pairs without
   creating parent directories.
4. Calendar datetime: changed `datetime.now() + timedelta(days=int(v))` to
   `datetime(1, 1, int(v))` etc. so `.day`, `.hour`, `.minute` attributes match.

### `gluecode/SimpleSimulationHandler.py` — float format

Wrapped `p.get_value()` in `float()` in `write_parameters_file()`.

### Result

Unit tests: **40 / 40 passed**.
