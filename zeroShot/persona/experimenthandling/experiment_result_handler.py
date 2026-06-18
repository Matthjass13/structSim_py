import logging

from experimenthandling.options import Options
from util.file_management import FileManagement

logger = logging.getLogger(__name__)


class ExperimentResultHandler:
    """
    Thread 3 – processes the results queue.

    For every result file path in the queue, extracts measures via the
    glue-code and writes a measures.txt file next to the result file.
    """

    def __init__(self, results_queue, glue_code, fm: FileManagement, options: Options):
        self._results_queue = results_queue
        self._glue_code = glue_code
        self._fm = fm
        self.options = options

    def run(self) -> None:
        # Drain whatever is currently in the queue
        items = []
        while not self._results_queue.empty():
            try:
                items.append(self._results_queue.get_nowait())
            except Exception:
                break

        if not items:
            return

        for result_path in items:
            logger.debug("Result queue string : %s", result_path)

            measures = self._glue_code.extract_measures(result_path)

            pos_last_slash = result_path.rfind("/")
            folder_to_save = result_path[:pos_last_slash]
            logger.debug("Folder where it's saved : %s", folder_to_save)

            pos_last_slash2 = folder_to_save.rfind("/")
            name_simulation = folder_to_save[pos_last_slash2 + 1:]
            logger.debug("Name Simulation : %s", name_simulation)

            measures_path = folder_to_save + "/measures.txt"
            self._fm.create_measures_file(measures, measures_path)
            self._fm.copy_file(
                measures_path,
                self.options.path_simulator + "/" + name_simulation + "/measures.txt",
            )
