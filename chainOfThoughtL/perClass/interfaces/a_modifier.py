"""
Chain-of-thought for AModifier:
1. Java-specific constructs: abstract class with abstract method applyModifier,
   two constructors, protected fields.
2. Python equivalents:
   - Abstract class -> ABC with @abstractmethod.
   - Constructor overloading -> default argument values in __init__.
   - protected fields -> _probability, _name by convention.
3. Risks/deviations:
   - Python ABC does not prevent instantiation unless all abstract methods are implemented.
   - No enforcement of 'protected'; convention only.
"""

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from experimenthandling.environment import Environment


class AModifier(ABC):
    """Abstract base class for environment modifiers."""

    def __init__(self, probability: float = 0.0, name: str = "AModifier"):
        self._probability = probability
        self._name = name

    @abstractmethod
    def apply_modifier(self, env: "Environment") -> "Environment":
        """Apply this modifier to env and return the (possibly modified) environment."""
        ...

    # Getters / setters
    def get_probability(self) -> float:
        return self._probability

    def set_probability(self, p: float) -> None:
        self._probability = p

    def get_name(self) -> str:
        return self._name

    def set_name(self, name: str) -> None:
        self._name = name

    # Expose as properties too
    @property
    def probability(self) -> float:
        return self._probability

    @probability.setter
    def probability(self, v: float) -> None:
        self._probability = v

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, v: str) -> None:
        self._name = v
