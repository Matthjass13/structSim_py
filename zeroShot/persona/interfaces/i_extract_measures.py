from abc import ABC, abstractmethod
from typing import List


class IExtractMeasures(ABC):
    """Interface for extracting measures from a result file."""

    @abstractmethod
    def extract_measures(self, results_file_path: str) -> List: ...
