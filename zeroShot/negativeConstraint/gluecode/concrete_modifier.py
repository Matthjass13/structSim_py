import logging
from interfaces.a_modifier import AModifier

logger = logging.getLogger(__name__)


class ConcreteModifier(AModifier):

    def __init__(self, key_to_change=None, operator=None, delta=None, probability=1):
        # Handle single-float constructor: ConcreteModifier(0.5) maps Java's
        # ConcreteModifier(double delta) -> this("val1", '*', delta, delta)
        if isinstance(key_to_change, (int, float)) and operator is None and delta is None:
            d = float(key_to_change)
            key_to_change = "val1"
            operator = '*'
            delta = d
            probability = d

        if key_to_change is None and operator is None and delta is None:
            super().__init__(0.0, "AModifier")
            self.key_to_change = None
            self.operator = None
            self.delta = None
            return

        if operator is not None and delta is not None:
            name = operator + str(delta)
        else:
            name = "AModifier"

        super().__init__(probability, name)
        self.key_to_change = key_to_change
        self.operator = operator
        self.delta = delta

    @classmethod
    def from_delta(cls, delta):
        return cls("val1", '*', delta, delta)

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
