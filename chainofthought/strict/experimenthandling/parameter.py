class Parameter:
    def __init__(self, key=None, value=0.0, source=None):
        """
        Two construction modes:
          Parameter(key, value)          -- normal constructor
          Parameter(source=other_param)  -- copy constructor
        """
        if source is not None:
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

    def __str__(self):
        return self.__repr__()
