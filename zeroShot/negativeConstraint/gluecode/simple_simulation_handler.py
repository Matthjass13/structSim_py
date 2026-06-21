import os
from experimenthandling.measure import Measure
from experimenthandling.parameter import Parameter
from interfaces.a_simulation_system_handler import ASimulationSystemHandler


class SimpleSimulationHandler(ASimulationSystemHandler):

    def __init__(self, modifiers=None):
        super().__init__()
        self.modifiers = modifiers if modifiers is not None else []

    def extract_measures(self, results_file_path):
        separator = "="
        measures_list = []
        try:
            with open(results_file_path, encoding="utf-8") as f:
                for line in f:
                    pos = line.index(separator)
                    measure_key = line[:pos]
                    measure_value = line[pos + 1:].rstrip("\n")
                    measures_list.append(Measure(measure_key, measure_value))
        except OSError as e:
            print(e)
        return measures_list

    def initiate_modifier_list(self):
        self.list_modifier_class = self.modifiers
        return self.list_modifier_class

    def read_parameters_file(self, path_or_stream):
        separator = "="
        parameters_list = []
        try:
            if isinstance(path_or_stream, str):
                f = open(path_or_stream, encoding="utf-8")
                close_after = True
            else:
                f = path_or_stream
                close_after = False

            for line in f:
                if isinstance(line, bytes):
                    line = line.decode("utf-8")
                pos = line.index(separator)
                key = line[:pos]
                value = float(line[pos + 1:].rstrip("\n"))
                parameters_list.append(Parameter(key, value))

            if close_after:
                f.close()
        except OSError as e:
            print(e)
        return parameters_list

    def write_parameters_file(self, set_of_parameters, location_to_store):
        try:
            with open(location_to_store + "/myParamFile.txt", "w", encoding="utf-8") as f:
                for p in set_of_parameters:
                    f.write(f"{p.get_key()}={p.get_value()}\n")
        except Exception as e:
            print(e)

    def start_simulation(self, path_to_input_file):
        result_file = self.options.get_path_to_simulator_result_file()
        os.makedirs(os.path.dirname(result_file), exist_ok=True)
        open(result_file, "a").close()

    def stop_program(self):
        pass
