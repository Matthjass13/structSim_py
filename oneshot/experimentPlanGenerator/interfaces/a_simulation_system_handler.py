from abc import abstractmethod
from typing import List

from experimenthandling.options import Options
from interfaces.a_modifier import AModifier
from interfaces.i_extract_measures import IExtractMeasures
from interfaces.i_manage_modifier import IManageModifier
from interfaces.i_manage_parameters_file import IManageParametersFile
from interfaces.i_start_simulation import IStartSimulation
from interfaces.i_stop_program import IStopProgram


class ASimulationSystemHandler(
    IStartSimulation, IStopProgram, IManageParametersFile, IExtractMeasures, IManageModifier
):

    def __init__(self) -> None:
        self.options: Options = Options()
        self.list_modifier_class: List[AModifier] = []

    def get_options(self) -> Options:
        return self.options

    def set_options(self, options: Options) -> None:
        self.options = options

    def get_list_modifier_class(self) -> List[AModifier]:
        return self.list_modifier_class

    def set_list_modifier_class(self, list_modifier_class: List[AModifier]) -> None:
        self.list_modifier_class = list_modifier_class
