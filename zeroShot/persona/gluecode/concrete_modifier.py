import logging
from typing import List

from experimenthandling.environment import Environment
from experimenthandling.parameter import Parameter
from interfaces.a_modifier import AModifier

logger = logging.getLogger(__name__)


class ConcreteModifier(AModifier):
    """
    A modifier that applies a single arithmetic operation (+, -, *, /)
    with a configurable delta to a named parameter.

    Supports three Java-style calling conventions:
      ConcreteModifier(key, operator, delta, probability)   ← full constructor
      ConcreteModifier(key, operator, delta)                ← probability defaults to 1.0
      ConcreteModifier(delta)                               ← shorthand: key="val1", op='*', prob=delta
    """

    def __init__(self, key_to_change="val1", operator="*", delta=1.0, probability=1.0):
        # Detect the single-float shorthand: ConcreteModifier(0.5)
        # In this case key_to_change is actually the delta value (a number)
        if isinstance(key_to_change, (int, float)):
            actual_delta = float(key_to_change)
            key_to_change = "val1"
            operator = "*"
            delta = actual_delta
            probability = actual_delta

        super().__init__(probability=probability, name=f"{operator}{delta}")
        self.key_to_change = key_to_change
        self.operator = operator
        self.delta = delta

    def apply_modifier(self, env: Environment) -> Environment:
        params: List[Parameter] = env.get_set_of_parameters()
        for p in params:
            logger.debug("param=%s  keyToChange=%s", p.get_key(), self.key_to_change)
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
