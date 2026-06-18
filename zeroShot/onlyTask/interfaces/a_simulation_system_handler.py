from abc import ABC, abstractmethod


class ASimulationSystemHandler(ABC):

    def __init__(self):
        self.options = None
        self.list_modifier_class = []

    @abstractmethod
    def start_simulation(self, path_to_input_file):
        pass

    @abstractmethod
    def stop_program(self):
        pass

    @abstractmethod
    def read_parameters_file(self, parameters_file_path):
        pass

    @abstractmethod
    def write_parameters_file(self, set_of_parameters, location_to_store):
        pass

    @abstractmethod
    def extract_measures(self, results_file_path):
        pass

    @abstractmethod
    def initiate_modifier_list(self):
        pass

    def get_options(self):
        return self.options

    def set_options(self, options):
        self.options = options

    def get_list_modifier_class(self):
        return self.list_modifier_class

    def set_list_modifier_class(self, list_modifier_class):
        self.list_modifier_class = list_modifier_class
