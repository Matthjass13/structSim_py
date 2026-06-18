import queue
import threading
from typing import IO, Union

from experimenthandling.environment import Environment
from experimenthandling.experiment_plan_generator import ExperimentPlanGenerator
from experimenthandling.experiment_simulator_handler import ExperimentSimulatorHandler
from interfaces.a_simulation_system_handler import ASimulationSystemHandler
from util.file_management import FileManagement


class StartProgram:
    """
    Orchestrates the three-thread simulation pipeline:
      Thread 1 – ExperimentPlanGenerator  (generates environments)
      Thread 2 – ExperimentSimulatorHandler (runs the simulator)
      Thread 3 – ExperimentResultHandler   (extracts measures; started by Thread 2)
    """

    @staticmethod
    def start_program(config_source: Union[str, IO], glue_code: ASimulationSystemHandler) -> None:
        fm = FileManagement()
        options = fm.load_data_from_properties_file(config_source)

        glue_code.set_options(options)

        # Load base parameters
        with open(options.get_path_parameters(), "r", encoding="utf-8") as fh:
            params = glue_code.read_parameters_file_from_stream(fh)

        base_env = Environment(0, params, 1.0)

        env_queue: queue.PriorityQueue = queue.PriorityQueue()
        result_queue: queue.Queue = queue.Queue()

        # Guard against infinite CRITERIA trees
        if (
            options.get_type_of_cut_off_planning() != "CRITERIA"
            or options.get_stop_criteria() > 0
        ):
            planning = ExperimentPlanGenerator(env_queue, base_env, options, glue_code, fm)
            planning_thread = threading.Thread(target=planning.run, name="Planning Thread")
            planning_thread.start()

            simulator = ExperimentSimulatorHandler(env_queue, result_queue, options, glue_code, fm, planning)
            simulation_thread = threading.Thread(target=simulator.run, name="Simulation Thread")
            simulation_thread.start()
