from abc import ABC, abstractmethod


class IStopProgram(ABC):
    """Interface for stopping the program gracefully."""

    @abstractmethod
    def stop_program(self) -> None: ...
