"""
Chain-of-thought for IManageModifier:
1. Java-specific constructs: interface, List<AModifier> return type (forward reference to AModifier).
2. Python equivalents:
   - Interface -> ABC with @abstractmethod.
   - List<AModifier> -> List['AModifier'] (string forward reference to avoid circular import).
3. Risks/deviations:
   - AModifier is defined later (a_modifier.py); use TYPE_CHECKING guard or string annotation.
"""

from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from interfaces.a_modifier import AModifier


class IManageModifier(ABC):
    """Interface: produce the list of modifiers used by the experiment plan generator."""

    @abstractmethod
    def initiate_modifier_list(self) -> List["AModifier"]:
        """Return the initialised list of AModifier instances."""
        ...
