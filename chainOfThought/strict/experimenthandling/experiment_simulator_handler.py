import threading

from experimenthandling.experiment_result_handler import ExperimentResultHandler


class ExperimentSimulatorHandler(threading.Thread):
    def __init__(self, environment_queue, results_queue, options, glue_code, fm, plan):
        super().__init__(name="Simulation Thread")
        self.environment_queue = environment_queue   # queue.Queue of Environment
        self.results_queue = results_queue           # queue.Queue of str
        self.options = options                       # Options
        self.glue_code = glue_code                  # ASimulationSystemHandler
        self.fm = fm                                 # FileManagement
        self.plan = plan                             # ExperimentPlanGenerator

    def run(self):
        result_handler = ExperimentResultHandler(
            self.results_queue, self.glue_code, self.fm, self.options
        )
        result_handler.name = "Result Thread"

        while True:
            try:
                env = self.environment_queue.get()   # blocking take()
                self.glue_code.start_simulation(self.options.get_path_parameters())

                result_path_for_this_simulation = (
                    env.path_save_result
                    + "/results_sim"
                    + str(env.id)
                    + ".txt"
                )

                self.fm.copy_file(
                    self.options.path_to_simulator_result_file,
                    result_path_for_this_simulation
                )

                sim_folder_name = env.path_save_result[
                    env.path_save_result.rfind("/") + 1:
                ]
                self.fm.copy_file(
                    self.options.path_to_simulator_result_file,
                    self.options.path_simulator
                    + "/"
                    + sim_folder_name
                    + "/results_sim"
                    + str(env.id)
                    + ".txt"
                )

                self.results_queue.put(result_path_for_this_simulation)

                if self.plan.is_finish:
                    if self.environment_queue.empty():
                        break

            except Exception as e:
                print(e)

        self.results_queue.put(None)  # sentinel: signal result handler to stop
        result_handler.start()
        result_handler.join()
