class MySimulator:
    """
    Minimal mock simulator: reads val1 and val2 from a parameter file,
    computes val1 * val2, and writes the result to a result file.
    """

    @staticmethod
    def run(path_to_input_file: str, path_to_result_file: str) -> None:
        params = {}
        with open(path_to_input_file, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if "=" in line:
                    key, _, value = line.partition("=")
                    params[key.strip()] = float(value.strip())

        result = params["val1"] * params["val2"]

        with open(path_to_result_file, "w", encoding="utf-8") as fh:
            fh.write(f"result={result}\n")
