from typing import Optional


class Options:
    """Holds all configuration parameters for a simulation run."""

    def __init__(self):
        self.path_parameters: Optional[str] = None
        self.folder_path_out: Optional[str] = None
        self.path_simulator: Optional[str] = None
        self.cut_off_planning: int = 0
        # Stores a duration in seconds for time-based cut-offs
        self.cut_off_planning_h: float = 0.0
        self.type_of_cut_off_planning: Optional[str] = None
        self.stop_criteria: float = 0.0
        self.path_to_simulator_result_file: Optional[str] = None
        self._cuttof_raw_value = 0

    def get_type_of_cuttof_planning(self):
        return self.type_of_cut_off_planning

    def get_cuttof_planning(self):
        return self.cut_off_planning

    def set_cuttof_raw_value(self, value):
        self._cuttof_raw_value = value

    def get_cuttof_planning_h(self):
        import datetime
        type_ = self.type_of_cut_off_planning
        val = self._cuttof_raw_value
        if type_ == "DAY":
            return datetime.datetime(1, 1, val)
        elif type_ == "HOURS":
            return datetime.datetime(1, 1, 1, val)
        elif type_ == "MINUTES":
            return datetime.datetime(1, 1, 1, 0, val)
        return None

    def get_path_parameters(self) -> Optional[str]:
        return self.path_parameters

    def set_path_parameters(self, path: str) -> None:
        self.path_parameters = path

    def get_folder_path_out(self) -> Optional[str]:
        return self.folder_path_out

    def set_folder_path_out(self, path: str) -> None:
        self.folder_path_out = path

    def get_path_simulator(self) -> Optional[str]:
        return self.path_simulator

    def set_path_simulator(self, path: str) -> None:
        self.path_simulator = path

    def get_cut_off_planning(self) -> int:
        return self.cut_off_planning

    def set_cut_off_planning(self, value: int) -> None:
        self.cut_off_planning = value

    def get_cut_off_planning_h(self) -> float:
        return self.cut_off_planning_h

    def set_cut_off_planning_h(self, seconds: float) -> None:
        self.cut_off_planning_h = seconds

    def get_type_of_cut_off_planning(self) -> Optional[str]:
        return self.type_of_cut_off_planning

    def set_type_of_cut_off_planning(self, value: str) -> None:
        self.type_of_cut_off_planning = value

    def get_stop_criteria(self) -> float:
        return self.stop_criteria

    def set_stop_criteria(self, value: float) -> None:
        self.stop_criteria = value

    def get_path_to_simulator_result_file(self) -> Optional[str]:
        return self.path_to_simulator_result_file

    def set_path_to_simulator_result_file(self, path: str) -> None:
        self.path_to_simulator_result_file = path
