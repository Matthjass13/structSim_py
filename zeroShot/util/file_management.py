import logging
import os
import shutil
from typing import IO, List, Union

from experimenthandling.measure import Measure
from experimenthandling.options import Options

logger = logging.getLogger(__name__)


class FileManagement:
    """
    Manages parameters and/or results files:
    - Read data from a file
    - Put key/value data into a dict
    - Save a file
    - Get a value by key
    """

    def __init__(self):
        self.filename: str = None
        self.options: Options = Options()
        self._path_result: str = None
        self._path_simulator: str = None

    def content_of_a_file(self) -> str:
        """Return a string with the content of the configured filename."""
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
        """Move a file from one location to another."""
        if not os.path.exists(origin_file):
            return
        try:
            shutil.move(origin_file, destination_file)
        except Exception:
            logger.error("Impossible to move this file")

    def copy_file(self, file: str, destination: str) -> None:
        """Copy a file to another location."""
        try:
            shutil.copy2(file, destination)
        except Exception:
            logger.error("This file in this folder already exist")

    def create_folder(self, folder_path: str) -> None:
        """Create an empty folder."""
        os.makedirs(folder_path, exist_ok=True)

    def save_simulation_result(self, result: str, env) -> str:
        """
        Save the simulation result in a file.
        Returns the path of the file where the result was saved.
        """
        file_path = os.path.join(
            self.options.get_folder_path_out(),
            f"_sim{env.get_id()}",
            "results.txt"
        )
        try:
            with open(file_path, "a", encoding="utf-8") as f:
                f.write(f"Result={result}\n")
        except FileNotFoundError:
            logger.error("File not Found")

        return file_path

    def _parse_properties(self, stream: IO) -> dict:
        """Parse a Java .properties format stream into a dict."""
        props = {}
        for raw_line in stream:
            line = raw_line.strip() if isinstance(raw_line, str) else raw_line.decode("utf-8").strip()
            if not line or line.startswith("#") or line.startswith("!"):
                continue
            if "=" in line:
                key, _, value = line.partition("=")
                props[key.strip()] = value.strip()
            elif ":" in line:
                key, _, value = line.partition(":")
                props[key.strip()] = value.strip()
        return props

    def _apply_properties_to_options(self, props: dict) -> Options:
        """Populate the Options object from a parsed properties dict."""
        self.options.set_path_parameters(props.get("pathParameters"))
        self.options.set_folder_path_out(props.get("pathOUT"))
        self.options.set_path_simulator(props.get("pathSimulator"))
        self.options.set_path_to_simulator_result_file(props.get("pathToSimulatorResultFile"))

        cut_off_value = props.get("cuttOfPlanning", "")
        type_cut_off = props.get("typeCuttOfPlanning", "")

        self.options.set_type_of_cut_off_planning(type_cut_off)

        if type_cut_off == "INT":
            self.options.set_cut_off_planning(int(cut_off_value))
        elif type_cut_off == "DAY":
            self.options.set_cut_off_planning_h(int(cut_off_value))
        elif type_cut_off == "HOURS":
            self.options.set_cut_off_planning_h(int(cut_off_value))
        elif type_cut_off == "MINUTES":
            self.options.set_cut_off_planning_h(int(cut_off_value))
        elif type_cut_off == "CRITERIA":
            self.options.set_stop_criteria(float(cut_off_value))

        return self.options

    def load_data_from_properties_file(self, source: Union[str, IO]) -> Options:
        """
        Load data from a properties file and populate an Options object.
        Accepts either a file path string or a file-like object (InputStream equivalent).
        """
        try:
            if isinstance(source, str):
                with open(source, "r", encoding="utf-8") as f:
                    props = self._parse_properties(f)
            else:
                props = self._parse_properties(source)
        except Exception as e:
            logger.error("Error loading data from properties file")
            raise

        return self._apply_properties_to_options(props)

    def write_data_in_properties_file(self, data_to_write: dict, file_path: str, keep_previous_results: bool) -> None:
        """
        Write key/value data to a properties file.
        If keep_previous_results is True, append; otherwise overwrite.
        """
        mode = "a" if keep_previous_results else "w"
        try:
            with open(file_path, mode, encoding="utf-8") as f:
                for key, value in data_to_write.items():
                    f.write(f"{key}={value}\n")
        except IOError as e:
            logger.error(str(e))

    def create_new_folder(self, e) -> str:
        """Create a new folder for a simulation environment."""
        self._path_result = os.path.join(self.options.get_folder_path_out(), f"_sim{e.get_id()}")
        self.create_folder(self._path_result)

        self._path_simulator = os.path.join(self.options.get_path_simulator(), f"_sim{e.get_id()}", "")
        self.create_folder(self._path_simulator)
        return self._path_result

    def create_new_folder_simulation(self, env, glue_code) -> None:
        """
        Create a new folder for the simulation environment,
        write the parameters file, then copy all files to the simulator folder.
        """
        path_new_folder = self.create_new_folder(env)
        env.set_path_save_result(path_new_folder)
        glue_code.write_parameters_file(env.get_set_of_parameters(), path_new_folder)

        content = os.listdir(self._path_result)
        for f_name in content:
            self._path_simulator += f_name
            src = os.path.join(self._path_result, f_name)
            try:
                shutil.copy2(src, self._path_simulator)
            except Exception as e:
                logger.error(
                    "Error when creating the new folder of the simulation. "
                    "Is the path in the config properties correct?"
                )

    def create_measures_file(self, measures: List[Measure], measures_file_path: str) -> None:
        """Write measures to a file."""
        try:
            with open(measures_file_path, "w", encoding="utf-8") as f:
                for m in measures:
                    f.write(f"{m.get_key()}={m.get_value()}\n")
        except Exception:
            logger.error("Error when creating the measures file")

    def create_modifier_file(self, path: str, modifier: str) -> None:
        """Write the modifier summary to a SummaryFile.txt."""
        summary_path = os.path.join(path, "SummaryFile.txt")
        try:
            with open(summary_path, "w", encoding="utf-8") as f:
                f.write(modifier)
                f.write("\n")
        except IOError as e:
            logger.error("Error saving the summary file")

    def get_filename(self) -> str:
        return self.filename

    def set_filename(self, filename: str) -> None:
        self.filename = filename

    def get_options(self) -> Options:
        return self.options

    def set_options(self, options: Options) -> None:
        self.options = options
