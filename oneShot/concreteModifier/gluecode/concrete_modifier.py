import logging
from experimenthandling.environment import Environment
from experimenthandling.parameter import Parameter
from interfaces.a_modifier import AModifier

logger = logging.getLogger(__name__)

class ConcreteModifier(AModifier):

    def __init__(self, key_to_change: str = "", operator: str = "",
                 delta: float = 0.0, probability: float = 0.0):
        if isinstance(key_to_change, (int, float)) and operator == "" and delta == 0.0:
            d = float(key_to_change)
            key_to_change = "val1"
            operator = "*"
            delta = d
            probability = d
        super().__init__(probability, operator + str(delta))
        self.key_to_change = key_to_change
        self.operator = operator
        self.delta = delta

    @classmethod
    def from_key_operator_delta(cls, key_to_change: str, operator: str,
                                delta: float) -> 'ConcreteModifier':
        return cls(key_to_change, operator, delta, 1.0)

    @classmethod
    def from_delta(cls, delta: float) -> 'ConcreteModifier':
        return cls("val1", '*', delta, delta)

    def apply_modifier(self, env: Environment) -> Environment:
        params = env.get_set_of_parameters()
        for p in params:
            logger.debug(f"param={p.get_key()} key_to_change={self.key_to_change}")
            if p.get_key() == self.key_to_change:
                match self.operator:
                    case '+': p.set_value(p.get_value() + self.delta)
                    case '-': p.set_value(p.get_value() - self.delta)
                    case '*': p.set_value(p.get_value() * self.delta)
                    case '/': p.set_value(p.get_value() / self.delta)
        return env

    @staticmethod
    def find_value(params: list[Parameter], key: str) -> float:
        for p in params:
            if p.get_key() == key:
                return p.get_value()
        return -1.0
