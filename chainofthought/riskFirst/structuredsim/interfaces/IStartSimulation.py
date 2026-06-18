from abc import ABC, abstractmethod


class IStartSimulation(ABC):
    """Interface for starting a simulation run."""

    @abstractmethod
    def start_simulation(self, path_to_input_file: str) -> None:
        """Execute the simulation using the given parameter input file."""
