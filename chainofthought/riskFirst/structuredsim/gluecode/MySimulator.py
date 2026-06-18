class MySimulator:
    """Reads a key=value parameter file, computes val1 * val2, writes result to output file."""

    @staticmethod
    def run(path_to_input_file: str, path_to_result_file: str) -> None:
        params = {}
        with open(path_to_input_file, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                pos = line.index("=")
                key = line[:pos].strip()
                value = float(line[pos + 1:].strip())
                params[key] = value

        result = params["val1"] * params["val2"]

        with open(path_to_result_file, "w", encoding="utf-8") as fh:
            fh.write(f"result={result}\n")
