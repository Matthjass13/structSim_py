from __future__ import annotations
from typing import List
from experimenthandling.parameter import Parameter


class Environment:
    def __init__(self, id: int = 1, set_of_parameters=None, probability: float = 1.0, other: "Environment" = None):
        import copy
        if isinstance(set_of_parameters, Environment):
            other = set_of_parameters
            set_of_parameters = None
        if other is not None:
            self.id: int = id
            self.set_of_parameters: List[Parameter] = copy.deepcopy(other.set_of_parameters)
            self.probability: float = other.probability
            self.trace: List[str] = list(other.trace)
            self.path_save_result: str = ""
        else:
            self.id = id
            self.set_of_parameters: List[Parameter] = set_of_parameters if set_of_parameters is not None else []
            self.probability = probability
            self.trace: List[str] = []
            self.path_save_result: str = ""

    def get_id(self) -> int:
        return self.id

    def get_set_of_parameters(self) -> List[Parameter]:
        return self.set_of_parameters

    def set_set_of_parameters(self, set_of_parameters: List[Parameter]) -> None:
        self.set_of_parameters = set_of_parameters

    def get_probability(self) -> float:
        return self.probability

    def set_probability(self, probability: float) -> None:
        self.probability = probability

    def get_path_save_result(self) -> str:
        return self.path_save_result

    def set_path_save_result(self, path_save_result: str) -> None:
        self.path_save_result = path_save_result

    def to_string_modifier(self) -> str:
        result = ""
        for s in self.trace:
            result += "   " + s
        return f"Simulation ID : {self.id}\t Probability : {self.probability}\t Modifier implemented : {result}"

    def get_trace(self) -> List[str]:
        return self.trace

    def set_trace(self, trace: List[str]) -> None:
        self.trace = trace

    def __lt__(self, other: "Environment") -> bool:
        return self.probability < other.probability

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Environment):
            return NotImplemented
        return self.probability == other.probability

    def __gt__(self, other: "Environment") -> bool:
        return self.probability > other.probability

    def compare_to(self, other: "Environment") -> int:
        if self.probability < other.probability:
            return -1
        elif self.probability > other.probability:
            return 1
        return 0
