import queue
import threading
from experimenthandling.environment import Environment
from experimenthandling.experiment_plan_generator import ExperimentPlanGenerator
from experimenthandling.experiment_simulator_handler import ExperimentSimulatorHandler
from util.file_management import FileManagement


class StartProgram:

    @staticmethod
    def start_program(config_file, glue_code):
        fm = FileManagement()

        options = fm.load_data_from_properties_file(config_file)

        with open(options.get_path_parameters(), encoding="utf-8") as f:
            list_param = glue_code.read_parameters_file(f)

        base_env = Environment(0, list_param, 1)

        planning_queue = queue.PriorityQueue()
        result_queue = queue.PriorityQueue()

        glue_code.set_options(options)

        if options.get_type_of_cuttof_planning() != "CRITERIA" or options.get_stop_criteria() > 0:
            planning = ExperimentPlanGenerator(planning_queue, base_env, options, glue_code, fm)
            planning_thread = threading.Thread(target=planning.run, name="Planning Thread")
            planning_thread.start()

            simulator = ExperimentSimulatorHandler(planning_queue, result_queue, options, glue_code, fm, planning)
            simulation_thread = threading.Thread(target=simulator.run, name="Simulation Thread")
            simulation_thread.start()
