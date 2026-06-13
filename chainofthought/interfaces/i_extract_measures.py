from abc import ABC, abstractmethod
from typing import List


class IExtractMeasures(ABC):
    @abstractmethod
    def extract_measures(self, results_file_path: str) -> List:
        pass
