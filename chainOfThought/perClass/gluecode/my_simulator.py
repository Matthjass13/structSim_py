"""
Chain-of-thought for MySimulator:
1. Java-specific constructs:
   - Static method only (no instance state).
   - BufferedReader/InputStreamReader with explicit UTF-8 charset.
   - HashMap<String, Double> for parameter storage.
   - BufferedWriter/FileWriter for output.
2. Python equivalents:
   - @staticmethod in a class, or a module-level function; class kept for structural symmetry.
   - Built-in open() with encoding="utf-8".
   - Plain dict for parameters.
   - open() with write mode for output.
3. Risks/deviations:
   - Java splits on first '=' per line; Python str.partition('=') is equivalent.
   - KeyError (missing val1/val2) not guarded — matches Java NPE behavior.
"""


class MySimulator:
    """Simple simulator that reads parameters and writes val1*val2 as result."""

    @staticmethod
    def run(path_to_input_file: str, path_to_result_file: str) -> None:
        params: dict[str, float] = {}
        try:
            with open(path_to_input_file, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if "=" in line:
                        key, _, val = line.partition("=")
                        params[key.strip()] = float(val.strip())

            result = params["val1"] * params["val2"]

            with open(path_to_result_file, "w", encoding="utf-8") as f:
                f.write(f"result={result}\n")
        except Exception as e:
            import traceback
            traceback.print_exc()
