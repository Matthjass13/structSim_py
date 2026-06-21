import logging
import queue
import threading

from experimenthandling.environment import Environment
from experimenthandling.experiment_result_handler import ExperimentResultHandler
from experimenthandling.options import Options

logger = logging.getLogger(__name__)


class ExperimentSimulatorHandler:
    """
    Second thread: dequeues environments, runs the simulation, and posts result paths.

    Java BlockingQueue.take() (blocking) → queue.Queue.get(block=True, timeout=…).
    The result thread is spawned only after all simulations finish, exactly as in Java.
    """

    def __init__(self, environment_queue: queue.Queue, results_queue: queue.Queue,
                 options: Options, glue_code, fm, plan):
        self.environment_queue = environment_queue
        self.results_queue = results_queue
        self.options = options
        self.glue_code = glue_code
        self.fm = fm
        self.plan = plan

    def run(self) -> None:
        result_handler = ExperimentResultHandler(self.results_queue, self.glue_code, self.fm, self.options)
        result_thread = threading.Thread(target=result_handler.run, name="Result Thread")

        while True:
            try:
                logger.debug(f"Size of the Simulation Queue : {self.environment_queue.qsize()}")
                env: Environment = self.environment_queue.get(block=True, timeout=0.5)

                self.glue_code.start_simulation(self.options.get_path_parameters())
                result_path = env.path_save_result + "/results_sim" + str(env.get_id()) + ".txt"
                logger.debug(result_path)
                self.fm.copy_file(self.options.path_to_simulator_result_file, result_path)

                sim_folder_name = env.path_save_result[env.path_save_result.rfind("/") + 1:]
                self.fm.copy_file(
                    self.options.path_to_simulator_result_file,
                    self.options.path_simulator + "/" + sim_folder_name + "/results_sim" + str(env.id) + ".txt",
                )

                self.results_queue.put(result_path)

                if self.plan.is_finish and self.environment_queue.empty():
                    logger.debug("Queue is empty and planning is finished!")
                    break

            except queue.Empty:
                if self.plan.is_finish:
                    break
            except Exception as e:
                logger.error(f"Error in simulation thread: {e}")

        result_thread.start()
        result_thread.join()
