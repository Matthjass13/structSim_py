from experimenthandling.parameter import Parameter


class Environment:
    def __init__(self, id=1, set_of_parameters=None, probability=1.0):
        import copy
        if isinstance(set_of_parameters, Environment):
            source = set_of_parameters
            self.id = id
            self.set_of_parameters = copy.deepcopy(source.set_of_parameters)
            self.probability = source.probability
            self.path_save_result = source.path_save_result
            self.trace = list(source.trace)
            return
        self.id = id
        self.set_of_parameters = set_of_parameters if set_of_parameters is not None else []
        self.probability = probability
        self.path_save_result = None   # str
        self.trace = []                # List[str]

    @classmethod
    def copy(cls, id, source_env):
        """Deep copy constructor: Environment(id, source_env) in Java."""
        new_params = [Parameter(source=p) for p in source_env.set_of_parameters]
        env = cls(id, new_params, source_env.probability)
        env.path_save_result = source_env.path_save_result
        env.trace = list(source_env.trace)
        return env

    def get_id(self):
        return self.id

    def get_set_of_parameters(self):
        return self.set_of_parameters

    def set_set_of_parameters(self, set_of_parameters):
        self.set_of_parameters = set_of_parameters

    def get_probability(self):
        return self.probability

    def set_probability(self, probability):
        self.probability = probability

    def get_path_save_result(self):
        return self.path_save_result

    def set_path_save_result(self, path_save_result):
        self.path_save_result = path_save_result

    def get_trace(self):
        return self.trace

    def set_trace(self, trace):
        self.trace = trace

    def to_string_modifier(self):
        result = ""
        for s in self.trace:
            result += "   " + s
        return (f"Simulation ID : {self.id}\t Probability : {self.probability}"
                f"\t Modifier implemented : {result}")

    # Comparable support (replaces Java Comparable<Environment>)
    def __lt__(self, other):
        return self.probability < other.probability

    def __eq__(self, other):
        if not isinstance(other, Environment):
            return NotImplemented
        return self.probability == other.probability

    def __le__(self, other):
        return self.probability <= other.probability

    def __gt__(self, other):
        return self.probability > other.probability

    def __ge__(self, other):
        return self.probability >= other.probability

    def compare_to(self, other: "Environment") -> int:
        if self.probability < other.probability:
            return -1
        elif self.probability > other.probability:
            return 1
        return 0

    def __repr__(self):
        return self.to_string_modifier()
