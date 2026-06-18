from abc import ABC, abstractmethod


class AModifier(ABC):
    def __init__(self, probability=0.0, name="AModifier"):
        self.probability = probability
        self.name = name

    @abstractmethod
    def apply_modifier(self, env):
        """Apply the modifier to an Environment and return the modified Environment."""
        pass

    def get_probability(self):
        return self.probability

    def set_probability(self, probability):
        self.probability = probability

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name
