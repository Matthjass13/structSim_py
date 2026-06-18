"""
Chain-of-thought for Parameter:
1. Java-specific constructs: public/protected field visibility, explicit getter/setter methods,
   @Override toString(), constructor overloading (copy constructor).
2. Python equivalents:
   - Fields: Python has no access modifiers; use naming convention (_value for protected).
   - Getters/setters: Kept for API compatibility, but Python properties could also be used.
   - Copy constructor: Handled via a second __init__ signature — in Python we use a classmethod
     factory (from_parameter) since Python does not support constructor overloading natively.
   - __str__ replaces toString().
3. Risks/deviations:
   - Java 'protected' has no enforcement in Python; _value is a convention only.
   - Copy constructor pattern replaced by classmethod — callers must use Parameter.from_parameter(p).
"""


class Parameter:
    """Represents a named numeric parameter."""

    def __init__(self, key: str, value: float):
        self.key = key
        self._value = value

    @classmethod
    def from_parameter(cls, p: "Parameter") -> "Parameter":
        """Copy constructor equivalent."""
        return cls(p.key, p._value)

    def __str__(self) -> str:
        return f"key : {self.key} value : {self._value}"

    def get_key(self) -> str:
        return self.key

    def set_key(self, key: str) -> None:
        self.key = key

    def get_value(self) -> float:
        return self._value

    def set_value(self, value: float) -> None:
        self._value = value

    # Also expose as property for Pythonic access
    @property
    def value(self) -> float:
        return self._value

    @value.setter
    def value(self, v: float) -> None:
        self._value = v
