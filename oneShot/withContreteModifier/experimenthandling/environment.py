from experimenthandling.parameter import Parameter


class Environment:

    def __init__(self, id: int = 1, set_of_parameters: list = None, probability: float = 1.0):
        self.id = id
        self.set_of_parameters: list[Parameter] = set_of_parameters if set_of_parameters is not None else []
        self.probability = probability
        self.path_save_result: str = ""
        self.trace: list[str] = []

    @classmethod
    def from_environment(cls, id: int, e: 'Environment') -> 'Environment':
        env = cls(id)
        env.set_of_parameters = [Parameter.from_parameter(p) for p in e.set_of_parameters]
        env.probability = e.probability
        env.trace = list(e.trace)
        return env

    def get_id(self) -> int:
        return self.id

    def get_set_of_parameters(self) -> list:
        return self.set_of_parameters

    def set_set_of_parameters(self, set_of_parameters: list) -> None:
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
        result = "".join(f"   {s}" for s in self.trace)
        return (
            f"Simulation ID : {self.id}\t "
            f"Probability : {self.probability}\t "
            f"Modifier implemented : {result}"
        )

    def get_trace(self) -> list[str]:
        return self.trace

    def set_trace(self, trace: list[str]) -> None:
        self.trace = trace

    def __lt__(self, other: 'Environment') -> bool:
        return self.probability < other.probability

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Environment):
            return NotImplemented
        return self.probability == other.probability

    def __le__(self, other: 'Environment') -> bool:
        return self.probability <= other.probability

    def __gt__(self, other: 'Environment') -> bool:
        return self.probability > other.probability

    def __ge__(self, other: 'Environment') -> bool:
        return self.probability >= other.probability
