import os
import threading
import time

from experimenthandling.environment import Environment


class ExperimentPlanGenerator(threading.Thread):
    def __init__(self, planning_queue, base_env, options, glue_code, fm):
        super().__init__(name="Planning Thread")
        self.base_environment = base_env       # Environment
        self.planning_queue = planning_queue   # queue.Queue
        self.options = options                 # Options
        self.glue_code = glue_code             # ASimulationSystemHandler
        self.fm = fm                           # FileManagement
        self._end_time = 0                     # int (ms)
        self._cutt_of_format = ""              # str
        self._result = ""                      # str (accumulated modifier summary)
        self.is_finish = False                 # public boolean flag

        # Initiate modifier list
        self.glue_code.initiate_modifier_list()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _create_next_environments(self, base_env: Environment) -> None:
        to_explore = []
        self.fm.create_new_folder_simulation(base_env, self.glue_code)
        list_modifiers = self.glue_code.get_list_modifier_class()
        to_explore.append(base_env)
        self._add_env_to_queue(base_env)

        id_cpt = base_env.get_id()
        cpt = 0

        while to_explore:
            if (self.options.get_type_of_cutt_of_planning() == "INT"
                    and cpt >= self.options.get_cutt_of_planning()):
                break

            parent_env = to_explore.pop(0)

            for modifier in list_modifiers:
                id_cpt += 1
                current_env = Environment.copy(id_cpt, parent_env)
                current_env = modifier.apply_modifier(current_env)
                current_env.get_trace().append(modifier.get_name())
                current_env.set_probability(
                    parent_env.get_probability() * modifier.get_probability()
                )

                if (self.options.get_type_of_cutt_of_planning() == "CRITERIA"
                        and current_env.get_probability() > self.options.get_stop_criteria()):
                    to_explore.append(current_env)

                if self.options.get_type_of_cutt_of_planning() == "INT":
                    to_explore.append(current_env)

                self.fm.create_new_folder_simulation(current_env, self.glue_code)
                self._add_env_to_queue(current_env)
                self._create_modifier_file(current_env)

            cpt += 1
            to_explore.sort(reverse=True)

    def _create_modifier_file(self, env: Environment) -> None:
        new_line = os.linesep
        self._result += env.to_string_modifier() + new_line
        self.fm.create_modifier_file(self.options.folder_path_out, self._result)

    def _add_env_to_queue(self, env: Environment) -> None:
        self.planning_queue.put(env)

    # ------------------------------------------------------------------
    # Thread entry point
    # ------------------------------------------------------------------

    def run(self):
        current_time = int(time.time() * 1000)
        cutt_of_type = self.options.get_type_of_cutt_of_planning()

        if cutt_of_type == "INT":
            self._create_next_environments(self.base_environment)

        elif cutt_of_type == "CRITERIA":
            self._create_next_environments(self.base_environment)

        elif cutt_of_type == "DAY":
            days = self.options.get_cutt_of_planning_h().day
            self._end_time = current_time + days * 86400000
            self._cutt_of_format = "TIME"

        elif cutt_of_type == "HOURS":
            hours = self.options.get_cutt_of_planning_h().hour
            self._end_time = current_time + hours * 3600000
            self._cutt_of_format = "TIME"

        elif cutt_of_type == "MINUTES":
            minutes = self.options.get_cutt_of_planning_h().minute
            self._end_time = current_time + minutes * 60000
            self._cutt_of_format = "TIME"

        if "TIME" in self._cutt_of_format:
            while int(time.time() * 1000) < self._end_time:
                self._create_next_environments(self.base_environment)

        self.is_finish = True
        self.fm.copy_file(
            self.options.folder_path_out + "/SummaryFile.txt",
            self.options.path_simulator + "/SummaryFile.txt"
        )
