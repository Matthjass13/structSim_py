import logging
from interfaces.a_modifier import AModifier

logger = logging.getLogger(__name__)


class ConcreteModifier(AModifier):

    def __init__(self, key_to_change=None, operator=None, delta=None, probability=1.0):
        if operator is None and delta is None and isinstance(key_to_change, (int, float)):
            # Mirrors Java: ConcreteModifier(double delta) → this("val1", '*', delta, delta)
            d = float(key_to_change)
            super().__init__(d, '*' + str(d))
            self.key_to_change = "val1"
            self.operator = '*'
            self.delta = d
        elif key_to_change is None and operator is None and delta is None:
            super().__init__()
            self.key_to_change = None
            self.operator = None
            self.delta = None
        else:
            super().__init__(probability, str(operator) + str(delta))
            self.key_to_change = key_to_change
            self.operator = operator
            self.delta = delta

    def apply_modifier(self, env):
        params = env.get_set_of_parameters()
        for p in params:
            logger.debug(f"param={p.get_key()} keyToChange={self.key_to_change}")
            if p.get_key() == self.key_to_change:
                if self.operator == '+':
                    p.set_value(p.get_value() + self.delta)
                elif self.operator == '-':
                    p.set_value(p.get_value() - self.delta)
                elif self.operator == '*':
                    p.set_value(p.get_value() * self.delta)
                elif self.operator == '/':
                    p.set_value(p.get_value() / self.delta)
        return env

    @staticmethod
    def find_value(params, key):
        for p in params:
            if p.get_key() == key:
                return p.get_value()
        return -1
