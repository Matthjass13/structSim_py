"""
Chain-of-thought for Measure:
1. Java-specific constructs: protected fields, explicit getters/setters, @Override toString().
2. Python equivalents:
   - protected fields: name-mangled as _key/_value by convention only.
   - Getters/setters: kept verbatim for API compatibility.
   - __str__ replaces toString().
3. Risks/deviations:
   - Both key and value are strings in Measure (unlike Parameter where value is double).
   - No enforcement of 'protected' in Python.
"""


class Measure:
    """Represents a key-value measurement result (both as strings)."""

    def __init__(self, key: str, value: str):
        self._key = key
        self._value = value

    def get_value(self) -> str:
        return self._value

    def set_value(self, value: str) -> None:
        self._value = value

    def get_key(self) -> str:
        return self._key

    def set_key(self, key: str) -> None:
        self._key = key

    def __str__(self) -> str:
        return f"Key : {self._key} Value : {self._value}"
