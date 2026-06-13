from abc import ABC, abstractmethod
from typing import List


class IExtractMeasures(ABC):
    """Interface to manage the extraction of measures."""

    @abstractmethod
    def extract_measures(self, results_file_path: str) -> List:
        """Extract the measures from a results file path."""
        pass
