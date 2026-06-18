from abc import ABC, abstractmethod
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from interfaces.a_modifier import AModifier


class IManageModifier(ABC):

    @abstractmethod
    def initiate_modifier_list(self) -> List["AModifier"]:
        ...
