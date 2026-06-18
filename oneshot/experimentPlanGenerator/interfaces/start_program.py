import threading
from queue import PriorityQueue
from typing import IO, List

from experimenthandling.environment import Environment
from experimenthandling.experiment_plan_generator import ExperimentPlanGenerator
from experimenthandling.experiment_simulator_handler import ExperimentSimulatorHandler
from experimenthandling.options import Options
from experimenthandling.parameter import Parameter
from interfaces.a_simulation_system_handler import ASimulationSystemHandler
from util.file_management import FileManagement


class StartProgram:

    @staticmethod
    def start_program(path_config_file, glue_code: ASimulationSystemHandler) -> None:
        fm = FileManagement()

        glue_code_class: ASimulationSystemHandler = glue_code

        o: Options = fm.load_data_from_properties_file(path_config_file)

        list_param: List[Parameter] = glue_code_class.read_parameters_file(o.path_parameters)

        base_env = Environment(0, list_param, 1.0)

        queue: PriorityQueue = PriorityQueue()
        result_queue: PriorityQueue = PriorityQueue()

        glue_code_class.set_options(o)

        if o.type_of_cut_off_planning != "CRITERIA" or o.stop_criteria > 0:
            planning = ExperimentPlanGenerator(queue, base_env, o, glue_code_class, fm)
            planning_thread = threading.Thread(target=planning.run, name="Planning Thread")
            planning_thread.start()

            simulator = ExperimentSimulatorHandler(queue, result_queue, o, glue_code_class, fm, planning)
            simulation_thread = threading.Thread(target=simulator.run, name="Simulation Thread")
            simulation_thread.start()
