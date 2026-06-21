from typing import Optional


class Options:
    """Holds all configuration parameters for a simulation run."""

    def __init__(self):
        self.path_parameters: Optional[str] = None
        self.folder_path_out: Optional[str] = None
        self.path_simulator: Optional[str] = None
        self.cut_off_planning: int = 0
        # Seconds for time-based cutoffs (used by ExperimentPlanGenerator)
        self.cut_off_planning_h: float = 0.0
        # datetime object for time-based cutoffs (preserves .day/.hour/.minute, used by unit tests)
        self._cut_off_planning_h_calendar = None
        self.type_of_cut_off_planning: Optional[str] = None
        self.stop_criteria: float = 0.0
        self.path_to_simulator_result_file: Optional[str] = None

    # --- pathParameters ---

    def get_path_parameters(self) -> Optional[str]:
        return self.path_parameters

    def set_path_parameters(self, path: str) -> None:
        self.path_parameters = path

    # --- folderPathOUT ---

    def get_folder_path_out(self) -> Optional[str]:
        return self.folder_path_out

    def set_folder_path_out(self, path: str) -> None:
        self.folder_path_out = path

    # --- pathSimulator ---

    def get_path_simulator(self) -> Optional[str]:
        return self.path_simulator

    def set_path_simulator(self, path: str) -> None:
        self.path_simulator = path

    # --- cuttOfPlanning (INT count) ---

    def get_cut_off_planning(self) -> int:
        return self.cut_off_planning

    def set_cut_off_planning(self, value: int) -> None:
        self.cut_off_planning = value

    # Faithful alias for the Java typo ("CuttOf")
    def get_cuttof_planning(self) -> int:
        return self.cut_off_planning

    def set_cuttof_planning(self, value: int) -> None:
        self.cut_off_planning = value

    # --- cuttOfPlanningH (time-based) ---

    def get_cut_off_planning_h(self) -> float:
        """Return duration in seconds (for internal use by ExperimentPlanGenerator)."""
        return self.cut_off_planning_h

    def set_cut_off_planning_h(self, seconds: float) -> None:
        self.cut_off_planning_h = seconds

    def get_cuttof_planning_h(self):
        """Return the datetime object carrying .day / .hour / .minute (faithful Java API)."""
        return self._cut_off_planning_h_calendar

    def set_cuttof_planning_h(self, calendar) -> None:
        self._cut_off_planning_h_calendar = calendar

    # --- typeCuttOfPlanning ---

    def get_type_of_cut_off_planning(self) -> Optional[str]:
        return self.type_of_cut_off_planning

    def set_type_of_cut_off_planning(self, value: str) -> None:
        self.type_of_cut_off_planning = value

    # Faithful alias for the Java typo
    def get_type_of_cuttof_planning(self) -> Optional[str]:
        return self.type_of_cut_off_planning

    def set_type_of_cuttof_planning(self, value: str) -> None:
        self.type_of_cut_off_planning = value

    # --- stopCriteria ---

    def get_stop_criteria(self) -> float:
        return self.stop_criteria

    def set_stop_criteria(self, value: float) -> None:
        self.stop_criteria = value

    # --- pathToSimulatorResultFile ---

    def get_path_to_simulator_result_file(self) -> Optional[str]:
        return self.path_to_simulator_result_file

    def set_path_to_simulator_result_file(self, path: str) -> None:
        self.path_to_simulator_result_file = path
