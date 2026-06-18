"""
Chain-of-thought for IStartSimulation:
1. Java-specific constructs: single-method interface.
2. Python equivalents: ABC with one @abstractmethod.
3. Risks/deviations: None.
"""

from abc import ABC, abstractmethod


class IStartSimulation(ABC):
    """Interface: start a simulation given a path to the input parameter file."""

    @abstractmethod
    def start_simulation(self, path_to_input_file: str) -> None:
        ...
