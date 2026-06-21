from experimenthandling.parameter import Parameter


class Environment:

    def __init__(self, id=1, set_of_parameters=None, probability=1, source_env=None):
        if source_env is not None:
            # Copy constructor: copy from source_env, assign new id
            self.id = id
            self.set_of_parameters = [Parameter(p.key, p.value) for p in source_env.set_of_parameters]
            self.probability = source_env.probability
            self.trace = list(source_env.trace)
        else:
            self.id = id
            self.set_of_parameters = set_of_parameters if set_of_parameters is not None else []
            self.probability = probability
            self.trace = []

        self.path_save_result = None

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
        result = "   ".join(self.trace)
        return f"Simulation ID : {self.id}\t Probability : {self.probability}\t Modifier implemented :    {result}"

    def __lt__(self, other):
        return self.probability < other.probability

    def __eq__(self, other):
        return self.probability == other.probability

    def __repr__(self):
        return f"Environment(id={self.id}, prob={self.probability})"
