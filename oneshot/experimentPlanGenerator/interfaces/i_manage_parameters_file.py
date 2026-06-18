from abc import ABC, abstractmethod
from typing import IO, List

from experimenthandling.parameter import Parameter


class IManageParametersFile(ABC):

    @abstractmethod
    def read_parameters_file(self, parameters_file_path) -> List[Parameter]:
        ...

    @abstractmethod
    def write_parameters_file(self, set_of_parameters: List[Parameter], location_to_store: str) -> None:
        ...
