import logging
import queue
import time
from datetime import datetime
from typing import List

from experimenthandling.environment import Environment
from experimenthandling.options import Options

logger = logging.getLogger(__name__)


class ExperimentPlanGenerator:
    """
    First thread: builds the planning queue by generating all environment variants.

    Java BlockingQueue.add() → queue.Queue.put_nowait()
    Java thread coordination (isFinish flag) is preserved as is_finish attribute.
    Java Collections.sort(list, reverseOrder()) → list.sort(reverse=True)
    """

    def __init__(self, planning_queue: queue.Queue, base_env: Environment,
                 options: Options, glue_code, fm):
        self.base_environment = base_env
        self.planning_queue = planning_queue
        self.options = options
        self.glue_code = glue_code
        self.fm = fm
        self.is_finish = False
        self._result = ""

        glue_code.initiate_modifier_list()

    def _create_next_environments(self, base_env: Environment) -> None:
        to_explore: List[Environment] = []
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

                current_env = Environment(id_cpt, copy_from=parent_env)
                current_env = modifier.apply_modifier(current_env)
                current_env.get_trace().append(modifier.get_name())

                logger.debug(f"--------------------------------------------{current_env.id} {current_env.trace}")

                current_env.set_probability(parent_env.get_probability() * modifier.get_probability())

                if (self.options.get_type_of_cutt_of_planning() == "CRITERIA"
                        and current_env.get_probability() > self.options.get_stop_criteria()):
                    to_explore.append(current_env)

                if self.options.get_type_of_cutt_of_planning() == "INT":
                    to_explore.append(current_env)

                self.fm.create_new_folder_simulation(current_env, self.glue_code)
                self._add_env_to_queue(current_env)
                self._create_modifier_file(current_env)

            cpt += 1
            logger.debug(f"CPT : {cpt}")

            # Sort descending so the most probable environment comes first
            to_explore.sort(reverse=True)

    def _create_modifier_file(self, env: Environment) -> None:
        self._result += env.to_string_modifier() + "\n"
        self.fm.create_modifier_file(self.options.folder_path_out, self._result)

    def _add_env_to_queue(self, env: Environment) -> None:
        try:
            self.planning_queue.put_nowait(env)
            logger.debug(f"Event : {env.id} is added !")
        except queue.Full:
            logger.error(f"Event : {env.id} is not added !")

    def run(self) -> None:
        cutt_of_format = ""
        deadline: datetime = None

        type_plan = self.options.get_type_of_cutt_of_planning()
        logger.debug(f"option = {type_plan}")

        if type_plan in ("INT", "CRITERIA"):
            self._create_next_environments(self.base_environment)
        elif type_plan in ("DAY", "HOURS", "MINUTES"):
            cutt_of_format = "TIME"
            deadline = self.options.get_cut_off_planning_h()

        if cutt_of_format == "TIME":
            while datetime.now() < deadline:
                self._create_next_environments(self.base_environment)

        self.is_finish = True

        self.fm.copy_file(
            self.options.folder_path_out + "/SummaryFile.txt",
            self.options.path_simulator + "/SummaryFile.txt",
        )
