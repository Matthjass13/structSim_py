from typing import List, Optional
from experimenthandling.parameter import Parameter


class Environment:
    """
    State of the simulation at instant T.

    Implements __lt__ so that Python's heapq / PriorityQueue can order
    environments by ascending probability — replacing Java's Comparable<Environment>.
    """

    def __init__(
        self,
        id: int = 1,
        set_of_parameters: Optional[List[Parameter]] = None,
        probability: float = 1.0,
        copy_from: Optional["Environment"] = None,
    ):
        import copy as _copy
        if isinstance(set_of_parameters, Environment):
            copy_from = set_of_parameters
            set_of_parameters = None
        if copy_from is not None:
            self.id = id
            self.set_of_parameters = _copy.deepcopy(copy_from.set_of_parameters)
            self.probability = copy_from.probability
            self.trace: List[str] = list(copy_from.trace)
        else:
            self.id = id
            self.set_of_parameters: List[Parameter] = set_of_parameters if set_of_parameters is not None else []
            self.probability = probability
            self.trace: List[str] = []

        self.path_save_result: Optional[str] = None

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

    def get_path_save_result(self) -> Optional[str]:
        return self.path_save_result

    def set_path_save_result(self, path_save_result: str) -> None:
        self.path_save_result = path_save_result

    def get_trace(self) -> List[str]:
        return self.trace

    def set_trace(self, trace: List[str]) -> None:
        self.trace = trace

    def to_string_modifier(self) -> str:
        result = "".join(f"   {s}" for s in self.trace)
        return f"Simulation ID : {self.id}\t Probability : {self.probability}\t Modifier implemented : {result}"

    # Priority queue ordering: lower probability → higher priority (ascending order)
    def __lt__(self, other: "Environment") -> bool:
        return self.probability < other.probability

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Environment):
            return False
        return self.probability == other.probability

    def compare_to(self, other: "Environment") -> int:
        if self.probability < other.probability:
            return -1
        elif self.probability > other.probability:
            return 1
        return 0

    def __repr__(self) -> str:
        return f"Environment(id={self.id}, probability={self.probability})"
