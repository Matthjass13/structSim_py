from abc import ABC, abstractmethod


class IStartSimulation(ABC):
    """Interface for starting an external simulator."""

    @abstractmethod
    def start_simulation(self, path_to_input_file: str) -> None: ...
