from abc import ABC, abstractmethod


class IStopProgram(ABC):
    @abstractmethod
    def stop_program(self):
        pass
