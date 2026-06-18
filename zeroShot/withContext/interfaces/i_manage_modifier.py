from abc import ABC, abstractmethod
from typing import List


class IManageModifier(ABC):
    """Interface to manage modifiers."""

    @abstractmethod
    def initiate_modifier_list(self) -> List:
        """Initiate the modifier class list."""
        pass
