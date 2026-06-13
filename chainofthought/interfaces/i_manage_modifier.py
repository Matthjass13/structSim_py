from abc import ABC, abstractmethod
from typing import List


class IManageModifier(ABC):
    @abstractmethod
    def initiate_modifier_list(self) -> List:
        pass
