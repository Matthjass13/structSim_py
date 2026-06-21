import logging

from interfaces.a_modifier import AModifier
from experimenthandling.environment import Environment

logger = logging.getLogger(__name__)


class ConcreteModifier(AModifier):
    def __init__(self, key_to_change: str = "val1", operator: str = "*",
                 delta: float = 1.0, probability: float = 1.0):
        if isinstance(key_to_change, (int, float)):
            delta = float(key_to_change)
            key_to_change = "val1"
            operator = "*"
            probability = delta
        super().__init__(probability=probability, name=f"{operator}{delta}")
        self.key_to_change = key_to_change
        self.operator = operator
        self.delta = delta

    @classmethod
    def from_delta_only(cls, delta: float) -> "ConcreteModifier":
        return cls(key_to_change="val1", operator="*", delta=delta, probability=delta)

    def apply_modifier(self, env: Environment) -> Environment:
        params = env.get_set_of_parameters()
        for p in params:
            logger.debug(f"param={p.get_key()} key_to_change={self.key_to_change}")
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
    def find_value(params: list, key: str) -> float:
        for p in params:
            if p.get_key() == key:
                return p.get_value()
        return -1.0
