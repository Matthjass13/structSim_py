import logging
import os
import shutil
from pathlib import Path
from typing import IO, Union

from experimenthandling.measure import Measure
from experimenthandling.options import Options

logger = logging.getLogger(__name__)


class FileManagement:

    def __init__(self):
        self.filename: str = ""
        self.options: Options = Options()
        self._path_result: str = ""
        self._path_simulator: str = ""

    def content_of_a_file(self) -> str:
        if not Path(self.filename).is_file():
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
        origin = Path(origin_file)
        if not origin.exists():
            return
        try:
            shutil.move(str(origin), destination_file)
        except Exception:
            logger.error("Impossible to move this file")

    def copy_file(self, file: str, destination: str) -> None:
        try:
            shutil.copy2(file, destination)
        except Exception:
            logger.error("This file in this folder already exist")

    def create_folder(self, folder_path: str) -> None:
        try:
            Path(folder_path).mkdir(parents=False, exist_ok=True)
        except FileNotFoundError:
            pass

    def save_simulation_result(self, result: str, env) -> str:
        file_path = (
            self.options.get_folder_path_out()
            + "/_sim" + str(env.get_id())
            + "/results.txt"
        )
        try:
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(f"Result={result}\n")
        except FileNotFoundError:
            logger.error("File not Found")
        return file_path

    def save_simultation_result(self, result: str, env) -> str:
        return self.save_simulation_result(result, env)

    def create_new_folder(self, env) -> str:
        return self._create_new_folder(env)

    def load_data_from_properties_file(self, file_path) -> Options:
        if hasattr(file_path, "read"):
            return self.load_data_from_properties_file_stream(file_path)
        props: dict = {}
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#") or line.startswith("!"):
                        continue
                    if "=" in line:
                        key, _, value = line.partition("=")
                        props[key.strip()] = value.strip()
        except IOError as e:
            logger.error("Error to load Data from Properties file")

        return self._apply_properties(props)

    def load_data_from_properties_file_stream(self, ips: IO) -> Options:
        props: dict = {}
        try:
            for line in ips:
                if isinstance(line, bytes):
                    line = line.decode("utf-8")
                line = line.strip()
                if not line or line.startswith("#") or line.startswith("!"):
                    continue
                if "=" in line:
                    key, _, value = line.partition("=")
                    props[key.strip()] = value.strip()
        except IOError as e:
            logger.error("Error to load Data from Properties file")

        return self._apply_properties(props)

    def _apply_properties(self, props: dict) -> Options:
        self.options.set_path_parameters(props.get("pathParameters", ""))
        self.options.set_folder_path_out(props.get("pathOUT", ""))
        self.options.set_path_simulator(props.get("pathSimulator", ""))
        self.options.set_path_to_simulator_result_file(props.get("pathToSimulatorResultFile", ""))

        cutt_of_value = props.get("cuttOfPlanning", "")
        type_cutt_of = props.get("typeCuttOfPlanning", "")

        self.options.set_type_of_cutt_of_planning(type_cutt_of)

        if type_cutt_of == "INT":
            self.options.set_cutt_of_planning(int(cutt_of_value))
        elif type_cutt_of == "DAY":
            self.options.set_cutt_of_planning_h({"DATE": int(cutt_of_value)})
        elif type_cutt_of == "HOURS":
            self.options.set_cutt_of_planning_h({"HOUR_OF_DAY": int(cutt_of_value)})
        elif type_cutt_of == "MINUTES":
            self.options.set_cutt_of_planning_h({"MINUTE": int(cutt_of_value)})
        elif type_cutt_of == "CRITERIA":
            self.options.set_stop_criteria(float(cutt_of_value))

        return self.options

    def write_data_in_properties_file(self, data_to_write: dict, file_path: str,
                                      keep_previous_results: bool) -> None:
        parent = os.path.dirname(file_path)
        if parent and not os.path.isdir(parent):
            return
        mode = "a" if keep_previous_results else "w"
        try:
            with open(file_path, mode, encoding="utf-8") as f:
                for key, value in data_to_write.items():
                    f.write(f"{key}={value}\n")
        except IOError as e:
            logger.error(str(e))

    def _create_new_folder(self, env) -> str:
        self._path_result = self.options.get_folder_path_out() + "/_sim" + str(env.get_id())
        self.create_folder(self._path_result)
        self._path_simulator = self.options.get_path_simulator() + "/_sim" + str(env.get_id()) + "/"
        self.create_folder(self._path_simulator)
        return self._path_result

    def create_new_folder_simulation(self, env, glue_code) -> None:
        path_new_folder = self._create_new_folder(env)
        env.set_path_save_result(path_new_folder)
        glue_code.write_parameters_file(env.get_set_of_parameters(), path_new_folder)

        result_dir = Path(self._path_result)
        for f in result_dir.iterdir():
            dest = Path(self._path_simulator) / f.name
            try:
                shutil.copy2(str(f), str(dest))
            except Exception:
                logger.error(
                    "Error when we create the new Folder of the simulation. "
                    "Is the path in the config properties right ?"
                )

    def create_measures_file(self, measures: list, measures_file_path: str) -> None:
        try:
            with open(measures_file_path, "w", encoding="utf-8") as f:
                for m in measures:
                    f.write(f"{m.get_key()}={m.get_value()}\n")
        except Exception:
            logger.error("Error when we create the measures file")

    def create_modifier_file(self, path: str, modifier: str) -> None:
        try:
            with open(path + "/SummaryFile.txt", "w", encoding="utf-8") as f:
                f.write(modifier)
                f.write("\n")
        except IOError as e:
            logger.error("Error to save the summary File")

    def get_filename(self) -> str:
        return self.filename

    def set_filename(self, filename: str) -> None:
        self.filename = filename

    def get_options(self) -> Options:
        return self.options

    def set_options(self, options: Options) -> None:
        self.options = options
