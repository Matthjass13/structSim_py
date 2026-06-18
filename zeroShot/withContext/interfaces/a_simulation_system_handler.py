from typing import List

from interfaces.i_start_simulation import IStartSimulation
from interfaces.i_stop_program import IStopProgram
from interfaces.i_manage_parameters_file import IManageParametersFile
from interfaces.i_extract_measures import IExtractMeasures
from interfaces.i_manage_modifier import IManageModifier


class ASimulationSystemHandler(IStartSimulation, IStopProgram, IManageParametersFile, IExtractMeasures, IManageModifier):
    """
    Abstract class to manage all implementations needed in the glue code.
    Implements all simulation-related interfaces.
    """

    def __init__(self):
        self.options = None
        self.list_modifier_class: List = []

    def get_options(self):
        return self.options

    def set_options(self, options) -> None:
        self.options = options

    def get_list_modifier_class(self) -> List:
        return self.list_modifier_class

    def set_list_modifier_class(self, list_modifier_class: List) -> None:
        self.list_modifier_class = list_modifier_class
