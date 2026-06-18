from __future__ import annotations
from typing import List
from experimenthandling.parameter import Parameter


class Environment:
    def __init__(self, id: int = 1, set_of_parameters: list = None, probability: float = 1.0,
                 copy_from: "Environment" = None):
        if copy_from is not None:
            self.id = id
            self.set_of_parameters = [Parameter(p.key, p.value) for p in copy_from.set_of_parameters]
            self.probability = copy_from.probability
            self.trace: List[str] = list(copy_from.trace)
            self.path_save_result: str = None
        else:
            self.id = id
            self.set_of_parameters = set_of_parameters if set_of_parameters is not None else []
            self.probability = probability
            self.trace: List[str] = []
            self.path_save_result: str = None

    def get_id(self) -> int:
        return self.id

    def get_set_of_parameters(self) -> list:
        return self.set_of_parameters

    def set_set_of_parameters(self, set_of_parameters: list):
        self.set_of_parameters = set_of_parameters

    def get_probability(self) -> float:
        return self.probability

    def set_probability(self, probability: float):
        self.probability = probability

    def get_path_save_result(self) -> str:
        return self.path_save_result

    def set_path_save_result(self, path_save_result: str):
        self.path_save_result = path_save_result

    def get_trace(self) -> List[str]:
        return self.trace

    def set_trace(self, trace: List[str]):
        self.trace = trace

    def to_string_modifier(self) -> str:
        result = "   ".join(self.trace)
        return f"Simulation ID : {self.id}\t Probability : {self.probability}\t Modifier implemented : {result}"

    def __lt__(self, other: "Environment") -> bool:
        return self.probability < other.probability

    def __eq__(self, other) -> bool:
        if not isinstance(other, Environment):
            return False
        return self.probability == other.probability

    def __repr__(self) -> str:
        return f"Environment(id={self.id}, probability={self.probability})"
