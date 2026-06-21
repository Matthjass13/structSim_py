import os

from interfaces.a_simulation_system_handler import ASimulationSystemHandler
from experimenthandling.parameter import Parameter
from experimenthandling.measure import Measure


class SimpleSimulationHandler(ASimulationSystemHandler):
    def __init__(self, modifiers=None):
        super().__init__()
        self._modifiers = modifiers if modifiers is not None else []

    # ------------------------------------------------------------------
    # IExtractMeasures
    # ------------------------------------------------------------------

    def extract_measures(self, results_file_path: str) -> list:
        separator = "="
        measures_list = []
        try:
            with open(results_file_path, 'r', encoding='utf-8') as f:
                for line in f:
                    line = line.rstrip('\n')
                    if not line:
                        continue
                    pos = line.index(separator)
                    measure_key = line[:pos]
                    measure_value = line[pos + 1:]
                    measures_list.append(Measure(measure_key, measure_value))
        except Exception as e:
            print(e)
        return measures_list

    # ------------------------------------------------------------------
    # IManageModifier
    # ------------------------------------------------------------------

    def initiate_modifier_list(self) -> list:
        self.list_modifier_class = self._modifiers
        return self.list_modifier_class

    # ------------------------------------------------------------------
    # IManageParametersFile
    # ------------------------------------------------------------------

    def read_parameters_file(self, parameters_file_path) -> list:
        """
        Accept either a file path (str) or a file-like object.
        Returns a list of Parameter.
        """
        separator = "="
        parameters_list = []
        try:
            if isinstance(parameters_file_path, str):
                f = open(parameters_file_path, 'r', encoding='utf-8')
                lines = f.readlines()
                f.close()
            else:
                # file-like object (InputStream equivalent)
                raw = parameters_file_path.read()
                if isinstance(raw, bytes):
                    raw = raw.decode('utf-8')
                lines = raw.splitlines()
                parameters_file_path.close()

            for line in lines:
                line = line.rstrip('\n')
                if not line:
                    continue
                pos = line.index(separator)
                key = line[:pos]
                value = float(line[pos + 1:])
                parameters_list.append(Parameter(key, value))
        except Exception as e:
            print(e)
        return parameters_list

    def write_parameters_file(self, set_of_parameters: list, location_to_store: str) -> None:
        try:
            with open(os.path.join(location_to_store, "myParamFile.txt"), 'w', encoding='utf-8') as bw:
                for p in set_of_parameters:
                    bw.write(p.get_key() + "=" + str(float(p.get_value())) + "\n")
        except Exception as e:
            print(e)

    # ------------------------------------------------------------------
    # IStartSimulation
    # ------------------------------------------------------------------

    def start_simulation(self, path_to_input_file: str) -> None:
        result_file = self.options.get_path_to_simulator_result_file()
        parent_dir = os.path.dirname(result_file)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
        try:
            if not os.path.exists(result_file):
                open(result_file, 'w').close()
        except Exception as e:
            print(e)

    # ------------------------------------------------------------------
    # IStopProgram
    # ------------------------------------------------------------------

    def stop_program(self) -> None:
        pass
