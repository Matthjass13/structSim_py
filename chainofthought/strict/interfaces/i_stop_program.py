from abc import ABC, abstractmethod


class IStopProgram(ABC):
    @abstractmethod
    def stop_program(self) -> None:
        """Stop the program."""
        pass
