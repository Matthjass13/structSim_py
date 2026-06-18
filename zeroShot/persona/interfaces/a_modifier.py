from abc import ABC, abstractmethod


class AModifier(ABC):
    """
    Abstract base for all parameter modifiers.
    Subclasses implement apply_modifier() to transform an Environment's parameters.
    """

    def __init__(self, probability: float = 0.0, name: str = "AModifier"):
        self.probability = probability
        self.name = name

    @abstractmethod
    def apply_modifier(self, env) -> object:
        """Apply this modifier to the given environment and return the modified environment."""
        ...

    def get_probability(self) -> float:
        return self.probability

    def set_probability(self, probability: float) -> None:
        self.probability = probability

    def get_name(self) -> str:
        return self.name

    def set_name(self, name: str) -> None:
        self.name = name
