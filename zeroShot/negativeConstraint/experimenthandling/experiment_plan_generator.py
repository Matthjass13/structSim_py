import logging
import time
from experimenthandling.environment import Environment

logger = logging.getLogger(__name__)


class ExperimentPlanGenerator:

    def __init__(self, planning_queue, base_env, options, glue_code, fm):
        self.base_environment = base_env
        self.planning_queue = planning_queue
        self.options = options
        self.glue_code = glue_code
        self.fm = fm
        self.is_finish = False
        self._end_time = 0
        self._cuttof_format = ""
        self._result = ""
        glue_code.initiate_modifier_list()

    def _create_next_environments(self, base_env):
        to_explore = []
        self.fm.create_new_folder_simulation(base_env, self.glue_code)

        list_modifiers = self.glue_code.get_list_modifier_class()
        to_explore.append(base_env)
        self._add_env_to_queue(base_env)

        id_cpt = base_env.id
        cpt = 0

        while to_explore:
            if self.options.get_type_of_cuttof_planning() == "INT" and cpt >= self.options.get_cuttof_planning():
                break

            parent_env = to_explore.pop(0)

            for modifier in list_modifiers:
                id_cpt += 1
                current_env = Environment(id_cpt, copy_from=parent_env)
                current_env = modifier.apply_modifier(current_env)
                current_env.get_trace().append(modifier.get_name())

                logger.debug(f"--------------------------------------------{current_env.id} {current_env.trace}")

                current_env.set_probability(parent_env.get_probability() * modifier.get_probability())

                if self.options.get_type_of_cuttof_planning() == "CRITERIA" and \
                        current_env.get_probability() > self.options.get_stop_criteria():
                    to_explore.append(current_env)

                if self.options.get_type_of_cuttof_planning() == "INT":
                    to_explore.append(current_env)

                self.fm.create_new_folder_simulation(current_env, self.glue_code)
                self._add_env_to_queue(current_env)
                self._create_modifier_file(current_env)

            cpt += 1
            logger.debug(f"CPT : {cpt}")

            to_explore.sort(reverse=True)

    def _create_modifier_file(self, env):
        self._result += env.to_string_modifier() + "\n"
        self.fm.create_modifier_file(self.options.folder_path_out, self._result)

    def _add_env_to_queue(self, env):
        self.planning_queue.put(env)
        logger.debug(f"Event : {env.id} is added !")

    def run(self):
        current_time = time.time()

        logger.debug(f"option = {self.options.get_type_of_cuttof_planning()}")

        cuttype = self.options.get_type_of_cuttof_planning()

        if cuttype == "INT":
            self._create_next_environments(self.base_environment)
        elif cuttype == "CRITERIA":
            self._create_next_environments(self.base_environment)
        elif cuttype == "DAY":
            self._end_time = current_time + self.options.get_cuttof_planning_h()["DAY"] * 86400
            self._cuttof_format = "TIME"
        elif cuttype == "HOURS":
            self._end_time = current_time + self.options.get_cuttof_planning_h()["HOURS"] * 3600
            self._cuttof_format = "TIME"
        elif cuttype == "MINUTES":
            self._end_time = current_time + self.options.get_cuttof_planning_h()["MINUTES"] * 60
            self._cuttof_format = "TIME"

        if "TIME" in self._cuttof_format:
            while time.time() < self._end_time:
                self._create_next_environments(self.base_environment)

        self.is_finish = True

        self.fm.copy_file(
            self.options.folder_path_out + "/SummaryFile.txt",
            self.options.path_simulator + "/SummaryFile.txt"
        )
