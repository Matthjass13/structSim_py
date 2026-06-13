import logging
import queue
import threading

from experimenthandling.experiment_result_handler import ExperimentResultHandler

logger = logging.getLogger(__name__)


class ExperimentSimulatorHandler:
    def __init__(self, environment_queue: queue.Queue, results_queue: queue.Queue,
                 options, glue_code, fm, plan):
        self.environment_queue = environment_queue
        self.results_queue = results_queue
        self.options = options
        self.glue_code = glue_code
        self.fm = fm
        self.plan = plan

    def run(self):
        result_handler = ExperimentResultHandler(self.results_queue, self.glue_code, self.fm, self.options)
        result_thread = threading.Thread(target=result_handler.run, name="Result Thread")

        while True:
            try:
                logger.debug(f"Size of the Simulation Queue : {self.environment_queue.qsize()}")
                env = self.environment_queue.get(block=True, timeout=1)

                self.glue_code.start_simulation(self.options.get_path_parameters())
                result_path_for_this_simulation = (
                    f"{env.path_save_result}/results_sim{env.get_id()}.txt"
                )
                logger.debug(result_path_for_this_simulation)
                self.fm.copy_file(self.options.path_to_simulator_result_file, result_path_for_this_simulation)

                sim_sub_folder = env.path_save_result[env.path_save_result.rfind("/") + 1:]
                self.fm.copy_file(
                    self.options.path_to_simulator_result_file,
                    f"{self.options.path_simulator}/{sim_sub_folder}/results_sim{env.id}.txt"
                )

                self.results_queue.put(result_path_for_this_simulation)

                if self.plan.is_finish and self.environment_queue.empty():
                    logger.debug("It's empty ! and it's not the first time that we try to read the queue !")
                    break

            except queue.Empty:
                if self.plan.is_finish:
                    break
            except Exception as e:
                logger.error(f"Error in the run of the Thread Simulator: {e}")

        result_thread.start()
        result_thread.join()
