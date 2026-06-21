from datetime import datetime


class Options:
    def __init__(self):
        self.path_parameters: str = None
        self.folder_path_out: str = None
        self.path_simulator: str = None
        self.cutt_of_planning: int = 0
        self.cutt_of_planning_h: datetime = None
        self.type_of_cutt_of_planning: str = None
        self.stop_criteria: float = 0.0
        self.path_to_simulator_result_file: str = None

    def get_path_parameters(self) -> str:
        return self.path_parameters

    def set_path_parameters(self, path_parameters: str):
        self.path_parameters = path_parameters

    def get_folder_path_out(self) -> str:
        return self.folder_path_out

    def set_folder_path_out(self, folder_path_out: str):
        self.folder_path_out = folder_path_out

    def get_path_simulator(self) -> str:
        return self.path_simulator

    def set_path_simulator(self, path_simulator: str):
        self.path_simulator = path_simulator

    def get_cutt_of_planning(self) -> int:
        return self.cutt_of_planning

    def set_cutt_of_planning(self, cutt_of_planning: int):
        self.cutt_of_planning = cutt_of_planning

    def get_cutt_of_planning_h(self) -> datetime:
        return self.cutt_of_planning_h

    def set_cutt_of_planning_h(self, cutt_of_planning_h: datetime):
        self.cutt_of_planning_h = cutt_of_planning_h

    def get_type_of_cutt_of_planning(self) -> str:
        return self.type_of_cutt_of_planning

    def set_type_of_cutt_of_planning(self, type_of_cutt_of_planning: str):
        self.type_of_cutt_of_planning = type_of_cutt_of_planning

    def get_stop_criteria(self) -> float:
        return self.stop_criteria

    def set_stop_criteria(self, stop_criteria: float):
        self.stop_criteria = stop_criteria

    def get_type_of_cuttof_planning(self) -> str:
        return self.type_of_cutt_of_planning

    def get_cuttof_planning(self) -> int:
        return self.cutt_of_planning

    def get_cuttof_planning_h(self) -> datetime:
        return self.cutt_of_planning_h

    def get_path_to_simulator_result_file(self) -> str:
        return self.path_to_simulator_result_file

    def set_path_to_simulator_result_file(self, path_to_simulator_result_file: str):
        self.path_to_simulator_result_file = path_to_simulator_result_file
