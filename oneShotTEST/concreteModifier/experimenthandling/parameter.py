class Parameter:

    def __init__(self, key: str = "", value: float = 0.0):
        self.key = key
        self.value = value

    @classmethod
    def from_parameter(cls, p: 'Parameter') -> 'Parameter':
        return cls(p.key, p.value)

    def __str__(self) -> str:
        return f"key : {self.key} value : {self.value}"

    def get_key(self) -> str:
        return self.key

    def set_key(self, key: str) -> None:
        self.key = key

    def get_value(self) -> float:
        return self.value

    def set_value(self, value: float) -> None:
        self.value = value
