import logging
from queue import Queue
from typing import List

from experimenthandling.measure import Measure
from experimenthandling.options import Options
from interfaces.a_simulation_system_handler import ASimulationSystemHandler
from util.file_management import FileManagement

logger = logging.getLogger(__name__)


class ExperimentResultHandler:
    """Displays where results are saved (third thread).

    Replaces Java's 'implements Runnable' pattern.
    """

    def __init__(
        self,
        results_queue: Queue,
        glue_code: ASimulationSystemHandler,
        fm: FileManagement,
        options: Options,
    ) -> None:
        self.results_queue: Queue = results_queue
        self.glue_code: ASimulationSystemHandler = glue_code
        self.fm: FileManagement = fm
        self.options: Options = options

    def run(self) -> None:
        if not self.results_queue.empty():
            items: List[str] = list(self.results_queue.queue)
            for str_path in items:
                logger.debug("Result queue string : %s", str_path)
                measures: List[Measure] = self.glue_code.extract_measures(str_path)
                position_of_last_slash = str_path.rfind("/")
                folder_to_save = str_path[:position_of_last_slash]
                logger.debug("Folder where it's saved : %s", folder_to_save)
                position_last_slash = folder_to_save.rfind("/")
                name_simulation = folder_to_save[position_last_slash + 1:]
                logger.debug("Name Simulation : %s", name_simulation)
                self.fm.create_measures_file(measures, folder_to_save + "/measures.txt")
                self.fm.copy_file(
                    folder_to_save + "/measures.txt",
                    self.options.path_simulator + "/" + name_simulation + "/measures.txt",
                )
        else:
            import threading
            threading.current_thread()  # No-op equivalent of Thread.currentThread().interrupt()
