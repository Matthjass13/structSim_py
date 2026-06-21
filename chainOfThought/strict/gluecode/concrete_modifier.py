from interfaces.a_modifier import AModifier


class ConcreteModifier(AModifier):
    def __init__(self, key_to_change=None, operator=None, delta=None, probability=None):
        """
        Mirrors three Java constructors:
          ConcreteModifier(keyToChange, operator, delta, probability)
          ConcreteModifier(keyToChange, operator, delta)   -> probability=1
          ConcreteModifier(delta)                          -> key='val1', op='*', prob=delta
          ConcreteModifier()                               -> defaults
        """
        if isinstance(key_to_change, (int, float)) and operator is None and delta is None:
            # Java: ConcreteModifier(double delta) -> this("val1", '*', delta, delta)
            d = float(key_to_change)
            super().__init__(d, '*' + str(d))
            self.key_to_change = "val1"
            self.operator = '*'
            self.delta = d
            return
        if key_to_change is not None and operator is not None and delta is not None:
            prob = probability if probability is not None else 1.0
            super().__init__(prob, str(operator) + str(delta))
            self.key_to_change = key_to_change
            self.operator = operator
            self.delta = delta
        elif key_to_change is None and operator is None and delta is not None:
            # ConcreteModifier(delta) constructor
            super().__init__(delta, '*' + str(delta))
            self.key_to_change = "val1"
            self.operator = '*'
            self.delta = delta
        else:
            # Default no-arg constructor
            super().__init__(0.0, "AModifier")
            self.key_to_change = None
            self.operator = None
            self.delta = None

    def apply_modifier(self, env):
        params = env.get_set_of_parameters()
        for p in params:
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
    def find_value(params: list, key: str) -> float:
        """Return the value of the parameter with the given key, or -1 if not found."""
        for p in params:
            if p.get_key() == key:
                return p.get_value()
        return -1.0
