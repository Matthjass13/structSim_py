class Parameter:

    def __init__(self, key, value, source=None):
        if source is not None:
            # copy constructor
            self.key = source.key
            self.value = source.value
        else:
            self.key = key
            self.value = value

    def get_key(self):
        return self.key

    def set_key(self, key):
        self.key = key

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def __repr__(self):
        return f"key : {self.key} value : {self.value}"
