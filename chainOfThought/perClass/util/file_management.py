"""
Chain-of-thought for FileManagement:
1. Java-specific constructs:
   - java.util.Properties (key=value file format).
   - java.nio.file.Files.move / Files.copy with StandardCopyOption.REPLACE_EXISTING.
   - InputStream overload for loadDataFromPropertiesFile.
   - Calendar for date/time cutoff parsing.
   - LinkedHashMap<String,String> for ordered key-value writing.
   - throws IOException.
2. Python equivalents:
   - Properties -> configparser (or manual key=value parsing; we use manual parsing to stay
     faithful because Java Properties files don't require section headers, which configparser
     requires by default).
   - Files.move / Files.copy -> shutil.move / shutil.copy2.
   - InputStream -> IO (file-like object); detect via duck-typing.
   - Calendar -> datetime.datetime.
   - LinkedHashMap -> dict (Python 3.7+ dicts are insertion-ordered).
   - IOException -> IOError / OSError (Python built-ins).
3. Risks/deviations:
   - configparser requires [section] headers; we parse key=value manually to avoid adding a
     dummy section, matching Java Properties behaviour.
   - Calendar arithmetic (DAY/HOURS/MINUTES) translated to datetime + timedelta.
   - 'throws IOException' not enforced in Python; exceptions propagate naturally.
"""

import os
import shutil
from datetime import datetime, timedelta
from typing import Dict, List, Optional, IO, TYPE_CHECKING

from experimenthandling.options import Options
from experimenthandling.measure import Measure

if TYPE_CHECKING:
    from experimenthandling.environment import Environment
    from interfaces.a_simulation_system_handler import ASimulationSystemHandler
    from experimenthandling.parameter import Parameter


def _parse_properties(text: str) -> Dict[str, str]:
    """Parse Java-style key=value properties text, ignoring blank lines and comments."""
    result: Dict[str, str] = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#") or line.startswith("!"):
            continue
        if "=" in line:
            k, _, v = line.partition("=")
            result[k.strip()] = v.strip()
    return result


