from abc import ABC, abstractmethod
from experimenthandling.environment import Environment


class AModifier(ABC):
    """
    Abstract base class for parameter modifiers.

    Java abstract class → Python ABC. The single abstract method applyModifier
    maps to apply_modifier (snake_case).
    """

    def __init__(self, probability: float = 0.0, name: str = "AModifier"):
        self.probability = probability
        self.name = name

    @abstractmethod
    def apply_modifier(self, env: Environment) -> Environment:
        """Apply this modifier to the environment and return the modified environment."""

    def get_probability(self) -> float:
        return self.probability

    def set_probability(self, probability: float) -> None:
        self.probability = probability

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name
