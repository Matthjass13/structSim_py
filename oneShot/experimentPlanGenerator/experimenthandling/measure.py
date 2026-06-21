class Measure:
    def __init__(self, key: str, value: str) -> None:
        self.key: str = key
        self.value: str = value

    def get_key(self) -> str:
        return self.key

    def get_value(self) -> str:
        return self.value

    def __str__(self) -> str:
        return f"Key : {self.key} Value : {self.value}"
