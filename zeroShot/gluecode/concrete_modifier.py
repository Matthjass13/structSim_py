import logging
from typing import List

from interfaces.a_modifier import AModifier

logger = logging.getLogger(__name__)


class ConcreteModifier(AModifier):
    """A concrete implementation of AModifier that applies arithmetic operations to parameters."""

    def __init__(self, key_to_change: str = None, operator: str = None, delta: float = 0.0, probability: float = 1.0):
        if key_to_change is None and operator is None:
            super().__init__(0.0, "AModifier")
            self.key_to_change = None
            self.operator = None
            self.delta = 0.0
        else:
            super().__init__(probability, operator + str(delta))
            self.key_to_change = key_to_change
            self.probability = probability
            self.operator = operator
            self.delta = delta

    @classmethod
    def with_default_probability(cls, key_to_change: str, operator: str, delta: float) -> "ConcreteModifier":
        return cls(key_to_change, operator, delta, 1.0)

    @classmethod
    def from_delta(cls, delta: float) -> "ConcreteModifier":
        return cls("val1", "*", delta, delta)

    def apply_modifier(self, env):
        params = env.get_set_of_parameters()
        for p in params:
            logger.debug(f"param={p.get_key()} keyToChange={self.key_to_change}")
            if p.get_key() == self.key_to_change:
                if self.operator == "+":
                    p.set_value(p.get_value() + self.delta)
                elif self.operator == "-":
                    p.set_value(p.get_value() - self.delta)
                elif self.operator == "*":
                    p.set_value(p.get_value() * self.delta)
                elif self.operator == "/":
                    p.set_value(p.get_value() / self.delta)
        return env

    @staticmethod
    def find_value(params: List, key: str) -> float:
        """Find the value of a parameter by key. Returns -1 if not found."""
        for p in params:
            if p.get_key() == key:
                return p.get_value()
        return -1
