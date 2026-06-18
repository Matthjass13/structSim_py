from abc import ABC, abstractmethod
from typing import IO, List


class IManageParametersFile(ABC):
    """Interface defining methods to manage parameters files."""

    @abstractmethod
    def read_parameters_file(self, parameters_file_path) -> List:
        """
        Read a parameters file used by the simulator.
        Accepts either a file path (str) or a file-like object (IO).
        Returns a list of Parameter objects.
        """
        pass

    @abstractmethod
    def write_parameters_file(self, set_of_parameters: List, location_to_store: str) -> None:
        """
        Write a new parameters file to be used by the simulator each time a parameter changes.
        """
        pass
