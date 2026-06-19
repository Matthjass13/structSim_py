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
