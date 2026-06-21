import datetime
from typing import Optional


class Options:
    def __init__(self) -> None:
        self.path_parameters: str = ""
        self.folder_path_out: str = ""
        self.path_simulator: str = ""
        self._cuttof_planning: int = 0
        self.cut_off_planning: int = 0  # backward compat alias
        self._cuttof_planning_h: Optional[datetime.datetime] = None
        self._type_of_cuttof_planning: str = ""
        self.type_of_cut_off_planning: str = ""  # backward compat alias
        self.stop_criteria: float = 0.0
        self.path_to_simulator_result_file: str = ""

    def get_path_parameters(self) -> str:
        return self.path_parameters

    def set_path_parameters(self, v: str) -> None:
        self.path_parameters = v

    def get_folder_path_out(self) -> str:
        return self.folder_path_out

    def set_folder_path_out(self, v: str) -> None:
        self.folder_path_out = v

    def get_path_simulator(self) -> str:
        return self.path_simulator

    def set_path_simulator(self, v: str) -> None:
        self.path_simulator = v

    def get_path_to_simulator_result_file(self) -> str:
        return self.path_to_simulator_result_file

    def set_path_to_simulator_result_file(self, v: str) -> None:
        self.path_to_simulator_result_file = v

    def get_type_of_cuttof_planning(self) -> str:
        return self._type_of_cuttof_planning

    def set_type_of_cuttof_planning(self, v: str) -> None:
        self._type_of_cuttof_planning = v
        self.type_of_cut_off_planning = v  # backward compat for start_program.py

    def get_cuttof_planning(self) -> int:
        return self._cuttof_planning

    def set_cuttof_planning(self, v: int) -> None:
        self._cuttof_planning = v
        self.cut_off_planning = v  # backward compat

    def get_cuttof_planning_h(self) -> Optional[datetime.datetime]:
        return self._cuttof_planning_h

    def set_cuttof_planning_h(self, v: Optional[datetime.datetime]) -> None:
        self._cuttof_planning_h = v

    def get_stop_criteria(self) -> float:
        return self.stop_criteria

    def set_stop_criteria(self, v: float) -> None:
        self.stop_criteria = v
