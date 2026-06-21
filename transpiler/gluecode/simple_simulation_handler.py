import os
from experimenthandling.measure import Measure
from experimenthandling.parameter import Parameter
from interfaces.a_simulation_system_handler import ASimulationSystemHandler


class SimpleSimulationHandler(ASimulationSystemHandler):

    def __init__(self, modifiers=None):
        super().__init__()
        self._modifiers = modifiers if modifiers is not None else []

    def extract_measures(self, results_file_path):
        measures_list = []
        try:
            with open(results_file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.rstrip("\n")
                    pos = line.index("=")
                    key = line[:pos]
                    value = line[pos + 1:]
                    measures_list.append(Measure(key, value))
        except Exception as e:
            print(f"Error in extract_measures: {e}")
        return measures_list

    def initiate_modifier_list(self):
        self.list_modifier_class = self._modifiers
        return self.list_modifier_class

    def read_parameters_file(self, parameters_file_path):
        parameters_list = []
        try:
            if hasattr(parameters_file_path, "read"):
                content = parameters_file_path.read()
                if isinstance(content, bytes):
                    content = content.decode("utf-8")
                lines = content.splitlines()
            else:
                with open(parameters_file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

            for line in lines:
                line = line.rstrip("\n")
                if "=" in line:
                    pos = line.index("=")
                    key = line[:pos]
                    value = float(line[pos + 1:])
                    parameters_list.append(Parameter(key, value))
        except Exception as e:
            print(f"Error in read_parameters_file: {e}")
        return parameters_list

    def write_parameters_file(self, set_of_parameters, location_to_store):
        try:
            with open(location_to_store + "/myParamFile.txt", "w", encoding="utf-8") as f:
                for p in set_of_parameters:
                    f.write(p.get_key() + "=" + str(p.get_value()) + "\n")
        except Exception as e:
            print(f"Error in write_parameters_file: {e}")

    def start_simulation(self, path_to_input_file):
        result_file = self.options.get_path_to_simulator_result_file()
        os.makedirs(os.path.dirname(result_file), exist_ok=True)
        open(result_file, "a").close()

    def stop_program(self):
        pass
