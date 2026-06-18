"""
Chain-of-thought for ExperimentResultHandler:
1. Java-specific constructs:
   - implements Runnable.
   - BlockingQueue<String>.
   - String path manipulation (lastIndexOf, substring).
   - Thread.currentThread().interrupt() when queue is empty.
2. Python equivalents:
   - Runnable -> class with run() method.
   - BlockingQueue -> queue.Queue.
   - Path manipulation -> os.path / str methods.
   - Thread interrupt -> no direct equivalent; we simply return (the thread exits naturally).
3. Risks/deviations:
   - Java's for-each on a BlockingQueue iterates snapshot contents; Python queue.Queue does
     not support iteration. We drain all items with non-blocking get_nowait() calls instead.
   - Thread interruption is not replicated (Python threads cannot be interrupted from outside);
     we exit the run() method cleanly.
"""

import queue
import os
from typing import TYPE_CHECKING

from experimenthandling.options import Options

if TYPE_CHECKING:
    from interfaces.a_simulation_system_handler import ASimulationSystemHandler
    from util.file_management import FileManagement


class ExperimentResultHandler:
    """Processes simulation results from the results queue."""

    def __init__(
        self,
        results_queue: queue.Queue,
        glue_code: "ASimulationSystemHandler",
        fm: "FileManagement",
        options: Options,
    ):
        self.results_queue = results_queue
        self.glue_code = glue_code
        self.fm = fm
        self.options = options

    def run(self) -> None:
        """Process all pending results in the queue."""
        if not self.results_queue.empty():
            while True:
                try:
                    result_path = self.results_queue.get_nowait()
                except queue.Empty:
                    break

                measures = self.glue_code.extract_measures(result_path)

                # Derive folder and simulation name from result path
                pos_last_slash = result_path.rfind("/")
                folder_to_save = result_path[:pos_last_slash]
                pos_last_slash2 = folder_to_save.rfind("/")
                name_simulation = folder_to_save[pos_last_slash2 + 1:]

                measures_path = os.path.join(folder_to_save, "measures.txt")
                self.fm.create_measures_file(measures, measures_path)
                self.fm.copy_file(
                    measures_path,
                    os.path.join(self.options.path_simulator, name_simulation, "measures.txt"),
                )
                self.results_queue.task_done()
        else:
            # Queue empty — nothing to process; thread exits naturally (mirrors interrupt())
            return
