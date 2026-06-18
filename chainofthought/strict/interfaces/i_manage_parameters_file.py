from abc import ABC, abstractmethod


class IManageParametersFile(ABC):
    @abstractmethod
    def read_parameters_file(self, parameters_file_path) -> list:
        """
        Read parameters from a file path (str) or a file-like object.
        Returns list of Parameter.
        """
        pass

    @abstractmethod
    def write_parameters_file(self, set_of_parameters: list, location_to_store: str) -> None:
        """Write parameters to a file at location_to_store."""
        pass
