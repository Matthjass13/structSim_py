from interfaces.i_start_simulation import IStartSimulation
from interfaces.i_stop_program import IStopProgram
from interfaces.i_manage_parameters_file import IManageParametersFile
from interfaces.i_extract_measures import IExtractMeasures
from interfaces.i_manage_modifier import IManageModifier


class ASimulationSystemHandler(IStartSimulation, IStopProgram, IManageParametersFile,
                                IExtractMeasures, IManageModifier):
    def __init__(self):
        self.options = None
        self.list_modifier_class = []

    def get_options(self):
        return self.options

    def set_options(self, options):
        self.options = options

    def get_list_modifier_class(self) -> list:
        return self.list_modifier_class

    def set_list_modifier_class(self, list_modifier_class: list):
        self.list_modifier_class = list_modifier_class
