import logging
import queue
import threading
from typing import IO, Union

from experimenthandling.environment import Environment
from experimenthandling.experiment_plan_generator import ExperimentPlanGenerator
from experimenthandling.experiment_simulator_handler import ExperimentSimulatorHandler
from interfaces.a_simulation_system_handler import ASimulationSystemHandler
from util.file_management import FileManagement

logger = logging.getLogger(__name__)


class StartProgram:
    """Class to start the program. Use the static method start_program."""

    @staticmethod
    def start_program(path_config_file: Union[str, IO], glue_code: ASimulationSystemHandler) -> None:
        """
        Start the simulation program.

        :param path_config_file: Path to the config properties file, or a file-like object.
        :param glue_code: The glue code object implementing ASimulationSystemHandler.
        """
        fm = FileManagement()

        glue_code_class: ASimulationSystemHandler = glue_code

        o = fm.load_data_from_properties_file(path_config_file)

        list_param = glue_code_class.read_parameters_file(o.get_path_parameters())

        base_env = Environment(0, list_param, 1.0)

        planning_queue: queue.PriorityQueue = queue.PriorityQueue()
        result_queue: queue.PriorityQueue = queue.PriorityQueue()

        glue_code_class.set_options(o)

        if o.get_type_of_cut_off_planning() != "CRITERIA" or o.get_stop_criteria() > 0:
            planning = ExperimentPlanGenerator(planning_queue, base_env, o, glue_code_class, fm)
            planning_thread = threading.Thread(target=planning.run, name="Planning Thread")
            planning_thread.start()

            simulator = ExperimentSimulatorHandler(planning_queue, result_queue, o, glue_code_class, fm, planning)
            simulation_thread = threading.Thread(target=simulator.run, name="Simulation Thread")
            simulation_thread.start()
