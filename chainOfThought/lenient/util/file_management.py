import configparser
import logging
import os
import shutil
from datetime import datetime, timedelta
from typing import List

from experimenthandling.options import Options

logger = logging.getLogger(__name__)


class FileManagement:
    def __init__(self):
        self.filename: str = None
        self.options: Options = Options()
        self._path_result: str = None
        self._path_simulator: str = None

    def content_of_a_file(self) -> str:
        if not os.path.isfile(self.filename):
            return "this is not a file"
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                return f.read().replace("\n", "")
        except IOError as e:
            logger.info("Just a stack trace", exc_info=e)
            return ""

    def move_file(self, origin_file: str, destination_file: str):
        if not os.path.exists(origin_file):
            return
        try:
            shutil.move(origin_file, destination_file)
        except IOError:
            logger.error("Impossible to move this file")

    def copy_file(self, file: str, destination: str):
        try:
            shutil.copy2(file, destination)
        except Exception:
            logger.error("This file in this folder already exist")

    def create_folder(self, folder_path: str):
        try:
            os.mkdir(folder_path)
        except (FileNotFoundError, FileExistsError):
            pass

    def save_simultation_result(self, result: str, env) -> str:
        return self.save_simulation_result(result, env)

    def save_simulation_result(self, result: str, env) -> str:
        file_path = f"{self.options.get_folder_path_out()}/_sim{env.get_id()}/results.txt"
        try:
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(f"Result={result}\n")
        except FileNotFoundError:
            logger.error("File not Found")
        return file_path

    def load_data_from_properties_file(self, file_path) -> Options:
        config = configparser.RawConfigParser()

        if isinstance(file_path, str):
            config.read(file_path)
        else:
            # file-like object (equivalent to InputStream)
            content = file_path.read()
            if isinstance(content, bytes):
                content = content.decode("utf-8")
            # configparser needs a section header; properties files don't have one
            config.read_string("[DEFAULT]\n" + content)

        props = dict(config["DEFAULT"])

        self.options.set_path_parameters(props.get("pathparameters"))
        self.options.set_folder_path_out(props.get("pathout"))
        self.options.set_path_simulator(props.get("pathsimulator"))
        self.options.set_path_to_simulator_result_file(props.get("pathtosimulatorresultfile"))

        cutt_of_value = props.get("cuttofplanning", "")
        type_cutt_of = props.get("typecuttofplanning", "")

        self.options.set_type_of_cutt_of_planning(type_cutt_of.upper() if type_cutt_of else "")

        type_upper = type_cutt_of.upper() if type_cutt_of else ""
        if type_upper == "INT":
            self.options.set_cutt_of_planning(int(cutt_of_value))
        elif type_upper == "DAY":
            self.options.set_cutt_of_planning_h(datetime(1, 1, int(cutt_of_value)))
        elif type_upper == "HOURS":
            self.options.set_cutt_of_planning_h(datetime(1, 1, 1, int(cutt_of_value)))
        elif type_upper == "MINUTES":
            self.options.set_cutt_of_planning_h(datetime(1, 1, 1, 0, int(cutt_of_value)))
        elif type_upper == "CRITERIA":
            self.options.set_stop_criteria(float(cutt_of_value))

        return self.options

    def write_data_in_properties_file(self, data_to_write: dict, file_path: str, keep_previous_results: bool):
        mode = "a" if keep_previous_results else "w"
        try:
            with open(file_path, mode, encoding="utf-8") as f:
                for key, value in data_to_write.items():
                    f.write(f"{key}={value}\n")
        except IOError as e:
            logger.error(str(e))

    def create_new_folder(self, env) -> str:
        self._path_result = f"{self.options.get_folder_path_out()}/_sim{env.get_id()}"
        self.create_folder(self._path_result)

        self._path_simulator = f"{self.options.get_path_simulator()}/_sim{env.get_id()}/"
        self.create_folder(self._path_simulator)
        return self._path_result

    def create_new_folder_simulation(self, env, glue_code):
        path_new_folder = self.create_new_folder(env)
        env.set_path_save_result(path_new_folder)
        glue_code.write_parameters_file(env.get_set_of_parameters(), path_new_folder)

        sim_folder = self._path_simulator
        for f_name in os.listdir(self._path_result):
            src = os.path.join(self._path_result, f_name)
            dst = os.path.join(sim_folder, f_name)
            try:
                shutil.copy2(src, dst)
            except IOError:
                logger.error(
                    "Error when we create the new Folder of the simulation. "
                    "Is the path in the config properties right ?"
                )

    def create_measures_file(self, measures: List, measures_file_path: str):
        try:
            with open(measures_file_path, "w", encoding="utf-8") as f:
                for m in measures:
                    f.write(f"{m.get_key()}={m.get_value()}\n")
        except Exception:
            logger.error("Error when we create the measures file")

    def create_modifier_file(self, path: str, modifier: str):
        try:
            with open(os.path.join(path, "SummaryFile.txt"), "w", encoding="utf-8") as f:
                f.write(modifier + "\n")
        except IOError as e:
            logger.error("Error to save the summary File")

    def get_filename(self) -> str:
        return self.filename

    def set_filename(self, filename: str):
        self.filename = filename

    def get_options(self) -> Options:
        return self.options

    def set_options(self, options: Options):
        self.options = options
