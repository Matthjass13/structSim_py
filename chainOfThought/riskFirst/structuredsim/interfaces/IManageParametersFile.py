from abc import ABC, abstractmethod
from typing import IO, List, Union
from experimenthandling.Parameter import Parameter


class IManageParametersFile(ABC):
    """Interface for reading and writing parameter files."""

    @abstractmethod
    def read_parameters_file(self, parameters_file_path: Union[str, IO]) -> List[Parameter]:
        """Read a parameters file (path or stream) and return a list of Parameter objects."""

    @abstractmethod
    def write_parameters_file(self, set_of_parameters: List[Parameter], location_to_store: str) -> None:
        """Write a parameters file to the given directory."""
