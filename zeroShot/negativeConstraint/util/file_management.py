import configparser
import logging
import os
import shutil

from experimenthandling.options import Options
from experimenthandling.measure import Measure

logger = logging.getLogger(__name__)


class FileManagement:

    def __init__(self):
        self.filename = None
        self.options = Options()
        self._path_result = None
        self._path_simulator = None

    def content_of_a_file(self):
        if not os.path.isfile(self.filename):
            return "this is not a file"
        content = ""
        try:
            with open(self.filename, encoding="utf-8") as f:
                for line in f:
                    content += line.rstrip("\n")
        except FileNotFoundError as e:
            logger.info("Just a stack trace", exc_info=e)
        return content

    def move_file(self, origin_file, destination_file):
        if not os.path.exists(origin_file):
            return
        try:
            shutil.move(origin_file, destination_file)
        except OSError:
            logger.error("Impossible to move this file")

    def copy_file(self, file, destination):
        try:
            shutil.copy2(file, destination)
        except Exception:
            logger.error("This file in this folder already exist")

    def create_folder(self, folder_path):
        os.makedirs(folder_path, exist_ok=True)

    def save_simulation_result(self, result, env):
        file_path = (
            self.options.get_folder_path_out() + "/_sim" + str(env.get_id()) + "/results.txt"
        )
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"Result={result}\n")
        return file_path

    def load_data_from_properties_file(self, source):
        config = configparser.ConfigParser()
        if hasattr(source, "read"):
            text = source.read()
            if isinstance(text, bytes):
                text = text.decode("utf-8")
            config.read_string("[root]\n" + text)
        else:
            with open(source, encoding="utf-8") as f:
                config.read_string("[root]\n" + f.read())

        props = dict(config["root"])

        self.options.set_path_parameters(props.get("pathparameters"))
        self.options.set_folder_path_out(props.get("pathout"))
        self.options.set_path_simulator(props.get("pathsimulator"))
        self.options.set_path_to_simulator_result_file(props.get("pathtosimulatorresultfile"))

        cuttof_value = props.get("cuttofplanning", "")
        type_cuttof = props.get("typecuttofplanning", "")

        self.options.set_type_of_cuttof_planning(type_cuttof.upper())

        match type_cuttof.upper():
            case "INT":
                self.options.set_cuttof_planning(int(cuttof_value))
            case "DAY":
                self.options.set_cuttof_planning_h({"DAY": int(cuttof_value)})
            case "HOURS":
                self.options.set_cuttof_planning_h({"HOURS": int(cuttof_value)})
            case "MINUTES":
                self.options.set_cuttof_planning_h({"MINUTES": int(cuttof_value)})
            case "CRITERIA":
                self.options.set_stop_criteria(float(cuttof_value))

        return self.options

    def write_data_in_properties_file(self, data_to_write, file_path, keep_previous_results):
        mode = "a" if keep_previous_results else "w"
        try:
            with open(file_path, mode, encoding="utf-8") as f:
                for key, value in data_to_write.items():
                    f.write(f"{key}={value}\n")
        except OSError as e:
            logger.error(str(e))

    def create_new_folder(self, env):
        self._path_result = self.options.get_folder_path_out() + "/_sim" + str(env.get_id())
        self.create_folder(self._path_result)

        self._path_simulator = self.options.get_path_simulator() + "/_sim" + str(env.get_id()) + "/"
        self.create_folder(self._path_simulator)
        return self._path_result

    def create_new_folder_simulation(self, env, glue_code):
        path_new_folder = self.create_new_folder(env)
        env.set_path_save_result(path_new_folder)
        glue_code.write_parameters_file(env.get_set_of_parameters(), path_new_folder)

        for f in os.listdir(self._path_result):
            src = os.path.join(self._path_result, f)
            dst = os.path.join(self._path_simulator, f)
            try:
                shutil.copy2(src, dst)
            except OSError as e:
                logger.error(
                    f"Error when we create the new Folder of the simulation. "
                    f"Is the path in the config properties right ? {e}"
                )

    def create_measures_file(self, measures, measures_file_path):
        try:
            with open(measures_file_path, "w", encoding="utf-8") as f:
                for m in measures:
                    f.write(m.get_key() + "=" + m.get_value() + "\n")
        except Exception:
            logger.error("Error when we create the measures file")

    def create_modifier_file(self, path, modifier):
        try:
            with open(path + "/SummaryFile.txt", "w", encoding="utf-8") as f:
                f.write(modifier + "\n")
        except OSError as e:
            logger.error(f"Error to save the summary File: {e}")

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename

    def get_options(self):
        return self.options

    def set_options(self, options):
        self.options = options
