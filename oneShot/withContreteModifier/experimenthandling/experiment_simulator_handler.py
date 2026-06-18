import logging
import queue
import threading

from experimenthandling.environment import Environment
from experimenthandling.options import Options
from util.file_management import FileManagement

logger = logging.getLogger(__name__)


class ExperimentSimulatorHandler:

    def __init__(self, environment_queue: queue.Queue, results_queue: queue.Queue,
                 options: Options, glue_code, fm: FileManagement, plan):
        self.environment_queue = environment_queue
        self.results_queue = results_queue
        self.options = options
        self.glue_code = glue_code
        self.fm = fm
        self.plan = plan

    def run(self) -> None:
        from experimenthandling.experiment_result_handler import ExperimentResultHandler

        result = ExperimentResultHandler(self.results_queue, self.glue_code, self.fm, self.options)
        result_thread = threading.Thread(target=result.run, name="Result Thread")

        while True:
            try:
                logger.debug(f"Size of the Simulation Queue : {self.environment_queue.qsize()}")
                env: Environment = self.environment_queue.get()

                self.glue_code.start_simulation(self.options.get_path_parameters())

                result_path = (
                    env.path_save_result
                    + "/results_sim"
                    + str(env.get_id())
                    + ".txt"
                )
                logger.debug(result_path)

                self.fm.copy_file(self.options.path_to_simulator_result_file, result_path)

                sim_folder = env.path_save_result[env.path_save_result.rfind("/") + 1:]
                self.fm.copy_file(
                    self.options.path_to_simulator_result_file,
                    self.options.path_simulator
                    + "/" + sim_folder
                    + "/results_sim" + str(env.id) + ".txt"
                )

                self.results_queue.put(result_path)

                if self.plan.is_finish and self.environment_queue.empty():
                    logger.debug(
                        "It's empty ! and it's not the first time that we try to read the queue !"
                    )
                    break

            except Exception as e:
                import traceback
                traceback.print_exc()
                logger.error("Error in the run of the Thread Simulator")

        result_thread.start()
