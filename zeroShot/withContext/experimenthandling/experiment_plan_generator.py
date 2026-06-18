import logging
import time
from typing import List

from experimenthandling.environment import Environment
from experimenthandling.options import Options
from interfaces.i_manage_modifier import IManageModifier
from util.file_management import FileManagement

logger = logging.getLogger(__name__)


class ExperimentPlanGenerator:
    """
    First thread: creates the planning queue by generating environments.
    """

    def __init__(self, planning_queue, base_env: Environment, options: Options, glue_code, fm: FileManagement):
        self._base_environment = base_env
        self._planning_queue = planning_queue
        self.options = options
        self._glue_code = glue_code
        self._fm = fm
        self.is_finish = False
        self._cut_off_format = ""
        self._result = ""

        glue_code.initiate_modifier_list()

    def _create_next_environments(self, base_env: Environment) -> None:
        to_explore: List[Environment] = []
        self._fm.create_new_folder_simulation(base_env, self._glue_code)

        list_modifiers = self._glue_code.get_list_modifier_class()
        to_explore.append(base_env)
        self._add_env_to_queue(base_env)

        parent_env: Environment
        current_env: Environment
        id_cpt = base_env.get_id()
        cpt = 0

        while to_explore:
            if (
                self.options.get_type_of_cut_off_planning() == "INT"
                and cpt >= self.options.get_cut_off_planning()
            ):
                break

            parent_env = to_explore.pop(0)

            for modifier in list_modifiers:
                id_cpt += 1

                current_env = Environment.copy_from(id_cpt, parent_env)
                current_env = modifier.apply_modifier(current_env)
                current_env.get_trace().append(modifier.get_name())

                logger.debug(f"--------------------------------------------{current_env.id} {current_env.trace}")

                current_env.set_probability(parent_env.get_probability() * modifier.get_probability())

                if (
                    self.options.get_type_of_cut_off_planning() == "CRITERIA"
                    and current_env.get_probability() > self.options.get_stop_criteria()
                ):
                    to_explore.append(current_env)

                if self.options.get_type_of_cut_off_planning() == "INT":
                    to_explore.append(current_env)

                self._fm.create_new_folder_simulation(current_env, self._glue_code)
                self._add_env_to_queue(current_env)
                self._create_modifier_file(current_env)

            cpt += 1
            logger.debug(f"CPT : {cpt}")

            # Sort in reverse order so the most probable environment is first
            to_explore.sort(reverse=True)

    def _create_modifier_file(self, e: Environment) -> None:
        new_line = "\n"
        self._result += e.to_string_modifier() + new_line
        self._fm.create_modifier_file(self.options.folder_path_out, self._result)

    def _add_env_to_queue(self, e: Environment) -> None:
        try:
            self._planning_queue.put_nowait(e)
            was_added = True
        except Exception:
            was_added = False

        if was_added:
            logger.debug(f"Event : {e.id} is added !")
        else:
            logger.error(f"Event : {e.id} is not added !")

    def run(self) -> None:
        current_time = time.time()
        end_time = 0.0
        cut_off_format = ""

        type_of_cut = self.options.get_type_of_cut_off_planning()
        logger.debug(f"option = {type_of_cut}")

        if type_of_cut == "INT":
            self._create_next_environments(self._base_environment)
        elif type_of_cut == "CRITERIA":
            self._create_next_environments(self._base_environment)
        elif type_of_cut == "DAY":
            end_time = current_time + self.options.get_cut_off_planning_h() * 86400
            cut_off_format = "TIME"
        elif type_of_cut == "HOURS":
            end_time = current_time + self.options.get_cut_off_planning_h() * 3600
            cut_off_format = "TIME"
        elif type_of_cut == "MINUTES":
            end_time = current_time + self.options.get_cut_off_planning_h() * 60
            cut_off_format = "TIME"

        if "TIME" in cut_off_format:
            while time.time() < end_time:
                self._create_next_environments(self._base_environment)

        self.is_finish = True

        self._fm.copy_file(
            self.options.folder_path_out + "/SummaryFile.txt",
            self.options.path_simulator + "/SummaryFile.txt"
        )
