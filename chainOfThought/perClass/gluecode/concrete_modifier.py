"""
Chain-of-thought for ConcreteModifier:
1. Java-specific constructs:
   - Extends abstract class AModifier (inheritance with abstract method override).
   - Constructor overloading (4 constructors with different signatures).
   - char type for operator (+, -, *, /).
   - Vector<Parameter> from Environment.
   - Static method findValue.
2. Python equivalents:
   - Inheritance: class ConcreteModifier(AModifier).
   - Constructor overloading: single __init__ with default arguments + classmethods.
   - char: plain str of length 1; no special type needed.
   - Vector<Parameter>: list of Parameter objects (already translated in Environment).
   - @staticmethod for findValue.
3. Risks/deviations:
   - Java char operator stored as str; arithmetic dispatch via dict or if/elif.
   - The 'name' field set in super().__init__ uses str(operator)+str(delta) to match Java.
   - Division by zero not guarded (matches Java behavior).
"""

from interfaces.a_modifier import AModifier
from experimenthandling.environment import Environment
import logging

logger = logging.getLogger(__name__)


class ConcreteModifier(AModifier):
    """Applies arithmetic operations (+, -, *, /) to a named parameter."""

    def __init__(self, key_to_change: str = "val1", operator: str = "*",
                 delta: float = 1.0, probability: float = 1.0):
        if isinstance(key_to_change, float):
            probability = key_to_change
            delta = key_to_change
            key_to_change = "val1"
        super().__init__(probability=probability, name=f"{operator}{delta}")
        self.key_to_change = key_to_change
        self.operator = operator
        self.delta = delta

    @classmethod
    def from_delta(cls, delta: float) -> "ConcreteModifier":
        """Matches ConcreteModifier(double delta) constructor."""
        return cls(key_to_change="val1", operator="*", delta=delta, probability=delta)

    def apply_modifier(self, env: Environment) -> Environment:
        for p in env.set_of_parameters:
            logger.debug(f"param={p.key} keyToChange={self.key_to_change}")
            if p.key == self.key_to_change:
                if self.operator == "+":
                    p.value = p.value + self.delta
                elif self.operator == "-":
                    p.value = p.value - self.delta
                elif self.operator == "*":
                    p.value = p.value * self.delta
                elif self.operator == "/":
                    p.value = p.value / self.delta
        return env

    @staticmethod
    def find_value(params: list, key: str) -> float:
        for p in params:
            if p.key == key:
                return p.value
        return -1.0
