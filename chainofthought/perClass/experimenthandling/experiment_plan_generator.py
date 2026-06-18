"""
Chain-of-thought for ExperimentPlanGenerator:
1. Java-specific constructs:
   - implements Runnable -> override run().
   - BlockingQueue<Environment> (PriorityBlockingQueue) -> queue.PriorityQueue.
   - BFS/DFS tree expansion with toExplore list.
   - Thread.sleep / Calendar-based time loop for DAY/HOURS/MINUTES cutoff.
   - isFinish boolean shared between threads (volatile in Java).
2. Python equivalents:
   - Runnable -> threading.Thread subclass or pass run() to Thread target; here we make it
     a Runnable-style class with a run() method designed to be the thread target.
   - BlockingQueue -> queue.PriorityQueue (blocks on put/get).
   - volatile boolean -> threading.Event or simple bool attribute (Python GIL makes single
     bool reads/writes atomic enough for this use-case; we also add a threading.Event).
   - Calendar time comparison -> datetime comparison.
3. Risks/deviations:
   - Java PriorityBlockingQueue orders by natural order (compareTo); our queue.PriorityQueue
     uses the __lt__ we defined on Environment, so the same semantics apply.
   - The Java code sorts toExplore in reverse (most probable first). We replicate with
     sorted(..., reverse=True).
   - isFinish is a plain bool; should be read only after join() in the consumer, which is safe.
"""

import queue
import threading
from datetime import datetime
from typing import List, TYPE_CHECKING

from experimenthandling.environment import Environment
from experimenthandling.options import Options

if TYPE_CHECKING:
    from interfaces.a_simulation_system_handler import ASimulationSystemHandler
    from util.file_management import FileManagement


class ExperimentPlanGenerator:
    """Generates the experiment plan (tree of environments) and pushes them onto a queue."""

    def __init__(
        self,
        planning_queue: queue.PriorityQueue,
        base_env: Environment,
        options: Options,
        glue_code: "ASimulationSystemHandler",
        fm: "FileManagement",
    ):
        self.planning_queue = planning_queue
        self.base_environment = base_env
        self.options = options
        self.glue_code = glue_code
        self.fm = fm
        self.is_finish: bool = False
        # Initialise modifier list via glue code
        self.glue_code.initiate_modifier_list()

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    def _add_env_to_queue(self, e: Environment) -> None:
        """Blocking put onto the planning queue."""
        self.planning_queue.put(e)

    def _create_modifier_file(self, e: Environment) -> None:
        result = e.to_string_modifier() + "\n"
        self.fm.create_modifier_file(self.options.folder_path_out, result)

    def _create_next_environments(self, base_env: Environment) -> None:
        """BFS/DFS tree expansion."""
        to_explore: List[Environment] = [base_env]
        self._add_env_to_queue(base_env)
        id_cpt = base_env.get_id()
        cpt = 0
        modifiers = self.glue_code.list_modifier_class
        type_cutoff = self.options.type_of_cutt_of_planning

        while to_explore:
            # Check INT cutoff
            if type_cutoff == "INT" and cpt >= self.options.cutt_of_planning:
                break

            parent_env = to_explore.pop(0)

            for modifier in modifiers:
                id_cpt += 1
                current_env = Environment.from_id_env(id_cpt, parent_env)
                current_env = modifier.apply_modifier(current_env)
                current_env.trace.append(modifier.name)
                current_env.probability = parent_env.probability * modifier.probability

                if type_cutoff == "CRITERIA" and current_env.probability > self.options.stop_criteria:
                    to_explore.append(current_env)
                elif type_cutoff == "INT":
                    to_explore.append(current_env)

                self.fm.create_new_folder_simulation(current_env, self.glue_code)
                self._add_env_to_queue(current_env)
                self._create_modifier_file(current_env)

            cpt += 1
            # Sort in reverse order (most probable first)
            to_explore.sort(reverse=True)

    # ------------------------------------------------------------------
    # Runnable entry point
    # ------------------------------------------------------------------

    def run(self) -> None:
        """Entry point executed by the planning thread."""
        type_cutoff = self.options.type_of_cutt_of_planning

        if type_cutoff in ("INT", "CRITERIA"):
            self._create_next_environments(self.base_environment)
        elif type_cutoff in ("DAY", "HOURS", "MINUTES"):
            deadline: datetime = self.options.cutt_of_planning_h
            while datetime.now() < deadline:
                self._create_next_environments(self.base_environment)

        self.is_finish = True

        # Copy summary file to simulator directory
        import os
        summary_src = os.path.join(self.options.folder_path_out, "SummaryFile.txt")
        summary_dst = os.path.join(self.options.path_simulator, "SummaryFile.txt")
        if os.path.isfile(summary_src):
            self.fm.copy_file(summary_src, summary_dst)
