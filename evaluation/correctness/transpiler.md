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
