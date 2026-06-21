class Options:
    """Class to specify the options to run the simulation."""

    def __init__(self):
        self.path_parameters: str = None
        self.folder_path_out: str = None
        self.path_simulator: str = None
        self.cut_off_planning: int = 0
        # Stores the raw integer value (days / hours / minutes) for time-based cutoffs
        self.cut_off_planning_h: int = 0
        self.type_of_cut_off_planning: str = None
        self.stop_criteria: float = 0.0
        self.path_to_simulator_result_file: str = None

    def get_path_parameters(self) -> str:
        return self.path_parameters

    def set_path_parameters(self, path_parameters: str) -> None:
        self.path_parameters = path_parameters

    def get_folder_path_out(self) -> str:
        return self.folder_path_out

    def set_folder_path_out(self, folder_path_out: str) -> None:
        self.folder_path_out = folder_path_out

    def get_path_simulator(self) -> str:
        return self.path_simulator

    def set_path_simulator(self, path_simulator: str) -> None:
        self.path_simulator = path_simulator

    def get_cut_off_planning(self) -> int:
        return self.cut_off_planning

    def set_cut_off_planning(self, cut_off_planning: int) -> None:
        self.cut_off_planning = cut_off_planning

    def get_cut_off_planning_h(self) -> int:
        return self.cut_off_planning_h

    def set_cut_off_planning_h(self, cut_off_planning_h: int) -> None:
        self.cut_off_planning_h = cut_off_planning_h

    def get_type_of_cut_off_planning(self) -> str:
        return self.type_of_cut_off_planning

    def set_type_of_cut_off_planning(self, type_of_cut_off_planning: str) -> None:
        self.type_of_cut_off_planning = type_of_cut_off_planning

    def get_type_of_cuttof_planning(self):
        return self.type_of_cut_off_planning

    def get_cuttof_planning(self):
        return self.cut_off_planning

    def get_cuttof_planning_h(self):
        import datetime
        type_ = self.type_of_cut_off_planning
        val = self.cut_off_planning_h
        if type_ == "DAY":
            return datetime.datetime(1, 1, val)
        elif type_ == "HOURS":
            return datetime.datetime(1, 1, 1, val)
        elif type_ == "MINUTES":
            return datetime.datetime(1, 1, 1, 0, val)
        return None

    def get_stop_criteria(self) -> float:
        return self.stop_criteria

    def set_stop_criteria(self, stop_criteria: float) -> None:
        self.stop_criteria = stop_criteria

    def get_path_to_simulator_result_file(self) -> str:
        return self.path_to_simulator_result_file

    def set_path_to_simulator_result_file(self, path_to_simulator_result_file: str) -> None:
        self.path_to_simulator_result_file = path_to_simulator_result_file
