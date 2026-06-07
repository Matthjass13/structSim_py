"""
Java source : unitTests/fileManagement/FileManagementSimulationTests.java
Extends     : FileManagementTests  →  setup fixture in conftest.py

Translation notes:
  - Mockito mock(X.class)                  →  MagicMock(spec=X)
  - Mockito verify(m, times(1)).method(a)  →  m.method.assert_called_once_with(a)
  - Mockito anyString()                    →  ANY  (from unittest.mock)
  - Mockito eq(value)                      →  value  (MagicMock uses == by default)
  - assertEquals(Path.of(a).normalize(),
                 Path.of(b).normalize())   →  assert Path(a) == Path(b)
  - Properties.load() in assertion         →  _load_properties() helper
  - saveSimultationResult (Java typo)      →  save_simulation_result  (corrected)
"""

import configparser
import pytest
from pathlib import Path
from unittest.mock import MagicMock, ANY

from structuredsim.experimenthandling import Environment, Options
from structuredsim.interfaces import ASimulationSystemHandler


def _load_properties(filepath: str) -> dict:
    """Parse a Java-style .properties file (no section header) into a plain dict."""
    config = configparser.RawConfigParser()
    config.optionxform = str
    with open(filepath, "r") as f:
        config.read_string("[DEFAULT]\n" + f.read())
    return dict(config["DEFAULT"])


class TestFileManagementSimulation:
    """Tests FileManagement methods related to Environment and Options."""

    @pytest.fixture(autouse=True)
    def setup(self, tmp_path, file_management):
        self.file_management = file_management
        self.temp_dir        = tmp_path

    # GPT generated
    def test_save_simulation_result_should_save_result_and_return_path_when_directory_exists(self):

        # Arrange
        options = Options()
        options.set_folder_path_out(str(self.temp_dir))
        self.file_management.set_options(options)

        env               = Environment()
        simulation_folder = self.temp_dir / "_sim1"
        simulation_folder.mkdir(parents=True)

        expected_result = "SUCCESS"

        # Act
        # Note: Java source has a typo "saveSimultationResult"; corrected here
        returned_path = self.file_management.save_simulation_result(expected_result, env)

        # Assert
        expected_path = str(simulation_folder / "results.txt")
        assert Path(expected_path) == Path(returned_path)
        assert Path(returned_path).exists()

        props = _load_properties(returned_path)
        assert props["Result"] == expected_result

    # ChatGPT generated
    def test_create_new_folder_should_create_result_and_simulator_folders(self):

        # Arrange
        options = Options()
        options.set_folder_path_out(str(self.temp_dir / "results"))
        options.set_path_simulator(str(self.temp_dir / "simulator"))
        self.file_management.set_options(options)

        (self.temp_dir / "results").mkdir(parents=True)
        (self.temp_dir / "simulator").mkdir(parents=True)

        env = Environment()

        # Act
        returned_path = self.file_management.create_new_folder(env)

        # Assert
        expected_result_folder    = self.temp_dir / "results"  / "_sim1"
        expected_simulator_folder = self.temp_dir / "simulator" / "_sim1"

        assert Path(returned_path) == expected_result_folder

        assert expected_result_folder.exists()
        assert expected_result_folder.is_dir()

        assert expected_simulator_folder.exists()
        assert expected_simulator_folder.is_dir()

    # ChatGPT generated
    def test_create_new_folder_simulation_should_create_simulation_folder_and_write_parameters_file(self):

        # Arrange
        options = Options()
        options.set_folder_path_out(str(self.temp_dir / "results"))
        options.set_path_simulator(str(self.temp_dir / "simulator"))
        self.file_management.set_options(options)

        (self.temp_dir / "results").mkdir(parents=True)
        (self.temp_dir / "simulator").mkdir(parents=True)

        env       = Environment()
        glue_code = MagicMock(spec=ASimulationSystemHandler)

        # Act
        self.file_management.create_new_folder_simulation(env, glue_code)

        # Assert
        # Mockito: verify(glueCode, times(1)).writeParametersFile(eq(env.getSetOfParameters()), anyString())
        glue_code.write_parameters_file.assert_called_once_with(
            env.get_set_of_parameters(),
            ANY,   # anyString() → any path string
        )
        assert env.get_path_save_result() is not None
        assert "_sim" in env.get_path_save_result()