class FileManagement:
    """Utility class mirroring Java FileManagement: file I/O, folder management, config loading."""

    def __init__(self):
        self.filename: Optional[str] = None
        self.options: Options = Options()
        self._path_result: Optional[str] = None
        self._path_simulator: Optional[str] = None

    # ------------------------------------------------------------------
    # Basic file operations
    # ------------------------------------------------------------------

    def content_of_a_file(self) -> str:
        """Read self.filename and return its full text content."""
        with open(self.filename, "r", encoding="utf-8") as fh:
            return fh.read()

    def move_file(self, origin_file: str, destination_file: str) -> None:
        """Move a file, replacing the destination if it exists."""
        shutil.move(origin_file, destination_file)

    def copy_file(self, file: str, destination: str) -> None:
        """Copy a file to destination path (replaces if exists)."""
        os.makedirs(os.path.dirname(destination), exist_ok=True)
        shutil.copy2(file, destination)

    def create_folder(self, folder_path: str) -> None:
        """Create a single directory (non-recursive)."""
        os.makedirs(folder_path, exist_ok=True)

    # ------------------------------------------------------------------
    # Result saving
    # ------------------------------------------------------------------

    def save_simulation_result(self, result: str, env: "Environment") -> str:
        """Write result string as key=value to the environment's result folder."""
        folder = os.path.join(self.options.folder_path_out, f"_sim{env.get_id()}")
        os.makedirs(folder, exist_ok=True)
        path = os.path.join(folder, "results.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(result)
        return path

    # ------------------------------------------------------------------
    # Properties file loading
    # ------------------------------------------------------------------

    def _apply_properties_to_options(self, props: Dict[str, str]) -> Options:
        """Populate an Options object from a parsed properties dict."""
        o = Options()
        o.set_path_parameters(props.get("pathParameters", ""))
        o.set_folder_path_out(props.get("pathOUT", props.get("folderPathOUT", "")))
        o.set_path_simulator(props.get("pathSimulator", ""))
        o.set_path_to_simulator_result_file(props.get("pathToSimulatorResultFile", ""))
        type_cutoff = props.get("typeCuttOfPlanning", props.get("typeOfCuttOfPlanning", "INT"))
        o.set_type_of_cutt_of_planning(type_cutoff)

        if type_cutoff == "INT":
            o.set_cutt_of_planning(int(props.get("cuttOfPlanning", "1")))
        elif type_cutoff == "CRITERIA":
            o.set_stop_criteria(float(props.get("cuttOfPlanning", props.get("stopCriteria", "0.0"))))
        elif type_cutoff in ("DAY", "HOURS", "MINUTES"):
            amount = int(props.get("cuttOfPlanning", "1"))
            now = datetime.now()
            if type_cutoff == "DAY":
                deadline = now + timedelta(days=amount)
            elif type_cutoff == "HOURS":
                deadline = now + timedelta(hours=amount)
            else:
                deadline = now + timedelta(minutes=amount)
            o.set_cutt_of_planning_h(deadline)
        return o

    def load_data_from_properties_file(self, file_path) -> Options:
        """Load options from a properties file path or file-like object."""
        if isinstance(file_path, str):
            with open(file_path, "r", encoding="utf-8") as fh:
                text = fh.read()
        else:
            # file-like object (InputStream equivalent)
            text = file_path.read()
            if isinstance(text, bytes):
                text = text.decode("utf-8")
        props = _parse_properties(text)
        self.options = self._apply_properties_to_options(props)
        return self.options

    # ------------------------------------------------------------------
    # Properties file writing
    # ------------------------------------------------------------------

    def write_data_in_properties_file(
        self,
        data_to_write: Dict[str, str],
        file_path: str,
        keep_previous_results: bool,
    ) -> None:
        """Write key=value pairs to file. If keep_previous_results, append; otherwise overwrite."""
        mode = "a" if keep_previous_results else "w"
        os.makedirs(os.path.dirname(file_path) or ".", exist_ok=True)
        with open(file_path, mode, encoding="utf-8") as fh:
            for k, v in data_to_write.items():
                fh.write(f"{k}={v}\n")

    # ------------------------------------------------------------------
    # Folder creation helpers
    # ------------------------------------------------------------------

    def create_new_folder(self, e: "Environment") -> str:
        """Create per-environment output and simulator folders; return the result path."""
        self._path_result = os.path.join(self.options.folder_path_out, f"_sim{e.get_id()}")
        self.create_folder(self._path_result)
        self._path_simulator = os.path.join(self.options.path_simulator, f"_sim{e.get_id()}")
        self.create_folder(self._path_simulator)
        return self._path_result

    def create_new_folder_simulation(
        self,
        env: "Environment",
        glue_code: "ASimulationSystemHandler",
    ) -> None:
        """Create folders, write parameter file, and copy files to simulator folder."""
        path_result = self.create_new_folder(env)
        env.set_path_save_result(path_result)
        glue_code.write_parameters_file(env.get_set_of_parameters(), path_result)
        # Copy each file from path_result to path_simulator
        if os.path.isdir(path_result):
            for fname in os.listdir(path_result):
                src = os.path.join(path_result, fname)
                dst = os.path.join(self._path_simulator, fname)
                if os.path.isfile(src):
                    shutil.copy2(src, dst)

    # ------------------------------------------------------------------
    # Measures / modifier file helpers
    # ------------------------------------------------------------------

    def create_measures_file(self, measures: List[Measure], measures_file_path: str) -> None:
        """Write key=value lines for each measure to measures_file_path."""
        os.makedirs(os.path.dirname(measures_file_path) or ".", exist_ok=True)
        with open(measures_file_path, "w", encoding="utf-8") as fh:
            for m in measures:
                fh.write(f"{m.get_key()}={m.get_value()}\n")

    def create_modifier_file(self, path: str, modifier: str) -> None:
        """Append modifier summary text to <path>/SummaryFile.txt."""
        os.makedirs(path, exist_ok=True)
        summary_path = os.path.join(path, "SummaryFile.txt")
        with open(summary_path, "a", encoding="utf-8") as fh:
            fh.write(modifier + "\n")

    # ------------------------------------------------------------------
    # Getters / setters
    # ------------------------------------------------------------------

    def get_filename(self) -> Optional[str]:
        return self.filename

    def set_filename(self, filename: str) -> None:
        self.filename = filename

    def get_options(self) -> Options:
        return self.options

    def set_options(self, options: Options) -> None:
        self.options = options
