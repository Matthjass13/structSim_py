from abc import ABC, abstractmethod
from typing import List


class IManageModifier(ABC):
    """Interface for managing the modifier list."""

    @abstractmethod
    def initiate_modifier_list(self) -> List: ...
