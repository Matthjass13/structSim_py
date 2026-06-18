import logging
import threading

from experimenthandling.options import Options
from util.file_management import FileManagement

logger = logging.getLogger(__name__)


class ExperimentResultHandler:
    """
    Third thread: displays where the results are saved and extracts measures.
    """

    def __init__(self, results_queue, glue_code, fm: FileManagement, options: Options):
        self._results_queue = results_queue
        self._glue_code = glue_code
        self._fm = fm
        self.options = options

    def run(self) -> None:
        if not self._results_queue.empty():
            items = []
            while not self._results_queue.empty():
                try:
                    items.append(self._results_queue.get_nowait())
                except Exception:
                    break

            for str_path in items:
                logger.debug(f"Result queue string : {str_path}")
                measures = self._glue_code.extract_measures(str_path)
                position_of_last_slash = str_path.rfind("/")
                folder_to_save = str_path[:position_of_last_slash]
                logger.debug(f"Folder where it's saved : {folder_to_save}")
                position_last_slash = folder_to_save.rfind("/")
                name_simulation = folder_to_save[position_last_slash + 1:]
                logger.debug(f"Name Simulation : {name_simulation}")
                self._fm.create_measures_file(measures, folder_to_save + "/measures.txt")
                self._fm.copy_file(
                    folder_to_save + "/measures.txt",
                    self.options.path_simulator + "/" + name_simulation + "/measures.txt"
                )
        else:
            threading.current_thread()  # equivalent to interrupt — no-op in Python
