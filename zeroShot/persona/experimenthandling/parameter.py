class Parameter:
    """Represents a single key/value simulation parameter."""

    def __init__(self, key: str, value: float):
        self.key = key
        self.value = value

    @classmethod
    def copy_from(cls, other: "Parameter") -> "Parameter":
        return cls(other.key, other.value)

    def get_key(self) -> str:
        return self.key

    def set_key(self, key: str) -> None:
        self.key = key

    def get_value(self) -> float:
        return self.value

    def set_value(self, value: float) -> None:
        self.value = value

    def __repr__(self) -> str:
        return f"key : {self.key} value : {self.value}"
