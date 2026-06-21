import logging
import queue
from typing import List

from experimenthandling.Options import Options

logger = logging.getLogger(__name__)


class ExperimentResultHandler:
    """
    Third thread: extracts measures from result files and writes measures.txt.

    Java BlockingQueue iteration → iterate over a standard queue.Queue by draining it.
    """

    def __init__(self, results_queue: queue.Queue, glue_code, fm, options: Options):
        self.results_queue = results_queue
        self.glue_code = glue_code
        self.fm = fm
        self.options = options

    def run(self) -> None:
        items: List[str] = []
        while not self.results_queue.empty():
            try:
                items.append(self.results_queue.get_nowait())
            except queue.Empty:
                break

        if not items:
            return

        for result_path in items:
            logger.debug(f"Result queue string : {result_path}")
            measures = self.glue_code.extract_measures(result_path)
            pos = result_path.rfind("/")
            folder_to_save = result_path[:pos]
            logger.debug(f"Folder where it's saved : {folder_to_save}")
            pos_last = folder_to_save.rfind("/")
            name_simulation = folder_to_save[pos_last + 1:]
            logger.debug(f"Name Simulation : {name_simulation}")
            self.fm.create_measures_file(measures, folder_to_save + "/measures.txt")
            self.fm.copy_file(
                folder_to_save + "/measures.txt",
                self.options.path_simulator + "/" + name_simulation + "/measures.txt",
            )
