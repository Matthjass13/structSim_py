import logging

logger = logging.getLogger(__name__)


class ExperimentResultHandler:

    def __init__(self, results_queue, glue_code, fm, options):
        self.results_queue = results_queue
        self.glue_code = glue_code
        self.fm = fm
        self.options = options

    def run(self):
        if not self.results_queue.empty():
            # Drain the queue into a list to iterate
            items = []
            while not self.results_queue.empty():
                try:
                    items.append(self.results_queue.get_nowait())
                except Exception:
                    break

            for result_path in items:
                logger.debug(f"Result queue string : {result_path}")
                measures = self.glue_code.extract_measures(result_path)
                pos_last_slash = result_path.rfind("/")
                folder_to_save = result_path[:pos_last_slash]
                logger.debug(f"Folder where it's saved : {folder_to_save}")
                pos_last_slash2 = folder_to_save.rfind("/")
                name_simulation = folder_to_save[pos_last_slash2 + 1:]
                logger.debug(f"Name Simulation : {name_simulation}")
                self.fm.create_measures_file(measures, folder_to_save + "/measures.txt")
                self.fm.copy_file(
                    folder_to_save + "/measures.txt",
                    self.options.path_simulator + "/" + name_simulation + "/measures.txt"
                )
