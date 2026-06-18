"""
Chain-of-thought for ExperimentSimulatorHandler:
1. Java-specific constructs:
   - implements Runnable.
   - Two BlockingQueues (environments, results).
   - environnmentQueue.take() — blocking call.
   - resultsQueue.add() — non-blocking.
   - Spawns a sub-thread (Result Thread) after the main loop.
   - do { ... } while(true) loop with break condition.
2. Python equivalents:
   - Runnable -> class with run() method.
   - BlockingQueue.take() -> queue.Queue.get() (blocks by default).
   - resultsQueue.add() -> queue.Queue.put_nowait().
   - Sub-thread: threading.Thread.
   - do-while -> while True with break.
3. Risks/deviations:
   - Java's do-while guarantees at least one iteration; Python while True does the same.
   - plan.isFinish is read without a lock; safe under CPython GIL for a single bool read.
   - environnmentQueue.isEmpty() -> queue.Queue.empty() (approximate under concurrency).
"""

import queue
import threading
import os
from typing import TYPE_CHECKING

from experimenthandling.options import Options
from experimenthandling.experiment_result_handler import ExperimentResultHandler

if TYPE_CHECKING:
    from experimenthandling.environment import Environment
    from experimenthandling.experiment_plan_generator import ExperimentPlanGenerator
    from interfaces.a_simulation_system_handler import ASimulationSystemHandler
    from util.file_management import FileManagement


class ExperimentSimulatorHandler:
    """Consumes environments from the planning queue, runs simulations, and queues results."""

    def __init__(
        self,
        environment_queue: queue.Queue,
        results_queue: queue.Queue,
        options: Options,
        glue_code: "ASimulationSystemHandler",
        fm: "FileManagement",
        plan: "ExperimentPlanGenerator",
    ):
        self.environment_queue = environment_queue
        self.results_queue = results_queue
        self.options = options
        self.glue_code = glue_code
        self.fm = fm
        self.plan = plan

    def run(self) -> None:
        """Main simulation loop."""
        result_handler = ExperimentResultHandler(
            self.results_queue, self.glue_code, self.fm, self.options
        )
        result_thread = threading.Thread(target=result_handler.run, name="Result Thread")

        while True:
            env: "Environment" = self.environment_queue.get()  # blocks
            self.glue_code.start_simulation(self.options.path_parameters)

            result_path = os.path.join(
                env.path_save_result, f"results_sim{env.get_id()}.txt"
            )
            self.fm.copy_file(self.options.path_to_simulator_result_file, result_path)

            # Also copy to simulator mirror directory
            sim_name = os.path.basename(env.path_save_result)
            mirror_path = os.path.join(
                self.options.path_simulator, sim_name, f"results_sim{env.id}.txt"
            )
            self.fm.copy_file(self.options.path_to_simulator_result_file, mirror_path)

            self.results_queue.put_nowait(result_path)
            self.environment_queue.task_done()

            if self.plan.is_finish and self.environment_queue.empty():
                break

        result_thread.start()
        result_thread.join()
