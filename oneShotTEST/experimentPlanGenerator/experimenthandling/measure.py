class Measure:
    def __init__(self, key: str, value: str) -> None:
        self.key: str = key
        self.value: str = value

    def __str__(self) -> str:
        return f"Key : {self.key} Value : {self.value}"
