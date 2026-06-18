"""
Chain-of-thought for IManageParametersFile:
1. Java-specific constructs: interface, method overloading (two readParametersFile signatures —
   one taking String path, one taking InputStream), Vector<Parameter>.
2. Python equivalents:
   - Interface -> ABC with @abstractmethod.
   - Method overloading -> two separate abstract methods (read_parameters_file and
     read_parameters_file_stream) because Python does not support overloading by signature.
   - InputStream -> typing.IO (file-like object).
   - Vector<Parameter> -> List[Parameter].
3. Risks/deviations:
   - The Java overload is split into two methods; callers must choose the correct one.
"""

from abc import ABC, abstractmethod
from typing import List, IO
from experimenthandling.parameter import Parameter


class IManageParametersFile(ABC):
    """Interface: read and write simulation parameter files."""

    @abstractmethod
    def read_parameters_file(self, parameters_file_path: str) -> List[Parameter]:
        """Read parameters from a file path."""
        ...

    @abstractmethod
    def read_parameters_file_stream(self, input_stream: IO) -> List[Parameter]:
        """Read parameters from a file-like object (InputStream equivalent)."""
        ...

    @abstractmethod
    def write_parameters_file(self, set_of_parameters: List[Parameter], location_to_store: str) -> None:
        """Write parameters to the given directory."""
        ...
