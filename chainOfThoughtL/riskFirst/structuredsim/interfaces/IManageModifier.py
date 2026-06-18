from abc import ABC, abstractmethod
from typing import List


class IManageModifier(ABC):
    """Interface for initialising the modifier list."""

    @abstractmethod
    def initiate_modifier_list(self) -> List:
        """Initialise and return the list of AModifier instances."""
