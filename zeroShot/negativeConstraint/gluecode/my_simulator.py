class MySimulator:

    @staticmethod
    def run(path_to_input_file, path_to_result_file):
        params = {}
        try:
            with open(path_to_input_file, encoding="utf-8") as f:
                for line in f:
                    pos = line.index("=")
                    key = line[:pos].strip()
                    value = float(line[pos + 1:].strip())
                    params[key] = value

            result = params["val1"] * params["val2"]

            with open(path_to_result_file, "w", encoding="utf-8") as f:
                f.write(f"result={result}\n")

        except Exception as e:
            print(e)
