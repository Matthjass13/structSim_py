class Parameter:
    def __init__(self, key: str, value: float, copy_from=None):
        if copy_from is not None:
            self.key = copy_from.key
            self.value = copy_from.value
        else:
            self.key = key
            self.value = value

    def get_key(self) -> str:
        return self.key

    def set_key(self, key: str):
        self.key = key

    def get_value(self) -> float:
        return self.value

    def set_value(self, value: float):
        self.value = value

    def __repr__(self) -> str:
        return f"key : {self.key} value : {self.value}"
