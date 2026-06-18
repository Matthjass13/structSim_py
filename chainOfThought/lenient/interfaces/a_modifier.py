from abc import ABC, abstractmethod


class AModifier(ABC):
    def __init__(self, probability: float = 0.0, name: str = "AModifier"):
        self.probability = probability
        self.name = name

    @abstractmethod
    def apply_modifier(self, env):
        pass

    def get_probability(self) -> float:
        return self.probability

    def set_probability(self, probability: float):
        self.probability = probability

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str):
        self.name = name
