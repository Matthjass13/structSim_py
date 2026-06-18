import logging
import threading

from experimenthandling.experiment_result_handler import ExperimentResultHandler
from experimenthandling.options import Options
from util.file_management import FileManagement

logger = logging.getLogger(__name__)


class ExperimentSimulatorHandler:
    """
    Thread 2 – consumes the environment queue and drives the simulator.

    For each environment dequeued:
    1. Calls glue_code.start_simulation() to run the external tool.
    2. Copies the result file to the per-simulation output folder.
    3. Pushes the result file path onto the results queue.

    When the planning thread signals it is finished and the environment
    queue is empty, the simulator starts Thread 3 (ExperimentResultHandler).
    """

    def __init__(self, environment_queue, results_queue, options: Options, glue_code, fm: FileManagement, plan):
        self._environment_queue = environment_queue
        self._results_queue = results_queue
        self.options = options
        self._glue_code = glue_code
        self._fm = fm
        self._plan = plan

    def run(self) -> None:
        result_handler = ExperimentResultHandler(
            self._results_queue, self._glue_code, self._fm, self.options
        )
        result_thread = threading.Thread(target=result_handler.run, name="Result Thread")

        while True:
            try:
                logger.debug("Simulation queue size: %d", self._environment_queue.qsize())
                env = self._environment_queue.get(block=True, timeout=1)

                self._glue_code.start_simulation(self.options.get_path_parameters())

                result_path = (
                    env.path_save_result + "/results_sim" + str(env.get_id()) + ".txt"
                )
                logger.debug(result_path)

                self._fm.copy_file(self.options.path_to_simulator_result_file, result_path)

                sim_folder_name = env.path_save_result[env.path_save_result.rfind("/") + 1:]
                self._fm.copy_file(
                    self.options.path_to_simulator_result_file,
                    self.options.path_simulator
                    + "/"
                    + sim_folder_name
                    + "/results_sim"
                    + str(env.id)
                    + ".txt",
                )

                self._results_queue.put(result_path)

            except Exception:
                # Timeout from queue.get() – check termination condition
                pass

            if self._plan.is_finish and self._environment_queue.empty():
                logger.debug("Planning finished and queue is empty – stopping simulation loop.")
                break

        result_thread.start()
        result_thread.join()
