from typing import List, Optional

from interfaces.IExtractMeasures import IExtractMeasures
from interfaces.IManageModifier import IManageModifier
from interfaces.IManageParametersFile import IManageParametersFile
from interfaces.IStartSimulation import IStartSimulation
from interfaces.IStopProgram import IStopProgram
from experimenthandling.Options import Options


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
