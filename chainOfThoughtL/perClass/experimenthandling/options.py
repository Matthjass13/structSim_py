"""
Chain-of-thought for Options:
1. Java-specific constructs: java.util.Calendar for date/time, protected fields, no-arg constructor,
   many getters/setters.
2. Python equivalents:
   - Calendar -> datetime.datetime (standard library, timezone-aware if needed).
   - No-arg constructor: __init__ with all fields defaulting to None/0.
   - Getters/setters: kept for API compatibility; also expose as plain attributes.
3. Risks/deviations:
   - Calendar has richer manipulation API than datetime; callers that relied on Calendar arithmetic
     must use timedelta instead.
   - cutoff_planning_h stores a datetime instead of a Calendar instance.
"""

from datetime import datetime
from typing import Optional


class Options:
    """Configuration options loaded from a properties file."""

    def __init__(self):
        self.path_parameters: Optional[str] = None
        self.folder_path_out: Optional[str] = None
        self.path_simulator: Optional[str] = None
        self.cutt_of_planning: int = 0
        self.cutt_of_planning_h: Optional[datetime] = None
        self.type_of_cutt_of_planning: Optional[str] = None
        self.stop_criteria: float = 0.0
        self.path_to_simulator_result_file: Optional[str] = None

    # --- Getters ---
    def get_path_parameters(self) -> Optional[str]:
        return self.path_parameters

    def get_folder_path_out(self) -> Optional[str]:
        return self.folder_path_out

    def get_path_simulator(self) -> Optional[str]:
        return self.path_simulator

    def get_cutt_of_planning(self) -> int:
        return self.cutt_of_planning

    def get_cutt_of_planning_h(self) -> Optional[datetime]:
        return self.cutt_of_planning_h

    def get_type_of_cutt_of_planning(self) -> Optional[str]:
        return self.type_of_cutt_of_planning

    def get_stop_criteria(self) -> float:
        return self.stop_criteria

    def get_path_to_simulator_result_file(self) -> Optional[str]:
        return self.path_to_simulator_result_file

    # --- Setters ---
    def set_path_parameters(self, v: str) -> None:
        self.path_parameters = v

    def set_folder_path_out(self, v: str) -> None:
        self.folder_path_out = v

    def set_path_simulator(self, v: str) -> None:
        self.path_simulator = v

    def set_cutt_of_planning(self, v: int) -> None:
        self.cutt_of_planning = v

    def set_cutt_of_planning_h(self, v: datetime) -> None:
        self.cutt_of_planning_h = v

    def set_type_of_cutt_of_planning(self, v: str) -> None:
        self.type_of_cutt_of_planning = v

    def set_stop_criteria(self, v: float) -> None:
        self.stop_criteria = v

    def set_path_to_simulator_result_file(self, v: str) -> None:
        self.path_to_simulator_result_file = v
