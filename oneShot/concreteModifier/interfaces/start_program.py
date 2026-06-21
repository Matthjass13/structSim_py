import logging
import queue
from typing import IO, Union

from experimenthandling.environment import Environment
from experimenthandling.options import Options
from util.file_management import FileManagement

logger = logging.getLogger(__name__)


class StartProgram:

    @staticmethod
    def start_program(path_config_file: Union[str, IO], glue_code) -> None:
        from experimenthandling.experiment_plan_generator import ExperimentPlanGenerator
        from experimenthandling.experiment_simulator_handler import ExperimentSimulatorHandler
        import threading

        fm = FileManagement()

        glue_code_class = glue_code

        if hasattr(path_config_file, 'read'):
            o = fm.load_data_from_properties_file_stream(path_config_file)
        else:
            o = fm.load_data_from_properties_file(path_config_file)

        if hasattr(path_config_file, 'read'):
            list_param = glue_code_class.read_parameters_file(o.get_path_parameters())
        else:
            list_param = glue_code_class.read_parameters_file(o.get_path_parameters())

        base_env = Environment(0, list_param, 1.0)

        planning_queue: queue.PriorityQueue = queue.PriorityQueue()
        result_queue: queue.PriorityQueue = queue.PriorityQueue()

        glue_code_class.set_options(o)

        if o.get_type_of_cutt_of_planning() != "CRITERIA" or o.get_stop_criteria() > 0:
            planning = ExperimentPlanGenerator(planning_queue, base_env, o, glue_code_class, fm)
            planning_thread = threading.Thread(target=planning.run, name="Planning Thread")
            planning_thread.start()

            simulator = ExperimentSimulatorHandler(
                planning_queue, result_queue, o, glue_code_class, fm, planning
            )
            simulation_thread = threading.Thread(target=simulator.run, name="Simulation Thread")
            simulation_thread.start()

            planning_thread.join()
            simulation_thread.join()
