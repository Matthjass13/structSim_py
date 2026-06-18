import logging
import queue
import threading

logger = logging.getLogger(__name__)


class ExperimentResultHandler:
    def __init__(self, results_queue: queue.Queue, glue_code, fm, options):
        self.results_queue = results_queue
        self.glue_code = glue_code
        self.fm = fm
        self.options = options

    def run(self):
        if not self.results_queue.empty():
            items = []
            while not self.results_queue.empty():
                try:
                    items.append(self.results_queue.get_nowait())
                except queue.Empty:
                    break

            for result_path in items:
                logger.debug(f"Result queue string : {result_path}")
                measures = self.glue_code.extract_measures(result_path)
                position_of_last_slash = result_path.rfind("/")
                folder_to_save = result_path[:position_of_last_slash]
                logger.debug(f"Folder where it's saved : {folder_to_save}")
                position_last_slash = folder_to_save.rfind("/")
                name_simulation = folder_to_save[position_last_slash + 1:]
                logger.debug(f"Name Simulation : {name_simulation}")
                self.fm.create_measures_file(measures, folder_to_save + "/measures.txt")
                self.fm.copy_file(
                    folder_to_save + "/measures.txt",
                    self.options.path_simulator + "/" + name_simulation + "/measures.txt"
                )
        else:
            threading.current_thread()  # no-op equivalent of interrupt
