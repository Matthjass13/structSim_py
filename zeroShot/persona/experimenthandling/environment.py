from typing import List
from experimenthandling.parameter import Parameter


class Environment:
    """
    Represents the state of the simulation at a given instant T.
    Holds an ID, a list of parameters, a probability, and a modifier trace.
    Comparable by probability for priority-queue ordering.
    """

    def __init__(self, env_id: int, set_of_parameters: List[Parameter], probability: float):
        self.id = env_id
        self.set_of_parameters: List[Parameter] = set_of_parameters
        self.probability = probability
        self.path_save_result: str = ""
        self.trace: List[str] = []

    @classmethod
    def copy_from(cls, new_id: int, source: "Environment") -> "Environment":
        """Create a deep copy of an existing environment with a new ID."""
        params = [Parameter.copy_from(p) for p in source.set_of_parameters]
        env = cls(new_id, params, source.probability)
        env.trace = list(source.trace)
        return env

    @classmethod
    def default(cls) -> "Environment":
        return cls(1, [], 1.0)

    # --- accessors ---

    def get_id(self) -> int:
        return self.id

    def get_set_of_parameters(self) -> List[Parameter]:
        return self.set_of_parameters

    def set_set_of_parameters(self, params: List[Parameter]) -> None:
        self.set_of_parameters = params

    def get_probability(self) -> float:
        return self.probability

    def set_probability(self, probability: float) -> None:
        self.probability = probability

    def get_path_save_result(self) -> str:
        return self.path_save_result

    def set_path_save_result(self, path: str) -> None:
        self.path_save_result = path

    def get_trace(self) -> List[str]:
        return self.trace

    def set_trace(self, trace: List[str]) -> None:
        self.trace = trace

    def to_string_modifier(self) -> str:
        modifiers = "   ".join(self.trace)
        return (
            f"Simulation ID : {self.id}\t "
            f"Probability : {self.probability}\t "
            f"Modifier implemented :    {modifiers}"
        )

    # --- ordering by probability (ascending) ---

    def __lt__(self, other: "Environment") -> bool:
        return self.probability < other.probability

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Environment):
            return NotImplemented
        return self.probability == other.probability

    def __repr__(self) -> str:
        return f"Environment(id={self.id}, probability={self.probability})"
