import logging
import queue as _queue
import threading
from queue import Queue

from experimenthandling.environment import Environment
from experimenthandling.experiment_result_handler import ExperimentResultHandler
from experimenthandling.options import Options
from interfaces.a_simulation_system_handler import ASimulationSystemHandler
from util.file_management import FileManagement

logger = logging.getLogger(__name__)


class ExperimentSimulatorHandler:
    """Simulation thread.

    Replaces Java's 'implements Runnable' pattern.
    """

    def __init__(
        self,
        environment_queue: Queue,
        results_queue: Queue,
        options: Options,
        glue_code: ASimulationSystemHandler,
        fm: FileManagement,
        plan: "ExperimentPlanGenerator",
    ) -> None:
        self.environment_queue: Queue = environment_queue
        self.results_queue: Queue = results_queue
        self.options: Options = options
        self.glue_code: ASimulationSystemHandler = glue_code
        self.fm: FileManagement = fm
        self.plan = plan

    def run(self) -> None:
        result = ExperimentResultHandler(self.results_queue, self.glue_code, self.fm, self.options)
        result_thread = threading.Thread(target=result.run, name="Result Thread")

        while True:
            try:
                logger.debug("Size of the Simulation Queue : %d", self.environment_queue.qsize())
                try:
                    env: Environment = self.environment_queue.get(block=True, timeout=0.1)
                except _queue.Empty:
                    if self.plan.is_finish and self.environment_queue.empty():
                        break
                    continue

                self.glue_code.start_simulation(self.options.path_parameters)
                result_path_for_this_simulation = (
                    env.path_save_result + "/results_sim" + str(env.get_id()) + ".txt"
                )
                logger.debug(result_path_for_this_simulation)
                self.fm.copy_file(self.options.path_to_simulator_result_file, result_path_for_this_simulation)
                self.fm.copy_file(
                    self.options.path_to_simulator_result_file,
                    self.options.path_simulator
                    + "/"
                    + env.path_save_result[env.path_save_result.rfind("/") + 1:]
                    + "/results_sim"
                    + str(env.id)
                    + ".txt",
                )

                self.results_queue.put(result_path_for_this_simulation)

                if self.plan.is_finish:
                    if self.environment_queue.empty():
                        logger.debug(
                            "It's empty ! and it's not the first time that we try to read the queue !"
                        )
                        break

            except Exception as e:
                import traceback
                traceback.print_exc()
                logger.error("Error in the run of the Thread Simulator")

        result_thread.start()
        result_thread.join()
