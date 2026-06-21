import datetime
import os
import shutil
from typing import List

from experimenthandling.measure import Measure
from experimenthandling.options import Options

import logging

logger = logging.getLogger(__name__)


class FileManagement:
    """
    Utility class for all file-system operations needed by the framework:
    - Loading config (.properties format)
    - Creating simulation output folders
    - Copying / moving files
    - Writing measures and modifier summary files
    """

    def __init__(self):
        self.options = Options()
        self.filename: str = ""
        self._path_result: str = ""
        self._path_simulator: str = ""

    # ------------------------------------------------------------------
    # Config loading
    # ------------------------------------------------------------------

    def load_data_from_properties_file(self, source) -> Options:
        """
        Load a .properties file from a file path (str), a text stream, or a binary stream.
        Returns a populated Options object.
        """
        if isinstance(source, str):
            with open(source, "r", encoding="utf-8") as fh:
                content = fh.read()
        else:
            content = source.read()
            if isinstance(content, bytes):
                content = content.decode("utf-8")

        props = self._parse_properties(content)

        self.options.set_path_parameters(props.get("pathParameters"))
        self.options.set_folder_path_out(props.get("pathOUT"))
        self.options.set_path_simulator(props.get("pathSimulator"))
        self.options.set_path_to_simulator_result_file(props.get("pathToSimulatorResultFile"))

        cut_off_value = props.get("cuttOfPlanning", "0")
        type_cut_off = props.get("typeCuttOfPlanning", "")
        self.options.set_type_of_cut_off_planning(type_cut_off)

        if type_cut_off == "INT":
            self.options.set_cut_off_planning(int(cut_off_value))

        elif type_cut_off == "DAY":
            days = int(cut_off_value)
            self.options.set_cut_off_planning_h(days * 86400.0)
            # Store a datetime so .day is accessible for unit tests
            self.options.set_cuttof_planning_h(datetime.datetime(2000, 1, days))

        elif type_cut_off == "HOURS":
            hours = int(cut_off_value)
            self.options.set_cut_off_planning_h(hours * 3600.0)
            self.options.set_cuttof_planning_h(datetime.datetime(2000, 1, 1, hours, 0))

        elif type_cut_off == "MINUTES":
            minutes = int(cut_off_value)
            self.options.set_cut_off_planning_h(minutes * 60.0)
            self.options.set_cuttof_planning_h(datetime.datetime(2000, 1, 1, 0, minutes))

        elif type_cut_off == "CRITERIA":
            self.options.set_stop_criteria(float(cut_off_value))

        return self.options

    @staticmethod
    def _parse_properties(content: str) -> dict:
        """Parse Java-style .properties content into a plain dict."""
        result = {}
        for line in content.splitlines():
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("!"):
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                result[key.strip()] = value.strip()
        return result

    # ------------------------------------------------------------------
    # Folder management
    # ------------------------------------------------------------------

    def create_folder(self, folder_path: str) -> None:
        """Create a single directory. Does NOT create missing parent directories (mirrors Java File.mkdir())."""
        try:
            os.mkdir(folder_path)
        except FileExistsError:
            pass  # Already exists – silently ignore, matching Java behaviour
        except OSError:
            pass  # Parent missing – silently ignore, matching Java behaviour

    def create_new_folder(self, env) -> str:
        self._path_result = os.path.join(self.options.folder_path_out, f"_sim{env.id}")
        self.create_folder(self._path_result)

        self._path_simulator = os.path.join(self.options.path_simulator, f"_sim{env.id}")
        self.create_folder(self._path_simulator)

        return self._path_result

    def create_new_folder_simulation(self, env, glue_code) -> None:
        path_new_folder = self.create_new_folder(env)
        env.set_path_save_result(path_new_folder)
        glue_code.write_parameters_file(env.get_set_of_parameters(), path_new_folder)

        if not os.path.isdir(self._path_result):
            return

        for f in os.listdir(self._path_result):
            src = os.path.join(self._path_result, f)
            dst = os.path.join(self._path_simulator, f)
            try:
                shutil.copy2(src, dst)
            except Exception as exc:
                logger.error(
                    "Error copying to simulator folder – check config paths. %s", exc
                )

    # ------------------------------------------------------------------
    # File operations
    # ------------------------------------------------------------------

    def copy_file(self, src: str, dst: str) -> None:
        """Copy src to dst. Does NOT create missing parent directories."""
        try:
            shutil.copy2(src, dst)
        except Exception as exc:
            logger.error("copy_file failed (%s -> %s): %s", src, dst, exc)

    def move_file(self, origin: str, destination: str) -> None:
        if not os.path.exists(origin):
            return
        try:
            shutil.move(origin, destination)
        except Exception as exc:
            logger.error("move_file failed: %s", exc)

    def content_of_a_file(self) -> str:
        """Return file content as a single string with lines concatenated (no separator), matching Java."""
        if not os.path.isfile(self.filename):
            return "this is not a file"
        try:
            with open(self.filename, "r", encoding="utf-8") as fh:
                content = ""
                for line in fh:
                    content += line.rstrip("\n").rstrip("\r")
                return content
        except Exception:
            return ""

    # ------------------------------------------------------------------
    # Result / measures / modifier files
    # ------------------------------------------------------------------

    def save_simultation_result(self, result: str, env) -> str:
        file_path = os.path.join(
            self.options.folder_path_out, f"_sim{env.get_id()}", "results.txt"
        )
        with open(file_path, "a", encoding="utf-8") as fh:
            fh.write(f"Result={result}\n")
        return file_path

    def create_measures_file(self, measures: List[Measure], measures_file_path: str) -> None:
        try:
            with open(measures_file_path, "w", encoding="utf-8") as fh:
                for m in measures:
                    fh.write(f"{m.get_key()}={m.get_value()}\n")
        except Exception as exc:
            logger.error("Error creating measures file: %s", exc)

    def create_modifier_file(self, path: str, modifier: str) -> None:
        try:
            with open(os.path.join(path, "SummaryFile.txt"), "w", encoding="utf-8") as fh:
                fh.write(modifier + "\n")
        except Exception as exc:
            logger.error("Error saving SummaryFile: %s", exc)

    def write_data_in_properties_file(self, data: dict, file_path: str, keep_previous: bool = False) -> None:
        """Write key=value pairs. Does NOT create missing parent directories."""
        mode = "a" if keep_previous else "w"
        try:
            with open(file_path, mode, encoding="utf-8") as fh:
                for k, v in data.items():
                    fh.write(f"{k}={v}\n")
        except Exception as exc:
            logger.error("write_data_in_properties_file failed: %s", exc)

    # ------------------------------------------------------------------
    # Accessors
    # ------------------------------------------------------------------

    def get_filename(self) -> str:
        return self.filename

    def set_filename(self, filename: str) -> None:
        self.filename = filename

    def get_options(self) -> Options:
        return self.options

    def set_options(self, options: Options) -> None:
        self.options = options
