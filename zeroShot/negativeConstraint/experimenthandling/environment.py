from experimenthandling.parameter import Parameter


class Environment:

    def __init__(self, id=1, set_of_parameters=None, probability=1, copy_from=None):
        if copy_from is not None:
            self.id = id
            self.set_of_parameters = [Parameter(p) for p in copy_from.set_of_parameters]
            self.probability = copy_from.probability
            self.trace = list(copy_from.trace)
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

    def to_string_modifier(self):
        result = "   ".join(self.trace)
        return f"Simulation ID : {self.id}\t Probability : {self.probability}\t Modifier implemented :    {result}"

    def get_trace(self):
        return self.trace

    def set_trace(self, trace):
        self.trace = trace

    def __lt__(self, other):
        return self.probability < other.probability

    def __eq__(self, other):
        return self.probability == other.probability

    def __le__(self, other):
        return self.probability <= other.probability

    def __gt__(self, other):
        return self.probability > other.probability

    def __ge__(self, other):
        return self.probability >= other.probability
