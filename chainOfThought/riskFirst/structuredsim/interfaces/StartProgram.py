import importlib.resources
import queue
import threading
from io import IOBase
from typing import IO, Union

from experimenthandling.environment import Environment
from experimenthandling.ExperimentPlanGenerator import ExperimentPlanGenerator
from experimenthandling.ExperimentSimulatorHandler import ExperimentSimulatorHandler
from interfaces.a_simulation_system_handler import ASimulationSystemHandler
from util.file_management import FileManagement


class StartProgram:
    """
    Static coordinator class that initialises and starts all three threads.

    Java static startProgram() → Python @staticmethod start_program().
    Java ClassLoader.getResourceAsStream() for loading parameters.txt is
    replaced by importlib.resources / plain file path, depending on what
    the caller provides in config's pathParameters.
    """

    @staticmethod
    def start_program(config_file: Union[str, IO], glue_code: ASimulationSystemHandler) -> None:
        fm = FileManagement()

        options = fm.load_data_from_properties_file(config_file)

        # Load parameters: the value in config may be a plain path or a resource name
        params_source = options.get_path_parameters()
        list_param = glue_code.read_parameters_file(params_source)

        base_env = Environment(0, list_param, 1.0)

        planning_queue: queue.Queue = queue.Queue()
        result_queue: queue.Queue = queue.Queue()

        glue_code.set_options(options)

        type_plan = options.get_type_of_cutt_of_planning()
        if type_plan != "CRITERIA" or options.get_stop_criteria() > 0:
            planning = ExperimentPlanGenerator(planning_queue, base_env, options, glue_code, fm)
            planning_thread = threading.Thread(target=planning.run, name="Planning Thread")
            planning_thread.start()

            simulator = ExperimentSimulatorHandler(
                planning_queue, result_queue, options, glue_code, fm, planning
            )
            simulation_thread = threading.Thread(target=simulator.run, name="Simulation Thread")
            simulation_thread.start()
