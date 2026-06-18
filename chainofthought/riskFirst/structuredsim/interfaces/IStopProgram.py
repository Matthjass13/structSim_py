from abc import ABC, abstractmethod


class IStopProgram(ABC):
    """Interface for graceful program termination."""

    @abstractmethod
    def stop_program(self) -> None:
        """Stop the program / simulation process."""
