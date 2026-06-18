from abc import abstractmethod

from interfaces.i_extract_measures import IExtractMeasures
from interfaces.i_manage_modifier import IManageModifier
from interfaces.i_manage_parameters_file import IManageParametersFile
from interfaces.i_start_simulation import IStartSimulation
from interfaces.i_stop_program import IStopProgram


class ASimulationSystemHandler(
    IStartSimulation,
    IStopProgram,
    IManageParametersFile,
    IExtractMeasures,
    IManageModifier,
):
    """
    Abstract base class that combines all five interfaces.
    Concrete subclasses must implement all abstract methods.
    """

    def __init__(self):
        self.options = None               # Options instance
        self.list_modifier_class = []     # List[AModifier]

    def get_options(self):
        return self.options

    def set_options(self, options):
        self.options = options

    def get_list_modifier_class(self):
        return self.list_modifier_class

    def set_list_modifier_class(self, list_modifier_class):
        self.list_modifier_class = list_modifier_class

    # Re-declare abstract methods so subclasses are forced to implement them
    @abstractmethod
    def start_simulation(self, path_to_input_file: str) -> None:
        pass

    @abstractmethod
    def stop_program(self) -> None:
        pass

    @abstractmethod
    def read_parameters_file(self, parameters_file_path) -> list:
        pass

    @abstractmethod
    def write_parameters_file(self, set_of_parameters: list, location_to_store: str) -> None:
        pass

    @abstractmethod
    def extract_measures(self, results_file_path: str) -> list:
        pass

    @abstractmethod
    def initiate_modifier_list(self) -> list:
        pass
