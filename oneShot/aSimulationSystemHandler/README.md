# aSimulationSystemHandler – Python Migration

## Original Prompt

In the "originalJavaCode" folder of the repository is the source code of a Java simulation framework (20 classes, Maven project). The framework is used to run structured simulations: it will read a parameter file and a configuration file as inputs and run algorithms, to produce output files with modified parameters. Migrate the entire project to Python and put the output files in a "aSimulationSystemHandler" folder to be created in the "oneshot" folder. In this created folder, also put the current prompt in a readme file. The migration must:
- Preserve the complete class hierarchy and object-oriented architecture
- Maintain all existing logic without adding or removing functionality
- Use appropriate Python libraries and modern Python idioms
- Follow Python naming conventions (snake_case for methods and variables, PascalCase for classes)
- Produce a requirements.txt in the output folder

Use the following migration as a reference and follow the same patterns. The original Java file is at originalJavaCode/interfaces/ASimulationSystemHandler.java. Its Python migration is provided below, enclosed in triple double quotes:

```python
from typing import List, Optional

from interfaces.i_start_simulation import IStartSimulation
from interfaces.i_stop_program import IStopProgram
from interfaces.i_manage_parameters_file import IManageParametersFile
from interfaces.i_extract_measures import IExtractMeasures
from interfaces.i_manage_modifier import IManageModifier
from interfaces.a_modifier import AModifier
from experimenthandling.options import Options


class ASimulationSystemHandler(
    IStartSimulation,
    IStopProgram,
    IManageParametersFile,
    IExtractMeasures,
    IManageModifier,
):
    """Abstract class combining all handler interfaces for the glue code layer.

    Replaces Java's 'implements I1, I2, I3, I4, I5' with Python multiple
    inheritance from ABC classes. Any concrete subclass must implement:
    start_simulation, stop_program, read_parameters_file,
    read_parameters_file_from_stream, write_parameters_file,
    extract_measures, and initiate_modifier_list.
    """

    def __init__(self) -> None:
        self._options: Optional[Options] = None
        self._list_modifier_class: List[AModifier] = []

    @property
    def options(self) -> Optional[Options]:
        """The simulation options."""
        return self._options

    @options.setter
    def options(self, options: Options) -> None:
        self._options = options

    @property
    def list_modifier_class(self) -> List[AModifier]:
        """The list of modifier instances."""
        return self._list_modifier_class

    @list_modifier_class.setter
    def list_modifier_class(self, list_modifier_class: List[AModifier]) -> None:
        self._list_modifier_class = list_modifier_class
```

---

## Project Structure

```
aSimulationSystemHandler/
├── README.md
├── requirements.txt
├── experimenthandling/
│   ├── __init__.py
│   ├── environment.py          # Environment  (Environment.java)
│   ├── experiment_plan_generator.py   # ExperimentPlanGenerator
│   ├── experiment_result_handler.py   # ExperimentResultHandler
│   ├── experiment_simulator_handler.py # ExperimentSimulatorHandler
│   ├── measure.py              # Measure
│   ├── options.py              # Options
│   └── parameter.py            # Parameter
├── interfaces/
│   ├── __init__.py
│   ├── a_modifier.py           # AModifier
│   ├── a_simulation_system_handler.py  # ASimulationSystemHandler
│   ├── i_extract_measures.py   # IExtractMeasures
│   ├── i_manage_modifier.py    # IManageModifier
│   ├── i_manage_parameters_file.py # IManageParametersFile
│   ├── i_start_simulation.py   # IStartSimulation
│   ├── i_stop_program.py       # IStopProgram
│   └── start_program.py        # StartProgram
├── util/
│   ├── __init__.py
│   └── file_management.py      # FileManagement
└── gluecode/
    ├── __init__.py
    ├── concrete_modifier.py    # ConcreteModifier
    ├── my_simulator.py         # MySimulator
    ├── simple_simulation_handler.py # SimpleSimulationHandler
    └── simulation.py           # Simulation (main entry point)
```

## Java → Python Mapping

| Java concept | Python equivalent |
|---|---|
| `abstract class` / `interface` | `ABC` with `@abstractmethod` |
| Multiple `implements` | Multiple inheritance from ABC bases |
| `Vector<T>` | `List[T]` |
| `BlockingQueue` / `PriorityBlockingQueue` | `queue.Queue` / `queue.PriorityQueue` |
| `Runnable` + `Thread` | `threading.Thread(target=obj.run)` |
| `Calendar` + time units | `datetime.timedelta` |
| `Properties` file | Plain key=value parsing |
| `Logger` (log4j) | `logging` module |
| `InputStream` | `IO[bytes]` / file object |
| Getters / setters | Python properties + explicit `get_*`/`set_*` methods |

## Running

```bash
cd aSimulationSystemHandler
python gluecode/simulation.py
```

Requires a `config.properties` file in the working directory.
