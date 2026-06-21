import queue
import threading

from experimenthandling.environment import Environment
from experimenthandling.experiment_plan_generator import ExperimentPlanGenerator
from experimenthandling.experiment_simulator_handler import ExperimentSimulatorHandler
from util.file_management import FileManagement


class StartProgram:
    @staticmethod
    def start_program(config_file, glue_code):
        """
        Entry point for the framework.

        :param config_file: Path string or file-like object pointing to the config.properties file.
        :param glue_code: An instance of ASimulationSystemHandler (concrete glue code).
        """
        fm = FileManagement()

        options = fm.load_data_from_properties_file(config_file)

        list_param = glue_code.read_parameters_file(options.get_path_parameters())

        base_env = Environment(0, list_param, 1.0)

        planning_queue = queue.Queue()
        result_queue = queue.Queue()

        glue_code.set_options(options)

        type_plan = options.get_type_of_cutt_of_planning()
        if type_plan != "CRITERIA" or options.get_stop_criteria() > 0:
            planning = ExperimentPlanGenerator(planning_queue, base_env, options, glue_code, fm)
            planning_thread = threading.Thread(target=planning.run, name="Planning Thread")
            planning_thread.start()

            simulator = ExperimentSimulatorHandler(planning_queue, result_queue, options, glue_code, fm, planning)
            simulation_thread = threading.Thread(target=simulator.run, name="Simulation Thread")
            simulation_thread.start()

            planning_thread.join()
            simulation_thread.join()
