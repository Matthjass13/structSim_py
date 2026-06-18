from abc import ABC, abstractmethod
from typing import IO, List


class IManageParametersFile(ABC):
    """Interface for reading and writing parameter files."""

    @abstractmethod
    def read_parameters_file(self, parameters_file_path: str) -> List: ...

    @abstractmethod
    def read_parameters_file_from_stream(self, stream: IO) -> List: ...

    @abstractmethod
    def write_parameters_file(self, set_of_parameters: List, location_to_store: str) -> None: ...
