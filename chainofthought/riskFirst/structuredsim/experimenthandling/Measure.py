class Measure:
    """Key-value data model for a simulation measure extracted from a results file."""

    def __init__(self, key: str = "", value: str = ""):
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

    def __repr__(self) -> str:
        return f"Key : {self.key} Value : {self.value}"
