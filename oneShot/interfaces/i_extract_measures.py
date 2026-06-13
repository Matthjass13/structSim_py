from abc import ABC, abstractmethod


class IExtractMeasures(ABC):

    @abstractmethod
    def extract_measures(self, results_file_path: str) -> list:
        pass
