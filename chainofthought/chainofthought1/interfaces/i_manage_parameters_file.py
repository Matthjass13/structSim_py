from abc import ABC, abstractmethod
from typing import List


class IManageParametersFile(ABC):
    @abstractmethod
    def read_parameters_file(self, parameters_file_path) -> List:
        """
        Read a parameters file. Accepts either a file path string or a file-like object.
        Returns a list of Parameter objects.
        """
        pass

    @abstractmethod
    def write_parameters_file(self, set_of_parameters: List, location_to_store: str):
        pass
