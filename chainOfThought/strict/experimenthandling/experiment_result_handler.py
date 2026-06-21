import threading


class ExperimentResultHandler(threading.Thread):
    def __init__(self, results_queue, glue_code, fm, options):
        super().__init__(name="Result Thread")
        self.results_queue = results_queue
        self.glue_code = glue_code      # ASimulationSystemHandler
        self.fm = fm                    # FileManagement
        self.options = options          # Options

    def run(self):
        while True:
            str_path = self.results_queue.get()
            if str_path is None:  # sentinel: no more results
                break
            measures = self.glue_code.extract_measures(str_path)
            position_of_last_slash = str_path.rfind("/")
            folder_to_save = str_path[:position_of_last_slash]
            position_last_slash = folder_to_save.rfind("/")
            name_simulation = folder_to_save[position_last_slash + 1:]
            self.fm.create_measures_file(measures, folder_to_save + "/measures.txt")
            self.fm.copy_file(
                folder_to_save + "/measures.txt",
                self.options.path_simulator + "/" + name_simulation + "/measures.txt"
            )
