import os
from io import IOBase
from typing import IO, List, Union

from experimenthandling.Measure import Measure
from experimenthandling.Parameter import Parameter
from interfaces.AModifier import AModifier
from interfaces.ASimulationSystemHandler import ASimulationSystemHandler


class SimpleSimulationHandler(ASimulationSystemHandler):
    """
    Concrete glue-code handler used by the default Simulation entry point.

    read_parameters_file accepts either a path (str) or a binary/text stream,
    which is needed when the caller loads the file from package resources.
    """

    def __init__(self, modifiers: List[AModifier] = None):
        super().__init__()
        self._modifiers: List[AModifier] = modifiers if modifiers is not None else []

    # ------------------------------------------------------------------
    # IExtractMeasures
    # ------------------------------------------------------------------

    def extract_measures(self, results_file_path: str) -> List[Measure]:
        measures: List[Measure] = []
        try:
            with open(results_file_path, "r", encoding="utf-8") as fh:
                for line in fh:
                    line = line.rstrip("\r\n")
                    if not line:
                        continue
                    pos = line.index("=")
                    measures.append(Measure(line[:pos], line[pos + 1:]))
        except (OSError, ValueError) as e:
            pass
        return measures

    # ------------------------------------------------------------------
    # IManageModifier
    # ------------------------------------------------------------------

    def initiate_modifier_list(self) -> List[AModifier]:
        self.list_modifier_class = self._modifiers
        return self.list_modifier_class

    # ------------------------------------------------------------------
    # IManageParametersFile
    # ------------------------------------------------------------------

    def read_parameters_file(self, source: Union[str, IO]) -> List[Parameter]:
        params: List[Parameter] = []
        try:
            if isinstance(source, str):
                fh = open(source, "r", encoding="utf-8")
                close_after = True
            else:
                if isinstance(source, (bytes, bytearray)):
                    lines = source.decode("utf-8").splitlines()
                    for line in lines:
                        line = line.strip()
                        if not line:
                            continue
                        pos = line.index("=")
                        params.append(Parameter(line[:pos].strip(), float(line[pos + 1:].strip())))
                    return params
                # file-like object
                raw = source.read()
                if isinstance(raw, bytes):
                    raw = raw.decode("utf-8")
                for line in raw.splitlines():
                    line = line.strip()
                    if not line:
                        continue
                    pos = line.index("=")
                    params.append(Parameter(line[:pos].strip(), float(line[pos + 1:].strip())))
                return params

            with fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    pos = line.index("=")
                    params.append(Parameter(line[:pos].strip(), float(line[pos + 1:].strip())))
        except (OSError, ValueError):
            pass
        return params

    def write_parameters_file(self, set_of_parameters: List[Parameter], location_to_store: str) -> None:
        path = os.path.join(location_to_store, "myParamFile.txt")
        with open(path, "w", encoding="utf-8") as fh:
            for p in set_of_parameters:
                fh.write(f"{p.get_key()}={float(p.get_value())}\n")

    # ------------------------------------------------------------------
    # IStartSimulation
    # ------------------------------------------------------------------

    def start_simulation(self, path_to_input_file: str) -> None:
        result_file = self.options.get_path_to_simulator_result_file()
        os.makedirs(os.path.dirname(result_file), exist_ok=True)
        # Create/truncate the result file so the simulator output is fresh
        open(result_file, "w").close()

    # ------------------------------------------------------------------
    # IStopProgram
    # ------------------------------------------------------------------

    def stop_program(self) -> None:
        pass
