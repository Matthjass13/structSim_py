from abc import ABC, abstractmethod
from typing import IO, Union


class IManageParametersFile(ABC):

    @abstractmethod
    def read_parameters_file(self, parameters_file_path: str) -> list:
        pass

    @abstractmethod
    def read_parameters_file_from_stream(self, input_stream: IO) -> list:
        pass

    @abstractmethod
    def write_parameters_file(self, set_of_parameters: list, location_to_store: str) -> None:
        pass
