class Measure:
    """Defines characteristics of Measures that can be extracted from simulation result files."""

    def __init__(self, key: str, value: str):
        self.key = key
        self.value = value

    def get_key(self) -> str:
        return self.key

    def set_key(self, key: str) -> None:
        self.key = key

    def get_value(self) -> str:
        return self.value

    def set_value(self, value: str) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"Key : {self.key} Value : {self.value}"
