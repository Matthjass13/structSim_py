"""
Chain-of-thought for StartProgram:
1. Java-specific constructs:
   - Static method startProgram accepting InputStream (classpath resource).
   - PriorityBlockingQueue for both planning queue and result queue.
   - Explicit Thread creation with setName().
   - Simulation.class.getClassLoader().getResourceAsStream() for classpath loading.
   - Cast: (ASimulationSystemHandler) glueCode.
2. Python equivalents:
   - @staticmethod in a class.
   - queue.PriorityQueue (thread-safe; items must support __lt__; Environment implements __lt__).
     For the result queue (strings) we use queue.Queue since strings are comparable.
   - threading.Thread(target=runnable.run, name="...").
   - Classpath resource loading: accept a file path string or file-like object directly;
     Python has no classpath concept, so callers pass an open file or path.
   - isinstance check replaces cast.
3. Risks/deviations:
   - PriorityBlockingQueue in Java orders by natural ordering (Environment.compareTo);
     Python's PriorityQueue requires (priority, item) tuples or __lt__ on items.
     We add __lt__ to Environment based on probability (ascending, matching Java).
   - The result queue is PriorityBlockingQueue<String> in Java — strings have natural ordering.
     We use queue.Queue for simplicity since ordering of result paths doesn't matter.
   - Thread.join() is not called in Java either; threads run as daemons until done.
"""

import queue
import threading

from experimenthandling.environment import Environment
from experimenthandling.experiment_plan_generator import ExperimentPlanGenerator
from experimenthandling.experiment_simulator_handler import ExperimentSimulatorHandler
from interfaces.a_simulation_system_handler import ASimulationSystemHandler
from util.file_management import FileManagement


class StartProgram:
    """Entry point that wires up the three-thread pipeline."""

    @staticmethod
    def start_program(config_source, glue_code) -> None:
        """
        config_source: path string or file-like object pointing to config.properties.
        glue_code: an ASimulationSystemHandler instance.
        """
        fm = FileManagement()
        if not isinstance(glue_code, ASimulationSystemHandler):
            raise TypeError("glue_code must be an ASimulationSystemHandler")
        glue_code_class: ASimulationSystemHandler = glue_code

        o = fm.load_data_from_properties_file(config_source)

        # Load parameters
        params_source = o.path_parameters  # path string; caller can also pass open file
        list_param = glue_code_class.read_parameters_file(params_source)

        base_env = Environment(0, list_param, 1.0)

        planning_queue: queue.PriorityQueue = queue.PriorityQueue()
        result_queue: queue.Queue = queue.Queue()

        glue_code_class.options = o

        type_cutoff = o.type_of_cutt_of_planning or ""
        if type_cutoff != "CRITERIA" or o.stop_criteria > 0:
            planning = ExperimentPlanGenerator(planning_queue, base_env, o, glue_code_class, fm)
            planning_thread = threading.Thread(target=planning.run, name="Planning Thread", daemon=True)
            planning_thread.start()

            simulator = ExperimentSimulatorHandler(planning_queue, result_queue, o, glue_code_class, fm, planning)
            sim_thread = threading.Thread(target=simulator.run, name="Simulation Thread", daemon=True)
            sim_thread.start()

            planning_thread.join()
            sim_thread.join()
