class Parameter:
    """Defines characteristics of Parameters."""

    def __init__(self, key: str, value: float):
        self.key = key
        self.value = value

    def __init_copy__(self, p: "Parameter"):
        self.key = p.key
        self.value = p.value

    @classmethod
    def copy(cls, p: "Parameter") -> "Parameter":
        instance = cls.__new__(cls)
        instance.key = p.key
        instance.value = p.value
        return instance

    def get_key(self) -> str:
        return self.key

    def set_key(self, key: str) -> None:
        self.key = key

    def get_value(self) -> float:
        return self.value

    def set_value(self, value: float) -> None:
        self.value = value

    def __str__(self) -> str:
        return f"key : {self.key} value : {self.value}"
