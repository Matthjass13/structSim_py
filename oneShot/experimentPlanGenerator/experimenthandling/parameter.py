class Parameter:
    def __init__(self, key: str = "", value: float = 0.0, other: "Parameter" = None):
        if other is not None:
            self.key: str = other.key
            self.value: float = other.value
        else:
            self.key = key
            self.value = value

    def get_key(self) -> str:
        return self.key

    def get_value(self) -> float:
        return self.value

    def set_value(self, value: float) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"key : {self.key} value : {self.value}"
