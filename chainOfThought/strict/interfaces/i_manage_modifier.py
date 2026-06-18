from abc import ABC, abstractmethod


class IManageModifier(ABC):
    @abstractmethod
    def initiate_modifier_list(self) -> list:
        """Initiate and return the list of AModifier instances."""
        pass
