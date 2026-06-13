from abc import ABC, abstractmethod


class AModifier(ABC):
    """Abstract class defining a method to modify the value of a parameter."""

    def __init__(self, probability: float = 0.0, name: str = "AModifier"):
        self.probability = probability
        self.name = name

    @abstractmethod
    def apply_modifier(self, env):
        """
        Apply an algorithm to modify parameters in the given environment.
        Returns the modified environment.
        """
        pass

    def get_probability(self) -> float:
        return self.probability

    def set_probability(self, probability: float) -> None:
        self.probability = probability

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name
