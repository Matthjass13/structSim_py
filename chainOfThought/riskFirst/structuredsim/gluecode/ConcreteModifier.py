import logging
from typing import List, Optional

from experimenthandling.Environment import Environment
from experimenthandling.Parameter import Parameter
from interfaces.AModifier import AModifier

logger = logging.getLogger(__name__)


class ConcreteModifier(AModifier):
    """
    Concrete modifier that applies arithmetic operations (+, -, *, /) to a named parameter.

    The operator field is a char in Java; it is kept as a single-character str in Python.
    The three Java constructors are unified into one __init__ with default arguments.
    """

    def __init__(
        self,
        key_to_change: str = "val1",
        operator: str = "*",
        delta: float = 1.0,
        probability: float = 1.0,
    ):
        # When called as ConcreteModifier(delta), mirror the Java ConcreteModifier(double delta) ctor
        if isinstance(key_to_change, (int, float)) and operator == "*" and delta == 1.0:
            delta = float(key_to_change)
            probability = delta
            key_to_change = "val1"

        super().__init__(probability, operator + str(delta))
        self.key_to_change = key_to_change
        self.operator = operator
        self.delta = delta

    def apply_modifier(self, env: Environment) -> Environment:
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
    def find_value(params: List[Parameter], key: str) -> float:
        for p in params:
            if p.get_key() == key:
                return p.get_value()
        return -1.0
