import logging
import os
import shutil
from configparser import RawConfigParser
from datetime import datetime, timedelta
from io import IOBase
from typing import IO, List, Union

from experimenthandling.measure import Measure
from experimenthandling.options import Options

logger = logging.getLogger(__name__)


class FileManagement:
    """
    Utility class for all file I/O operations.

    Key Java → Python translation decisions:
    - java.util.Properties  → configparser.RawConfigParser (no interpolation)
    - java.util.Calendar    → datetime + timedelta for deadline computation
    - Files.copy / Files.move → shutil.copy2 / shutil.move
    - BufferedWriter/FileWriter → built-in open() context manager
    """

    def __init__(self):
        self.filename: str = ""
        self.options: Options = Options()
        self._path_result: str = ""
        self._path_simulator: str = ""

    # ------------------------------------------------------------------
    # Config file loading
    # ------------------------------------------------------------------

    def load_data_from_properties_file(self, source: Union[str, IO]) -> Options:
        """
        Load config.properties into an Options object.

        Accepts either a file path (str) or an open binary/text stream,
        mirroring the two Java overloads of loadDataFromPropertiesFile.
        """
        parser = RawConfigParser()
        parser.optionxform = str  # preserve case

        if isinstance(source, str):
            # Wrap in a fake section header that configparser requires
            with open(source, "r", encoding="utf-8") as fh:
                content = "[DEFAULT]\n" + fh.read()
        else:
            raw = source.read()
            if isinstance(raw, bytes):
                raw = raw.decode("utf-8")
            content = "[DEFAULT]\n" + raw

        parser.read_string(content)
        props = dict(parser["DEFAULT"])

        self.options.set_path_parameters(props.get("pathParameters") or props.get("pathparameters"))
        self.options.set_folder_path_out(props.get("pathOUT") or props.get("pathout"))
        self.options.set_path_simulator(props.get("pathSimulator") or props.get("pathsimulator"))
        self.options.set_path_to_simulator_result_file(
            props.get("pathToSimulatorResultFile") or props.get("pathtosimulatorresultfile")
        )

        cutt_of_value = props.get("cuttOfPlanning") or props.get("cuttofplanning") or ""
        type_cutt_of = props.get("typeCuttOfPlanning") or props.get("typecuttofplanning") or ""

        self.options.set_type_of_cutt_of_planning(type_cutt_of.strip())

        type_cutt_of = type_cutt_of.strip()
        cutt_of_value = cutt_of_value.strip()

        if type_cutt_of == "INT":
            self.options.set_cutt_of_planning(int(cutt_of_value))
        elif type_cutt_of == "DAY":
            self.options.set_cut_off_planning_h(datetime(1, 1, int(cutt_of_value)))
        elif type_cutt_of == "HOURS":
            self.options.set_cut_off_planning_h(datetime(1, 1, 1, int(cutt_of_value)))
        elif type_cutt_of == "MINUTES":
            self.options.set_cut_off_planning_h(datetime(1, 1, 1, 0, int(cutt_of_value)))
        elif type_cutt_of == "CRITERIA":
            self.options.set_stop_criteria(float(cutt_of_value))

        return self.options

    # ------------------------------------------------------------------
    # Folder management
    # ------------------------------------------------------------------

    def create_folder(self, folder_path: str) -> None:
        try:
            os.mkdir(folder_path)
        except (FileNotFoundError, FileExistsError):
            pass

    def save_simultation_result(self, result: str, env) -> str:
        return self.save_simulation_result(result, env)

    def write_data_in_properties_file(self, data_to_write: dict, file_path: str, keep_previous_results: bool) -> None:
        mode = "a" if keep_previous_results else "w"
        try:
            with open(file_path, mode, encoding="utf-8") as fh:
                for k, v in data_to_write.items():
                    fh.write(f"{k}={v}\n")
        except OSError:
            pass

    def create_new_folder(self, env) -> str:
        self._path_result = self.options.get_folder_path_out() + "/_sim" + str(env.id)
        self.create_folder(self._path_result)

        self._path_simulator = self.options.get_path_simulator() + "/_sim" + str(env.id) + "/"
        self.create_folder(self._path_simulator)
        return self._path_result

    def create_new_folder_simulation(self, env, glue_code) -> None:
        path_new_folder = self.create_new_folder(env)
        env.set_path_save_result(path_new_folder)
        glue_code.write_parameters_file(env.get_set_of_parameters(), path_new_folder)

        for f_name in os.listdir(self._path_result):
            src = os.path.join(self._path_result, f_name)
            dst = os.path.join(self._path_simulator, f_name)
            try:
                shutil.copy2(src, dst)
            except Exception as e:
                logger.error(
                    f"Error creating simulation folder. Check paths in config.properties. {e}"
                )

    # ------------------------------------------------------------------
    # File operations
    # ------------------------------------------------------------------

    def copy_file(self, file: str, destination: str) -> None:
        try:
            shutil.copy2(file, destination)
        except Exception as e:
            logger.error(f"Could not copy file: {e}")

    def move_file(self, origin_file: str, destination_file: str) -> None:
        if not os.path.exists(origin_file):
            return
        try:
            shutil.move(origin_file, destination_file)
        except Exception as e:
            logger.error(f"Could not move file: {e}")

    def content_of_a_file(self) -> str:
        if not os.path.isfile(self.filename):
            return "this is not a file"
        with open(self.filename, "r", encoding="utf-8") as fh:
            return fh.read().replace("\n", "")

    # ------------------------------------------------------------------
    # Simulation output files
    # ------------------------------------------------------------------

    def create_measures_file(self, measures: List[Measure], measures_file_path: str) -> None:
        try:
            with open(measures_file_path, "w", encoding="utf-8") as fh:
                for m in measures:
                    fh.write(f"{m.get_key()}={m.get_value()}\n")
        except Exception as e:
            logger.error(f"Error creating measures file: {e}")

    def create_modifier_file(self, path: str, modifier: str) -> None:
        try:
            with open(os.path.join(path, "SummaryFile.txt"), "w", encoding="utf-8") as fh:
                fh.write(modifier)
                fh.write("\n")
        except Exception as e:
            logger.error(f"Error saving SummaryFile: {e}")

    def save_simulation_result(self, result: str, env) -> str:
        file_path = (
            self.options.get_folder_path_out()
            + "/_sim"
            + str(env.get_id())
            + "/results.txt"
        )
        with open(file_path, "a", encoding="utf-8") as fh:
            fh.write(f"Result={result}\n")
        return file_path

    # ------------------------------------------------------------------
    # Getters / Setters
    # ------------------------------------------------------------------

    def get_filename(self) -> str:
        return self.filename

    def set_filename(self, filename: str) -> None:
        self.filename = filename

    def get_options(self) -> Options:
        return self.options

    def set_options(self, options: Options) -> None:
        self.options = options
