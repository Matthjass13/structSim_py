import os
from typing import IO, List

from experimenthandling.measure import Measure
from experimenthandling.parameter import Parameter
from interfaces.a_modifier import AModifier
from interfaces.a_simulation_system_handler import ASimulationSystemHandler


class SimpleSimulationHandler(ASimulationSystemHandler):
    """
    Concrete glue-code implementation.

    - Reads/writes parameter files in "key=value" format.
    - Extracts measures from result files in the same format.
    - start_simulation() is intentionally a no-op stub; the real call
      to MySimulator.run() would be inserted here by the integrator.
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

    def read_parameters_file(self, parameters_file_path: str) -> List[Parameter]:
        params: List[Parameter] = []
        if hasattr(parameters_file_path, "read"):
            content = parameters_file_path.read()
            if isinstance(content, bytes):
                content = content.decode("utf-8")
            lines = content.splitlines()
        else:
            with open(parameters_file_path, "r", encoding="utf-8") as fh:
                lines = fh.readlines()
        for line in lines:
            line = line.strip()
            if "=" in line:
                key, _, value = line.partition("=")
                params.append(Parameter(key.strip(), float(value.strip())))
        return params

    def read_parameters_file_from_stream(self, stream: IO) -> List[Parameter]:
        params: List[Parameter] = []
        for line in stream:
            line = line.strip() if isinstance(line, str) else line.decode("utf-8").strip()
            if "=" in line:
                key, _, value = line.partition("=")
                params.append(Parameter(key.strip(), float(value.strip())))
        return params

    def write_parameters_file(self, set_of_parameters: List[Parameter], location_to_store: str) -> None:
        file_path = os.path.join(location_to_store, "myParamFile.txt")
        with open(file_path, "w", encoding="utf-8") as fh:
            for p in set_of_parameters:
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
        # Create an empty result file so the framework can copy it
        open(result_file, "a", encoding="utf-8").close()

    def stop_program(self) -> None:
        pass
