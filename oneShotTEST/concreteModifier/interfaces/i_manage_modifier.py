from abc import ABC, abstractmethod


class IManageModifier(ABC):

    @abstractmethod
    def initiate_modifier_list(self) -> list:
        pass
