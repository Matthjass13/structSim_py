import os
from typing import IO, List

from experimenthandling.measure import Measure
from experimenthandling.parameter import Parameter
from interfaces.a_modifier import AModifier
from interfaces.a_simulation_system_handler import ASimulationSystemHandler

logger_import = __import__("logging").getLogger(__name__)


class SimpleSimulationHandler(ASimulationSystemHandler):

    def __init__(self, modifiers: List[AModifier] = None) -> None:
        super().__init__()
        self._modifiers: List[AModifier] = modifiers if modifiers is not None else []

    def extract_measures(self, results_file_path: str) -> List[Measure]:
        separator = "="
        measures_list: List[Measure] = []
        try:
            with open(results_file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.rstrip("\n")
                    pos = line.index(separator)
                    measure_key = line[:pos]
                    measure_value = line[pos + 1:]
                    measures_list.append(Measure(measure_key, measure_value))
        except OSError as e:
            import traceback
            traceback.print_exc()
        return measures_list

    def initiate_modifier_list(self) -> List[AModifier]:
        self.list_modifier_class = self._modifiers
        return self.list_modifier_class

    def read_parameters_file(self, parameters_file_path) -> List[Parameter]:
        separator = "="
        parameters_list: List[Parameter] = []
        try:
            if isinstance(parameters_file_path, str):
                f = open(parameters_file_path, "r", encoding="utf-8")
            else:
                import io
                content = parameters_file_path.read()
                if isinstance(content, bytes):
                    content = content.decode("utf-8")
                f = io.StringIO(content)

            with f:
                for line in f:
                    line = line.rstrip("\n")
                    pos = line.index(separator)
                    key = line[:pos]
                    value = float(line[pos + 1:])
                    parameters_list.append(Parameter(key, value))
        except OSError as e:
            import traceback
            traceback.print_exc()
        return parameters_list

    def write_parameters_file(self, set_of_parameters: List[Parameter], location_to_store: str) -> None:
        try:
            with open(location_to_store + "/myParamFile.txt", "w", encoding="utf-8") as f:
                for p in set_of_parameters:
                    f.write(f"{p.get_key()}={p.get_value()}\n")
        except Exception as e:
            import traceback
            traceback.print_exc()

    def start_simulation(self, path_to_input_file: str) -> None:
        result_file = self.options.path_to_simulator_result_file
        os.makedirs(os.path.dirname(result_file), exist_ok=True)
        open(result_file, "a").close()

    def stop_program(self) -> None:
        pass
