import logging
import os
import shutil

from experimenthandling.options import Options

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
            with open(self.filename, "r", encoding="utf-8") as f:
                for line in f:
                    content += line.rstrip("\n")
        except FileNotFoundError:
            logger.info(f"File not found: {self.filename}")
        return content

    def move_file(self, origin_file, destination_file):
        if not os.path.exists(origin_file):
            return
        try:
            shutil.move(origin_file, destination_file)
        except Exception as e:
            logger.error(f"Impossible to move this file: {e}")

    def copy_file(self, file_path, destination):
        try:
            shutil.copy2(file_path, destination)
        except Exception as e:
            logger.error(f"Error copying file: {e}")

    def create_folder(self, folder_path):
        os.makedirs(folder_path, exist_ok=True)

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

        path_sim = self._path_simulator
        if os.path.isdir(self._path_result):
            for f_name in os.listdir(self._path_result):
                src = os.path.join(self._path_result, f_name)
                dst = os.path.join(path_sim, f_name)
                try:
                    shutil.copy2(src, dst)
                except Exception as e:
                    logger.error(f"Error creating new folder simulation: {e}")

    def create_measures_file(self, measures, measures_file_path):
        try:
            with open(measures_file_path, "w", encoding="utf-8") as f:
                for m in measures:
                    f.write(m.get_key() + "=" + m.get_value() + "\n")
        except Exception as e:
            logger.error(f"Error creating measures file: {e}")

    def create_modifier_file(self, path, modifier):
        try:
            with open(path + "/SummaryFile.txt", "w", encoding="utf-8") as f:
                f.write(modifier)
                f.write("\n")
        except Exception as e:
            logger.error(f"Error saving summary file: {e}")

    def load_data_from_properties_file(self, file_path):
        """Load options from a .properties file (key=value format). file_path can be a str or file-like object."""
        props = {}
        try:
            if hasattr(file_path, "read"):
                content = file_path.read()
                if isinstance(content, bytes):
                    content = content.decode("utf-8")
                lines = content.splitlines()
            else:
                with open(file_path, "r", encoding="utf-8") as f:
                    lines = f.readlines()

            for line in lines:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" in line:
                    k, v = line.split("=", 1)
                    props[k.strip()] = v.strip()
        except Exception as e:
            logger.error(f"Error loading properties file: {e}")

        self.options.set_path_parameters(props.get("pathParameters"))
        self.options.set_folder_path_out(props.get("pathOUT"))
        self.options.set_path_simulator(props.get("pathSimulator"))
        self.options.set_path_to_simulator_result_file(props.get("pathToSimulatorResultFile"))

        cutoff_value = props.get("cuttOfPlanning", "")
        type_cutoff = props.get("typeCuttOfPlanning", "")
        self.options.set_type_of_cutoff_planning(type_cutoff)

        if type_cutoff == "INT":
            self.options.set_cutoff_planning(int(cutoff_value))
        elif type_cutoff in ("DAY", "HOURS", "MINUTES"):
            self.options.set_cutoff_planning_time_value(int(cutoff_value))
        elif type_cutoff == "CRITERIA":
            self.options.set_stop_criteria(float(cutoff_value))

        return self.options

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename

    def get_options(self):
        return self.options

    def set_options(self, options):
        self.options = options
