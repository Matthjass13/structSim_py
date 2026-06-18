from datetime import timedelta
from typing import Optional


class Options:
    def __init__(self) -> None:
        self.path_parameters: str = ""
        self.folder_path_out: str = ""
        self.path_simulator: str = ""
        self.cut_off_planning: int = 0
        self.cut_off_planning_h: Optional[timedelta] = None
        self.type_of_cut_off_planning: str = ""
        self.stop_criteria: float = 0.0
        self.path_to_simulator_result_file: str = ""
