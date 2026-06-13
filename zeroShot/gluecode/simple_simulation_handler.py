import logging
import os
from typing import IO, List, Union

from experimenthandling.measure import Measure
from experimenthandling.parameter import Parameter
from interfaces.a_simulation_system_handler import ASimulationSystemHandler

logger = logging.getLogger(__name__)


class SimpleSimulationHandler(ASimulationSystemHandler):
    """Concrete implementation of ASimulationSystemHandler for simple simulations."""

    def __init__(self, modifiers: List = None):
        super().__init__()
        self._modifiers: List = modifiers if modifiers is not None else []

    def extract_measures(self, results_file_path: str) -> List[Measure]:
        separator = "="
        measures_list: List[Measure] = []
        try:
            with open(results_file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.rstrip("\n")
                    if not line:
                        continue
                    pos = line.index(separator)
                    measure_key = line[:pos]
                    measure_value = line[pos + 1:]
                    measures_list.append(Measure(measure_key, measure_value))
        except IOError as e:
            import traceback
            traceback.print_exc()
        return measures_list

    def initiate_modifier_list(self) -> List:
        self.list_modifier_class = self._modifiers
        return self.list_modifier_class

    def read_parameters_file(self, source: Union[str, IO]) -> List[Parameter]:
        """Read parameters from a file path or file-like object."""
        separator = "="
        parameters_list: List[Parameter] = []

        try:
            if isinstance(source, str):
                f = open(source, "r", encoding="utf-8")
                lines = f.readlines()
                f.close()
            else:
                lines = source.readlines()
                if lines and isinstance(lines[0], bytes):
                    lines = [l.decode("utf-8") for l in lines]

            for line in lines:
                line = line.rstrip("\n")
                if not line:
                    continue
                pos = line.index(separator)
                key = line[:pos]
                value = float(line[pos + 1:])
                parameters_list.append(Parameter(key, value))
        except IOError as e:
            import traceback
            traceback.print_exc()

        return parameters_list

    def write_parameters_file(self, set_of_parameters: List[Parameter], location_to_store: str) -> None:
        file_path = os.path.join(location_to_store, "myParamFile.txt")
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                for p in set_of_parameters:
                    f.write(f"{p.get_key()}={p.get_value()}\n")
        except Exception as e:
            import traceback
            traceback.print_exc()

    def start_simulation(self, path_to_input_file: str) -> None:
        result_file = self.options.get_path_to_simulator_result_file()
        parent_dir = os.path.dirname(result_file)
        if parent_dir:
            os.makedirs(parent_dir, exist_ok=True)
        try:
            open(result_file, "a").close()
        except IOError as e:
            import traceback
            traceback.print_exc()

    def stop_program(self) -> None:
        pass
