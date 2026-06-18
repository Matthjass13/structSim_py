"""
Chain-of-thought for Environment:
1. Java-specific constructs:
   - implements Comparable<Environment> with compareTo.
   - java.util.Vector<Parameter> for setOfParameters.
   - java.util.List<String> (ArrayList) for trace.
   - Multiple constructors (3-arg, copy, no-arg).
   - Deep copy of Vector<Parameter> in copy constructor.
2. Python equivalents:
   - Comparable: implement __lt__ and __eq__ (functools.total_ordering or manual) so that
     environments can be sorted by probability.
   - Vector/ArrayList -> list (Python list is thread-safe for append under the GIL, sufficient here).
   - Multiple constructors -> classmethod factories (from_id_env for copy constructor).
   - Deep copy: use copy.deepcopy or manual list comprehension.
3. Risks/deviations:
   - Java Vector is synchronized; Python list is not. For multi-threaded use a threading.Lock
     would be needed, but the Java code doesn't appear to mutate the vector concurrently.
   - compareTo returns int in Java; Python rich comparison returns bool.
"""

import copy
from typing import List, Optional
from experimenthandling.parameter import Parameter


class Environment:
    """Represents a simulation environment with parameters and probability."""

    def __init__(self, id_: int, set_of_parameters: List[Parameter], probability: float):
        self.id = id_
        self.set_of_parameters: List[Parameter] = set_of_parameters
        self.probability: float = probability
        self.path_save_result: Optional[str] = None
        self.trace: List[str] = []

    @classmethod
    def from_id_env(cls, id_: int, e: "Environment") -> "Environment":
        """Copy constructor: deep-copies parameters and trace from e."""
        new_env = cls(id_, [], e.probability)
        new_env.set_of_parameters = [Parameter.from_parameter(p) for p in e.set_of_parameters]
        new_env.trace = list(e.trace)
        new_env.path_save_result = e.path_save_result
        return new_env

    @classmethod
    def default(cls) -> "Environment":
        """No-arg constructor equivalent: id=1, empty params, probability=1."""
        return cls(1, [], 1.0)

    # Comparison by probability (mirrors compareTo)
    def __lt__(self, other: "Environment") -> bool:
        return self.probability < other.probability

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Environment):
            return NotImplemented
        return self.probability == other.probability

    def __le__(self, other: "Environment") -> bool:
        return self.probability <= other.probability

    def __gt__(self, other: "Environment") -> bool:
        return self.probability > other.probability

    def __ge__(self, other: "Environment") -> bool:
        return self.probability >= other.probability

    # Getters / setters
    def get_id(self) -> int:
        return self.id

    def set_id(self, id_: int) -> None:
        self.id = id_

    def get_set_of_parameters(self) -> List[Parameter]:
        return self.set_of_parameters

    def set_set_of_parameters(self, params: List[Parameter]) -> None:
        self.set_of_parameters = params

    def get_probability(self) -> float:
        return self.probability

    def set_probability(self, p: float) -> None:
        self.probability = p

    def get_path_save_result(self) -> Optional[str]:
        return self.path_save_result

    def set_path_save_result(self, path: str) -> None:
        self.path_save_result = path

    def get_trace(self) -> List[str]:
        return self.trace

    def to_string_modifier(self) -> str:
        """Returns a human-readable summary including trace."""
        return (
            f"Environment id={self.id} probability={self.probability} "
            f"trace={self.trace} path={self.path_save_result}"
        )

    def __str__(self) -> str:
        params_str = ", ".join(str(p) for p in self.set_of_parameters)
        return (
            f"Environment[id={self.id}, probability={self.probability}, "
            f"params=[{params_str}], trace={self.trace}]"
        )
