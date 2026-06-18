import logging
import os
import shutil
from datetime import timedelta
from typing import IO, List, Optional

from experimenthandling.environment import Environment
from experimenthandling.measure import Measure
from experimenthandling.options import Options

logger = logging.getLogger(__name__)


class FileManagement:

    def __init__(self) -> None:
        self.filename: str = ""
        self.options: Options = Options()
        self._path_result: str = ""
        self._path_simulator: str = ""

    def content_of_a_file(self) -> str:
        if not os.path.isfile(self.filename):
            return "this is not a file"

        content_file = ""
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    content_file += line.rstrip("\n")
        except FileNotFoundError as e:
            logger.info("Just a stack trace", exc_info=e)

        return content_file

    def move_file(self, origin_file: str, destination_file: str) -> None:
        if not os.path.exists(origin_file):
            return
        try:
            shutil.move(origin_file, destination_file)
        except OSError:
            logger.error("Impossible to move this file")

    def copy_file(self, file: str, destination: str) -> None:
        try:
            shutil.copy2(file, destination)
        except Exception:
            logger.error("This file in this folder already exist")

    def create_folder(self, folder_path: str) -> None:
        os.makedirs(folder_path, exist_ok=True)

    def save_simulation_result(self, result: str, env: Environment) -> str:
        file_path = self.options.folder_path_out + "/" + "_sim" + str(env.get_id()) + "/results.txt"
        try:
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(f"Result={result}\n")
        except FileNotFoundError:
            logger.error("File not Found")
        return file_path

    def load_data_from_properties_file(self, file_path) -> Options:
        """Load config from a file path (str) or an InputStream (file-like object)."""
        import configparser

        properties: dict = {}

        if isinstance(file_path, str):
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if line and "=" in line and not line.startswith("#"):
                        key, _, value = line.partition("=")
                        properties[key.strip()] = value.strip()
        else:
            # file-like object (InputStream equivalent)
            content = file_path.read()
            if isinstance(content, bytes):
                content = content.decode("utf-8")
            for line in content.splitlines():
                line = line.strip()
                if line and "=" in line and not line.startswith("#"):
                    key, _, value = line.partition("=")
                    properties[key.strip()] = value.strip()

        self.options.path_parameters = properties.get("pathParameters", "")
        self.options.folder_path_out = properties.get("pathOUT", "")
        self.options.path_simulator = properties.get("pathSimulator", "")
        self.options.path_to_simulator_result_file = properties.get("pathToSimulatorResultFile", "")

        cut_off_value = properties.get("cuttOfPlanning", "")
        type_cut_off = properties.get("typeCuttOfPlanning", "")

        self.options.type_of_cut_off_planning = type_cut_off

        match type_cut_off:
            case "INT":
                self.options.cut_off_planning = int(cut_off_value)
            case "DAY":
                self.options.cut_off_planning_h = timedelta(days=int(cut_off_value))
            case "HOURS":
                self.options.cut_off_planning_h = timedelta(hours=int(cut_off_value))
            case "MINUTES":
                self.options.cut_off_planning_h = timedelta(minutes=int(cut_off_value))
            case "CRITERIA":
                self.options.stop_criteria = float(cut_off_value)

        return self.options

    def write_data_in_properties_file(
        self, data_to_write: dict, file_path: str, keep_previous_results: bool
    ) -> None:
        mode = "a" if keep_previous_results else "w"
        try:
            with open(file_path, mode, encoding="utf-8") as f:
                for key, value in data_to_write.items():
                    f.write(f"{key}={value}\n")
        except OSError as e:
            logger.error(str(e))

    def create_new_folder(self, env: Environment) -> str:
        self._path_result = self.options.folder_path_out + "/" + "_sim" + str(env.get_id())
        self.create_folder(self._path_result)

        self._path_simulator = self.options.path_simulator + "/" + "_sim" + str(env.get_id()) + "/"
        self.create_folder(self._path_simulator)
        return self._path_result

    def create_new_folder_simulation(self, env: Environment, glue_code) -> None:
        path_new_folder = self.create_new_folder(env)
        env.set_path_save_result(path_new_folder)
        glue_code.write_parameters_file(env.get_set_of_parameters(), path_new_folder)

        content = os.listdir(self._path_result)
        for fname in content:
            src = os.path.join(self._path_result, fname)
            dst = self._path_simulator + fname
            try:
                shutil.copy2(src, dst)
            except OSError as e:
                logger.error(
                    "Error when we create the new Folder of the simulation. "
                    "Is the path in the config properties right ? "
                )

    def create_measures_file(self, measures: List[Measure], measures_file_path: str) -> None:
        try:
            with open(measures_file_path, "w", encoding="utf-8") as f:
                for m in measures:
                    f.write(f"{m.key}={m.value}\n")
        except Exception:
            logger.error("Error when we create the measures file")

    def create_modifier_file(self, path: str, modifier: str) -> None:
        try:
            with open(path + "/SummaryFile.txt", "w", encoding="utf-8") as f:
                f.write(modifier)
                f.write("\n")
        except OSError as e:
            logger.error("Error to save the summary File")

    def get_filename(self) -> str:
        return self.filename

    def set_filename(self, filename: str) -> None:
        self.filename = filename

    def get_options(self) -> Options:
        return self.options

    def set_options(self, options: Options) -> None:
        self.options = options
