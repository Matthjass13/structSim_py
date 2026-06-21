from typing import List, Optional

from interfaces.i_extract_measures import IExtractMeasures
from interfaces.i_manage_modifier import IManageModifier
from interfaces.i_manage_parameters_file import IManageParametersFile
from interfaces.i_start_simulation import IStartSimulation
from interfaces.i_stop_program import IStopProgram
from experimenthandling.options import Options


class ASimulationSystemHandler(
    IStartSimulation,
    IStopProgram,
    IManageParametersFile,
    IExtractMeasures,
    IManageModifier,
):
    """
    Abstract handler that aggregates all simulation-related interfaces.

    Java multiple interface implementation → Python multiple ABC inheritance.
    Python resolves the MRO (Method Resolution Order) automatically.
    """

    def __init__(self):
        self.options: Optional[Options] = None
        self.list_modifier_class: List = []

    def get_options(self) -> Optional[Options]:
        return self.options

    def set_options(self, options: Options) -> None:
        self.options = options

    def get_list_modifier_class(self) -> List:
        return self.list_modifier_class

    def set_list_modifier_class(self, list_modifier_class: List) -> None:
        self.list_modifier_class = list_modifier_class
