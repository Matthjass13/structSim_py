import io
import os
import shutil
import datetime

from experimenthandling.options import Options


class FileManagement:
    def __init__(self):
        self.filename = None          # str
        self.options = Options()
        self._path_result = None      # str (private, replaces pathResult)
        self._path_simulator = None   # str (private, replaces pathSimulator)

    # ------------------------------------------------------------------
    # File reading
    # ------------------------------------------------------------------

    def content_of_a_file(self) -> str:
        """Return the full content of self.filename as a single string."""
        if not os.path.isfile(self.filename):
            return "this is not a file"
        content_file = ""
        try:
            with open(self.filename, 'r') as f:
                for line in f:
                    content_file += line.rstrip('\n')
        except Exception as e:
            print(e)
        return content_file

    # ------------------------------------------------------------------
    # File / folder operations
    # ------------------------------------------------------------------

    def move_file(self, origin_file: str, destination_file: str) -> None:
        if not os.path.exists(origin_file):
            return
        try:
            shutil.move(origin_file, destination_file)
        except Exception:
            pass

    def copy_file(self, file: str, destination: str) -> None:
        try:
            shutil.copy2(file, destination)
        except Exception:
            pass

    def create_folder(self, folder_path: str) -> None:
        os.makedirs(folder_path, exist_ok=True)

    # ------------------------------------------------------------------
    # Saving simulation results
    # ------------------------------------------------------------------

    def save_simulation_result(self, result: str, env) -> str:
        """
        Append a Result=<result> property to a results.txt file inside
        the environment's output folder.
        """
        file_path = self.options.get_folder_path_out() + "/" + "_sim" + str(env.get_id()) + "/results.txt"
        try:
            with open(file_path, 'a') as fops:
                fops.write(f"Result={result}\n")
        except Exception as e:
            print(e)
        return file_path

    # ------------------------------------------------------------------
    # Loading config from a properties file
    # ------------------------------------------------------------------

    def _parse_properties_dict(self, props: dict) -> Options:
        """
        Populate self.options from a dict of key→value strings (properties format).
        Mirrors the Java switch block in loadDataFromPropertiesFile.
        """
        cutt_of_value = props.get("cuttOfPlanning", "")

        for key, val in props.items():
            if key == "pathParameters":
                self.options.set_path_parameters(val)
            elif key == "pathOUT":
                self.options.set_folder_path_out(val)
            elif key == "pathSimulator":
                self.options.set_path_simulator(val)
            elif key == "pathToSimulatorResultFile":
                self.options.set_path_to_simulator_result_file(val)
            elif key == "cuttOfPlanning":
                cutt_of_value = val
            elif key == "typeCuttOfPlanning":
                self.options.set_type_of_cutt_of_planning(val)
                if val == "INT":
                    self.options.set_cutt_of_planning(int(cutt_of_value))
                elif val == "DAY":
                    cal = datetime.datetime.now().replace(day=int(cutt_of_value))
                    self.options.set_cutt_of_planning_h(cal)
                elif val == "HOURS":
                    cal = datetime.datetime.now().replace(hour=int(cutt_of_value))
                    self.options.set_cutt_of_planning_h(cal)
                elif val == "MINUTES":
                    cal = datetime.datetime.now().replace(minute=int(cutt_of_value))
                    self.options.set_cutt_of_planning_h(cal)
                elif val == "CRITERIA":
                    self.options.set_stop_criteria(float(cutt_of_value))
        return self.options

    def load_data_from_properties_file(self, source) -> Options:
        """
        Load options from a properties file.
        source can be:
          - a str (file path)
          - a file-like object (io.IOBase / InputStream equivalent)
        """
        props = {}
        try:
            if isinstance(source, str):
                with open(source, 'r') as f:
                    lines = f.readlines()
            else:
                # file-like object
                lines = source.read().splitlines()
                if lines and isinstance(lines[0], bytes):
                    lines = [line.decode('utf-8') for line in lines]
                source.close()

            for line in lines:
                line = line.strip()
                if not line or line.startswith('#') or line.startswith('!'):
                    continue
                pos = line.find('=')
                if pos == -1:
                    continue
                k = line[:pos].strip()
                v = line[pos + 1:].strip()
                props[k] = v
        except Exception as e:
            print(e)

        return self._parse_properties_dict(props)

    # ------------------------------------------------------------------
    # Writing properties data
    # ------------------------------------------------------------------

    def write_data_in_properties_file(self, data_to_write: dict, file_path: str, keep_previous_results: bool) -> None:
        """
        Write a dict of str→str to a properties file.
        keep_previous_results=True → append mode; False → overwrite.
        """
        mode = 'a' if keep_previous_results else 'w'
        try:
            with open(file_path, mode) as fops:
                for k, v in data_to_write.items():
                    fops.write(f"{k}={v}\n")
        except Exception as e:
            print(e)

    # ------------------------------------------------------------------
    # Folder creation for environments
    # ------------------------------------------------------------------

    def create_new_folder(self, env) -> str:
        self._path_result = self.options.get_folder_path_out() + "/" + "_sim" + str(env.get_id())
        self.create_folder(self._path_result)
        self._path_simulator = self.options.get_path_simulator() + "/" + "_sim" + str(env.get_id()) + "/"
        self.create_folder(self._path_simulator)
        return self._path_result

    def create_new_folder_simulation(self, env, glue_code) -> None:
        """
        Create output folder, write parameter file, then copy all files into
        the simulator subfolder.
        """
        path_new_folder = self.create_new_folder(env)
        env.set_path_save_result(path_new_folder)
        glue_code.write_parameters_file(env.get_set_of_parameters(), path_new_folder)

        content = [
            f for f in os.listdir(self._path_result)
            if os.path.isfile(os.path.join(self._path_result, f))
        ]
        for f_name in content:
            dest = self._path_simulator + f_name
            src = os.path.join(self._path_result, f_name)
            new_file = dest
            try:
                shutil.copy2(src, new_file)
            except Exception as e:
                print(e)

    # ------------------------------------------------------------------
    # Measures / modifier summary files
    # ------------------------------------------------------------------

    def create_measures_file(self, measures: list, measures_file_path: str) -> None:
        try:
            with open(measures_file_path, 'w', encoding='utf-8') as bw:
                for m in measures:
                    bw.write(m.get_key() + "=" + m.get_value() + "\n")
        except Exception as e:
            print(e)

    def create_modifier_file(self, path: str, modifier: str) -> None:
        try:
            with open(os.path.join(path, "SummaryFile.txt"), 'w', encoding='utf-8') as bw:
                bw.write(modifier + "\n")
        except Exception as e:
            print(e)

    # ------------------------------------------------------------------
    # Getters / setters
    # ------------------------------------------------------------------

    def get_filename(self):
        return self.filename

    def set_filename(self, filename):
        self.filename = filename

    def get_options(self):
        return self.options

    def set_options(self, options):
        self.options = options
