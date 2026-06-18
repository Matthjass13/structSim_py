import logging
import os
import time
from datetime import timedelta
from queue import Full, Queue
from typing import List

from experimenthandling.environment import Environment
from experimenthandling.options import Options
from interfaces.a_modifier import AModifier
from interfaces.a_simulation_system_handler import ASimulationSystemHandler
from util.file_management import FileManagement

logger = logging.getLogger(__name__)


class ExperimentPlanGenerator:
    """Generates the planning queue of environments for the simulation.

    Replaces Java's 'implements Runnable' pattern: this class exposes a run()
    method intended to be passed as target to threading.Thread.
    """

    def __init__(
        self,
        planning_queue: Queue,
        base_env: Environment,
        options: Options,
        glue_code: ASimulationSystemHandler,
        fm: FileManagement,
    ) -> None:
        self.base_environment: Environment = base_env
        self.planning_queue: Queue = planning_queue
        self.options: Options = options
        self.glue_code: ASimulationSystemHandler = glue_code
        self.fm: FileManagement = fm
        self.is_finish: bool = False

        self._end_time: float = 0.0
        self._cut_off_format: str = ""
        self._result: str = ""

        self.glue_code.initiate_modifier_list()

    def _create_next_environments(self, base_env: Environment) -> None:
        to_explore: List[Environment] = []
        self.fm.create_new_folder_simulation(base_env, self.glue_code)

        list_modifiers: List[AModifier] = self.glue_code.list_modifier_class
        to_explore.append(base_env)
        self._add_env_to_queue(base_env)

        id_cpt: int = base_env.get_id()
        cpt: int = 0

        while to_explore:

            if (self.options.type_of_cut_off_planning == "INT"
                    and cpt >= self.options.cut_off_planning):
                break

            parent_env: Environment = to_explore.pop(0)

            for modifier in list_modifiers:
                id_cpt += 1

                current_env = Environment(id_cpt, other=parent_env)
                current_env = modifier.apply_modifier(current_env)
                current_env.get_trace().append(modifier.get_name())

                logger.debug(
                    "--------------------------------------------%d %s",
                    current_env.id,
                    current_env.trace,
                )

                current_env.set_probability(
                    parent_env.get_probability() * modifier.get_probability()
                )

                if (self.options.type_of_cut_off_planning == "CRITERIA"
                        and current_env.get_probability() > self.options.stop_criteria):
                    to_explore.append(current_env)

                if self.options.type_of_cut_off_planning == "INT":
                    to_explore.append(current_env)

                self.fm.create_new_folder_simulation(current_env, self.glue_code)
                self._add_env_to_queue(current_env)
                self._create_modifier_file(current_env)

            cpt += 1
            logger.debug("CPT : %d", cpt)

            to_explore.sort(reverse=True)

    def _create_modifier_file(self, env: Environment) -> None:
        self._result += env.to_string_modifier() + os.linesep
        self.fm.create_modifier_file(self.options.folder_path_out, self._result)

    def _add_env_to_queue(self, env: Environment) -> None:
        try:
            self.planning_queue.put_nowait(env)
            logger.debug("Event : %d is added !", env.id)
        except Full:
            logger.error("Event : %d is not added !", env.id)

    def run(self) -> None:
        current_time = time.time()

        logger.debug("option = %s", self.options.type_of_cut_off_planning)

        match self.options.type_of_cut_off_planning:
            case "INT" | "CRITERIA":
                self._create_next_environments(self.base_environment)
            case "DAY" | "HOURS" | "MINUTES":
                duration: timedelta = self.options.cut_off_planning_h
                self._end_time = current_time + duration.total_seconds()
                self._cut_off_format = "TIME"

        if "TIME" in self._cut_off_format:
            while time.time() < self._end_time:
                self._create_next_environments(self.base_environment)

        self.is_finish = True

        self.fm.copy_file(
            self.options.folder_path_out + "/SummaryFile.txt",
            self.options.path_simulator + "/SummaryFile.txt",
        )
