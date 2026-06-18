class Measure:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

    def __str__(self):
        return f"Key : {self.key} Value : {self.value}"
