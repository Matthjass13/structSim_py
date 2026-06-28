import logging

logger = logging.getLogger(__name__)


class ExperimentResultHandler:

    def __init__(self, results_queue, glue_code, fm, options):
        self.results_queue = results_queue
        self.glue_code = glue_code
        self.fm = fm
        self.options = options

    def run(self):
        while True:
            str_path = self.results_queue.get()
            if str_path is None:  # sentinel: no more results
                break
            logger.debug(f"Result queue string : {str_path}")
            measures = self.glue_code.extract_measures(str_path)
            position_of_last_slash = str_path.rfind("/")
            folder_to_save = str_path[:position_of_last_slash]
            logger.debug(f"Folder where it's saved : {folder_to_save}")
            position_last_slash = folder_to_save.rfind("/")
            name_simulation = folder_to_save[position_last_slash + 1:]
            logger.debug(f"Name Simulation : {name_simulation}")
            self.fm.create_measures_file(measures, folder_to_save + "/measures.txt")
            self.fm.copy_file(
                folder_to_save + "/measures.txt",
                self.options.path_simulator + "/" + name_simulation + "/measures.txt"
            )
