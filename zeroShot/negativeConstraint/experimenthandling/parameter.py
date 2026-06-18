class Parameter:

    def __init__(self, key, value=None):
        if isinstance(key, Parameter):
            self.key = key.key
            self.value = key.value
        else:
            self.key = key
            self.value = float(value)

    def __str__(self):
        return f"key : {self.key} value : {self.value}"

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
