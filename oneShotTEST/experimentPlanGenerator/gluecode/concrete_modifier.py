import logging
from typing import List

from experimenthandling.environment import Environment
from experimenthandling.parameter import Parameter
from interfaces.a_modifier import AModifier

logger = logging.getLogger(__name__)


class ConcreteModifier(AModifier):

    def __init__(
        self,
        key_to_change: str = "val1",
        operator: str = "*",
        delta: float = 1.0,
        probability: float = 1.0,
    ) -> None:
        super().__init__(probability, operator + str(delta))
        self.key_to_change: str = key_to_change
        self.operator: str = operator
        self.delta: float = delta

    def apply_modifier(self, env: Environment) -> Environment:
        params: List[Parameter] = env.get_set_of_parameters()
        for p in params:
            logger.debug("param=%s keyToChange=%s", p.get_key(), self.key_to_change)
            if p.get_key() == self.key_to_change:
                match self.operator:
                    case "+":
                        p.set_value(p.get_value() + self.delta)
                    case "-":
                        p.set_value(p.get_value() - self.delta)
                    case "*":
                        p.set_value(p.get_value() * self.delta)
                    case "/":
                        p.set_value(p.get_value() / self.delta)
        return env

    @staticmethod
    def find_value(params: List[Parameter], key: str) -> float:
        for p in params:
            if p.get_key() == key:
                return p.get_value()
        return -1.0
