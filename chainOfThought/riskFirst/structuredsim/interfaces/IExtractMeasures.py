from abc import ABC, abstractmethod
from typing import List
from experimenthandling.Measure import Measure


class IExtractMeasures(ABC):
    """Interface for extracting measures from a simulation result file."""

    @abstractmethod
    def extract_measures(self, results_file_path: str) -> List[Measure]:
        """Parse the result file and return a list of Measure objects."""
