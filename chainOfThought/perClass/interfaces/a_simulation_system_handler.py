"""
Chain-of-thought for ASimulationSystemHandler:
1. Java-specific constructs: abstract class implementing four interfaces simultaneously,
   ArrayList<AModifier> field, protected Options field.
2. Python equivalents:
   - Multiple interface implementation -> multiple inheritance from all four ABCs.
   - ArrayList -> list.
   - Abstract class: still ABC (multiple inheritance with ABC is well-supported in Python).
3. Risks/deviations:
   - Python MRO (Method Resolution Order) handles multiple inheritance; no diamond problem here
     because all parent ABCs inherit only from ABC.
   - Subclasses must implement ALL abstract methods from all four interfaces.
"""

from abc import ABC
from typing import List, Optional
from interfaces.i_start_simulation import IStartSimulation
from interfaces.i_stop_program import IStopProgram
from interfaces.i_manage_parameters_file import IManageParametersFile
from interfaces.i_extract_measures import IExtractMeasures
from interfaces.i_manage_modifier import IManageModifier
from experimenthandling.options import Options
from interfaces.a_modifier import AModifier


class ASimulationSystemHandler(
    IStartSimulation,
    IStopProgram,
    IManageParametersFile,
    IExtractMeasures,
    IManageModifier,
    ABC,
):
    """Abstract handler that must be subclassed to provide simulation logic."""

    def __init__(self):
        self._options: Optional[Options] = None
        self.list_modifier_class: List[AModifier] = []

    def get_options(self) -> Optional[Options]:
        return self._options

    def set_options(self, options: Options) -> None:
        self._options = options

    def get_list_modifier_class(self) -> List[AModifier]:
        return self.list_modifier_class

    def set_list_modifier_class(self, modifiers: List[AModifier]) -> None:
        self.list_modifier_class = modifiers
