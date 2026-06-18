"""
Chain-of-thought for IStopProgram:
1. Java-specific constructs: single-method interface.
2. Python equivalents: ABC with one @abstractmethod.
3. Risks/deviations: None.
"""

from abc import ABC, abstractmethod


class IStopProgram(ABC):
    """Interface: gracefully stop the simulation program."""

    @abstractmethod
    def stop_program(self) -> None:
        ...
