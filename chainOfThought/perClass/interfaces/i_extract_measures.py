"""
Chain-of-thought for IExtractMeasures:
1. Java-specific constructs: Java interface with a single abstract method; Vector<Measure> return type.
2. Python equivalents:
   - Interface -> ABC (Abstract Base Class) from abc module with @abstractmethod.
   - Vector<Measure> -> List[Measure] (Python list).
3. Risks/deviations:
   - Python ABCs are not enforced at import time; only at instantiation of a subclass will
     missing implementations raise TypeError.
"""

from abc import ABC, abstractmethod
from typing import List
from experimenthandling.measure import Measure


class IExtractMeasures(ABC):
    """Interface: extract measures from a simulation result file."""

    @abstractmethod
    def extract_measures(self, results_file_path: str) -> List[Measure]:
        """Parse the results file and return a list of Measure objects."""
        ...
