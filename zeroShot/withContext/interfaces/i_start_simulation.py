from abc import ABC, abstractmethod


class IStartSimulation(ABC):
    """Interface to start a simulation."""

    @abstractmethod
    def start_simulation(self, path_to_input_file: str) -> None:
        """Start the simulation. Results are saved to a file."""
        pass
