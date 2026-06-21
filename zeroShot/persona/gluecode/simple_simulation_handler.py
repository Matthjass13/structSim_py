import io
import os
from typing import List, Union

from experimenthandling.measure import Measure
from experimenthandling.parameter import Parameter
from interfaces.a_modifier import AModifier
from interfaces.a_simulation_system_handler import ASimulationSystemHandler


class SimpleSimulationHandler(ASimulationSystemHandler):
    """
    Concrete glue-code implementation.

    - Reads/writes parameter files in "key=value" format.
    - read_parameters_file() accepts either a file path (str) or a binary/text stream.
    - Extracts measures from result files in the same format.
    - start_simulation() creates an empty result file so the framework can copy it.
    """

    def __init__(self, modifiers: List[AModifier] = None):
        super().__init__()
        self._modifiers: List[AModifier] = modifiers or []

    # ------------------------------------------------------------------
    # IManageModifier
    # ------------------------------------------------------------------

    def initiate_modifier_list(self) -> List[AModifier]:
        self.list_modifier_class = self._modifiers
        return self.list_modifier_class

    # ------------------------------------------------------------------
    # IManageParametersFile
    # ------------------------------------------------------------------

    def _parse_params_from_lines(self, lines) -> List[Parameter]:
        params: List[Parameter] = []
        for line in lines:
            if isinstance(line, bytes):
                line = line.decode("utf-8")
            line = line.strip()
            if "=" in line:
                key, _, value = line.partition("=")
                params.append(Parameter(key.strip(), float(value.strip())))
        return params

    def read_parameters_file(self, source: Union[str, "io.IOBase"]) -> List[Parameter]:
        """
        Accept either a file path (str) or any stream (BytesIO, text file, binary file).
        Mirrors both Java overloads: readParametersFile(String) and readParametersFile(InputStream).
        """
        if isinstance(source, str):
            with open(source, "r", encoding="utf-8") as fh:
                return self._parse_params_from_lines(fh)
        else:
            # Stream: BytesIO, binary file, or text file
            content = source.read()
            if isinstance(content, bytes):
                lines = content.decode("utf-8").splitlines()
            else:
                lines = content.splitlines()
            return self._parse_params_from_lines(lines)

    def read_parameters_file_from_stream(self, stream) -> List[Parameter]:
        return self.read_parameters_file(stream)

    def write_parameters_file(self, set_of_parameters: List[Parameter], location_to_store: str) -> None:
        file_path = os.path.join(location_to_store, "myParamFile.txt")
        with open(file_path, "w", encoding="utf-8") as fh:
            for p in set_of_parameters:
                # Always write as float (e.g. 10.0 not 10) to match Java double serialisation
                fh.write(f"{p.get_key()}={float(p.get_value())}\n")

    # ------------------------------------------------------------------
    # IExtractMeasures
    # ------------------------------------------------------------------

    def extract_measures(self, results_file_path: str) -> List[Measure]:
        measures: List[Measure] = []
        with open(results_file_path, "r", encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if "=" in line:
                    key, _, value = line.partition("=")
                    measures.append(Measure(key.strip(), value.strip()))
        return measures

    # ------------------------------------------------------------------
    # IStartSimulation / IStopProgram
    # ------------------------------------------------------------------

    def start_simulation(self, path_to_input_file: str) -> None:
        result_file = self.options.get_path_to_simulator_result_file()
        os.makedirs(os.path.dirname(result_file), exist_ok=True)
        open(result_file, "a", encoding="utf-8").close()

    def stop_program(self) -> None:
        pass
