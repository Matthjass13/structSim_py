from typing import List
from experimenthandling.parameter import Parameter


class Environment:
    """
    An environment is the state of the simulation at instant T.
    Contains an ID, a list of Parameters, and a probability that this state can occur.
    """

    def __init__(self, id: int = 1, set_of_parameters: List[Parameter] = None, probability: float = 1.0):
        if isinstance(set_of_parameters, Environment):
            source = set_of_parameters
            self.id = id
            self.set_of_parameters = [Parameter.copy(p) for p in source.set_of_parameters]
            self.probability = source.probability
            self.path_save_result = None
            self.trace = list(source.trace)
            return
        self.id = id
        self.set_of_parameters: List[Parameter] = set_of_parameters if set_of_parameters is not None else []
        self.probability = probability
        self.path_save_result: str = None
        self.trace: List[str] = []

    @classmethod
    def copy_from(cls, id: int, e: "Environment") -> "Environment":
        """Create a new Environment by copying another."""
        instance = cls.__new__(cls)
        instance.id = id
        instance.set_of_parameters = [Parameter.copy(p) for p in e.set_of_parameters]
        instance.probability = e.probability
        instance.path_save_result = None
        instance.trace = list(e.trace)
        return instance

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

    def get_trace(self) -> List[str]:
        return self.trace

    def set_trace(self, trace: List[str]) -> None:
        self.trace = trace

    def to_string_modifier(self) -> str:
        result = ""
        for s in self.trace:
            result += "   " + s
        return f"Simulation ID : {self.id}\t Probability : {self.probability}\t Modifier implemented : {result}"

    def compare_to(self, other: "Environment") -> int:
        if self.probability < other.probability:
            return -1
        elif self.probability > other.probability:
            return 1
        return 0

    def __lt__(self, other: "Environment") -> bool:
        return self.probability < other.probability

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Environment):
            return False
        return self.probability == other.probability

    def __str__(self) -> str:
        return self.to_string_modifier()
