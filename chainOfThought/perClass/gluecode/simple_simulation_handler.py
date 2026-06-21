"""
Chain-of-thought for SimpleSimulationHandler:
1. Java-specific constructs:
   - Extends ASimulationSystemHandler (abstract class with multiple interface impls).
   - Constructor overloading (default + with modifiers list).
   - Vector<Measure>, Vector<Parameter> return types.
   - InputStream overload for readParametersFile.
   - BufferedReader/InputStreamReader with UTF-8.
   - new File(...).getParentFile().mkdirs() + createNewFile() in startSimulation.
2. Python equivalents:
   - class SimpleSimulationHandler(ASimulationSystemHandler).
   - Default arg: modifiers=None in __init__, defaulting to [].
   - Return lists instead of Vector; list is the Python equivalent.
   - InputStream overload: accept file-like object via second method or isinstance check.
   - open() with encoding="utf-8".
   - Path.parent.mkdir(parents=True, exist_ok=True) + Path.touch() in start_simulation.
3. Risks/deviations:
   - Lines starting with '#' in properties files (Java Properties skips them); we skip them.
   - The Java startSimulation creates the result file but does NOT run MySimulator —
     the actual simulation call is intentionally a no-op placeholder here, matching Java.
"""

import os
from pathlib import Path
from typing import List

from experimenthandling.measure import Measure
from experimenthandling.parameter import Parameter
from interfaces.a_modifier import AModifier
from interfaces.a_simulation_system_handler import ASimulationSystemHandler


class SimpleSimulationHandler(ASimulationSystemHandler):
    """Concrete implementation of ASimulationSystemHandler for simple file-based simulations."""

    def __init__(self, modifiers: List[AModifier] = None):
        super().__init__()
        self._modifiers: List[AModifier] = modifiers if modifiers is not None else []

    def extract_measures(self, results_file_path: str) -> list:
        measures = []
        try:
            with open(results_file_path, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    if "=" in line:
                        key, _, value = line.partition("=")
                        measures.append(Measure(key.strip(), value.strip()))
        except OSError as e:
            import traceback; traceback.print_exc()
        return measures

    def initiate_modifier_list(self) -> list:
        self.list_modifier_class = self._modifiers
        return self.list_modifier_class

    def read_parameters_file(self, source) -> list:
        """Accept a file path string or a file-like object."""
        params = []
        if isinstance(source, (str, os.PathLike)):
            try:
                lines = Path(source).read_text(encoding="utf-8").splitlines()
            except OSError:
                import traceback; traceback.print_exc()
                return params
        else:
            raw = source.read()
            if isinstance(raw, bytes):
                raw = raw.decode("utf-8")
            lines = raw.splitlines()

        for line in lines:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, val = line.partition("=")
                try:
                    params.append(Parameter(key.strip(), float(val.strip())))
                except ValueError:
                    pass
        return params

    def read_parameters_file_stream(self, input_stream) -> list:
        raw = input_stream.read()
        if isinstance(raw, bytes):
            raw = raw.decode("utf-8")
        params = []
        for line in raw.splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if "=" in line:
                key, _, val = line.partition("=")
                try:
                    params.append(Parameter(key.strip(), float(val.strip())))
                except ValueError:
                    pass
        return params

    def write_parameters_file(self, set_of_parameters: list, location_to_store: str) -> None:
        out_path = os.path.join(location_to_store, "myParamFile.txt")
        try:
            with open(out_path, "w", encoding="utf-8") as f:
                for p in set_of_parameters:
                    f.write(f"{p.key}={p.value}\n")
        except Exception:
            import traceback; traceback.print_exc()

    def start_simulation(self, path_to_input_file: str) -> None:
        result_file = self.options.path_to_simulator_result_file
        Path(result_file).parent.mkdir(parents=True, exist_ok=True)
        Path(result_file).touch(exist_ok=True)

    def stop_program(self) -> None:
        pass
