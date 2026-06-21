import queue
import threading

from util.file_management import FileManagement
from experimenthandling.environment import Environment
from experimenthandling.experiment_plan_generator import ExperimentPlanGenerator
from experimenthandling.experiment_simulator_handler import ExperimentSimulatorHandler


class StartProgram:
    @staticmethod
    def start_program(path_config_file, glue_code) -> None:
        """
        Wire up the planning and simulator threads and start the experiment.

        path_config_file: str (file path) or file-like object for config.properties
        glue_code: ASimulationSystemHandler instance
        """
        fm = FileManagement()
        glue_code_class = glue_code  # ASimulationSystemHandler

        o = fm.load_data_from_properties_file(path_config_file)

        # Read the parameters file (may be a path or a stream)
        params_path = o.get_path_parameters()
        list_param = glue_code_class.read_parameters_file(params_path)

        base_env = Environment(0, list_param, 1.0)

        environment_queue = queue.Queue()
        result_queue = queue.Queue()

        glue_code_class.set_options(o)

        if (not o.get_type_of_cutt_of_planning() == "CRITERIA"
                or o.get_stop_criteria() > 0):

            planning = ExperimentPlanGenerator(
                environment_queue, base_env, o, glue_code_class, fm
            )
            planning.name = "Planning Thread"
            planning.start()

            simulator = ExperimentSimulatorHandler(
                environment_queue, result_queue, o, glue_code_class, fm, planning
            )
            simulator.name = "Simulation Thread"
            simulator.start()

            planning.join()
            simulator.join()
