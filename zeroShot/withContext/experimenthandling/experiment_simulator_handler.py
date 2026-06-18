import logging
import threading

from experimenthandling.experiment_result_handler import ExperimentResultHandler
from experimenthandling.options import Options
from util.file_management import FileManagement

logger = logging.getLogger(__name__)


class ExperimentSimulatorHandler:
    """Second thread: runs each simulation environment."""

    def __init__(self, environment_queue, results_queue, options: Options, glue_code, fm: FileManagement, plan):
        self._environment_queue = environment_queue
        self._results_queue = results_queue
        self.options = options
        self._glue_code = glue_code
        self._fm = fm
        self._plan = plan

    def run(self) -> None:
        result_handler = ExperimentResultHandler(self._results_queue, self._glue_code, self._fm, self.options)
        result_thread = threading.Thread(target=result_handler.run, name="Result Thread")

        while True:
            try:
                logger.debug(f"Size of the Simulation Queue : {self._environment_queue.qsize()}")
                env = self._environment_queue.get()

                self._glue_code.start_simulation(self.options.get_path_parameters())

                result_path_for_this_simulation = (
                    env.path_save_result + "/results_sim" + str(env.get_id()) + ".txt"
                )
                logger.debug(result_path_for_this_simulation)

                self._fm.copy_file(self.options.path_to_simulator_result_file, result_path_for_this_simulation)
                self._fm.copy_file(
                    self.options.path_to_simulator_result_file,
                    self.options.path_simulator
                    + "/"
                    + env.path_save_result[env.path_save_result.rfind("/") + 1:]
                    + "/results_sim"
                    + str(env.id)
                    + ".txt"
                )

                self._results_queue.put(result_path_for_this_simulation)

                if self._plan.is_finish:
                    if self._environment_queue.empty():
                        logger.debug(
                            "It's empty! and it's not the first time that we try to read the queue!"
                        )
                        break

            except Exception as e:
                import traceback
                traceback.print_exc()
                logger.error("Error in the run of the Thread Simulator")

        result_thread.start()
