import logging
import os
import shutil
from io import StringIO
from typing import IO, List

from experimenthandling.measure import Measure
from experimenthandling.options import Options

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

    # ------------------------------------------------------------------
    # Config loading
    # ------------------------------------------------------------------

    def load_data_from_properties_file(self, source) -> Options:
        """
        Load a .properties file from either a file path (str) or an open stream (IO).
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
        try:
            self.options.set_cuttof_raw_value(int(float(cut_off_value)))
        except (ValueError, TypeError):
            pass

        if type_cut_off == "INT":
            self.options.set_cut_off_planning(int(cut_off_value))
        elif type_cut_off == "DAY":
            self.options.set_cut_off_planning_h(int(cut_off_value) * 86400.0)
        elif type_cut_off == "HOURS":
            self.options.set_cut_off_planning_h(int(cut_off_value) * 3600.0)
        elif type_cut_off == "MINUTES":
            self.options.set_cut_off_planning_h(int(cut_off_value) * 60.0)
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
        try:
            os.mkdir(folder_path)
        except (FileNotFoundError, FileExistsError):
            pass

    def create_new_folder(self, env) -> str:
        path_result = os.path.join(self.options.folder_path_out, f"_sim{env.id}")
        self.create_folder(path_result)

        path_simulator = os.path.join(self.options.path_simulator, f"_sim{env.id}")
        self.create_folder(path_simulator)

        self._path_result = path_result
        self._path_simulator = path_simulator
        return path_result

    def create_new_folder_simulation(self, env, glue_code) -> None:
        path_new_folder = self.create_new_folder(env)
        env.set_path_save_result(path_new_folder)
        glue_code.write_parameters_file(env.get_set_of_parameters(), path_new_folder)

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
        try:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
        except Exception as exc:
            logger.error("copy_file failed: %s", exc)

    def move_file(self, origin: str, destination: str) -> None:
        if not os.path.exists(origin):
            return
        try:
            shutil.move(origin, destination)
        except Exception as exc:
            logger.error("move_file failed: %s", exc)

    def content_of_a_file(self) -> str:
        if not os.path.isfile(self.filename):
            return "this is not a file"
        with open(self.filename, "r", encoding="utf-8") as fh:
            return "".join(line.rstrip("\n") for line in fh)

    # ------------------------------------------------------------------
    # Result / measures / modifier files
    # ------------------------------------------------------------------

    def save_simulation_result(self, result: str, env) -> str:
        file_path = os.path.join(
            self.options.folder_path_out, f"_sim{env.get_id()}", "results.txt"
        )
        with open(file_path, "a", encoding="utf-8") as fh:
            fh.write(f"Result={result}\n")
        return file_path

    def save_simultation_result(self, result: str, env) -> str:
        return self.save_simulation_result(result, env)

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

    def write_data_in_properties_file(
        self, data: dict, file_path: str, keep_previous: bool = False
    ) -> None:
        parent = os.path.dirname(file_path)
        if parent and not os.path.isdir(parent):
            return
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
