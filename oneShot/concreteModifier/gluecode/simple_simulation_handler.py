import logging
import os
from pathlib import Path

from experimenthandling.measure import Measure
from experimenthandling.parameter import Parameter
from interfaces.a_simulation_system_handler import ASimulationSystemHandler

logger = logging.getLogger(__name__)


class SimpleSimulationHandler(ASimulationSystemHandler):

    def __init__(self, modifiers: list = None):
        super().__init__()
        self._modifiers: list = modifiers if modifiers is not None else []

    def extract_measures(self, results_file_path: str) -> list:
        separator = "="
        measures_list: list[Measure] = []
        try:
            with open(results_file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.rstrip("\n")
                    pos = line.index(separator)
                    measure_key = line[:pos]
                    measure_value = line[pos + 1:]
                    measures_list.append(Measure(measure_key, measure_value))
        except IOError as e:
            logger.error(str(e))
        return measures_list

    def initiate_modifier_list(self) -> list:
        self.list_modifier_class = self._modifiers
        return self.list_modifier_class

    def read_parameters_file(self, parameters_file_path: str) -> list:
        if hasattr(parameters_file_path, "read"):
            return self.read_parameters_file_from_stream(parameters_file_path)
        separator = "="
        parameters_list: list[Parameter] = []
        try:
            with open(parameters_file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.rstrip("\n")
                    if not line:
                        continue
                    pos = line.index(separator)
                    key = line[:pos]
                    value = float(line[pos + 1:])
                    parameters_list.append(Parameter(key, value))
        except IOError as e:
            logger.error(str(e))
        return parameters_list

    def read_parameters_file_from_stream(self, input_stream) -> list:
        separator = "="
        parameters_list: list[Parameter] = []
        try:
            for line in input_stream:
                if isinstance(line, bytes):
                    line = line.decode("utf-8")
                line = line.rstrip("\n")
                if not line:
                    continue
                pos = line.index(separator)
                key = line[:pos]
                value = float(line[pos + 1:])
                parameters_list.append(Parameter(key, value))
        except IOError as e:
            logger.error(str(e))
        return parameters_list

    def write_parameters_file(self, set_of_parameters: list, location_to_store: str) -> None:
        try:
            with open(location_to_store + "/myParamFile.txt", "w", encoding="utf-8") as f:
                for p in set_of_parameters:
                    f.write(f"{p.get_key()}={float(p.get_value())}\n")
        except Exception as e:
            logger.error(str(e))

    def start_simulation(self, path_to_input_file: str) -> None:
        result_file = self.options.get_path_to_simulator_result_file()
        os.makedirs(os.path.dirname(result_file), exist_ok=True)
        Path(result_file).touch()

    def stop_program(self) -> None:
        pass
