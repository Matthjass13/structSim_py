"""
Java source : unitTests/fileManagement/FileManagementPropertiesTests.java
Extends     : FileManagementTests  →  setup fixture in conftest.py

Translation notes:
  - InputStream                 →  io.BytesIO
  - LinkedHashMap<String,String>→  dict (ordered by insertion since Python 3.7)
  - Properties.load()           →  _load_properties() helper (see below)
  - Properties.getProperty(key) →  props[key] / props.get(key)
  - assertNull(x)               →  assert x is None
  - @ParameterizedTest @CsvSource → @pytest.mark.parametrize
  - Calendar assumption: options.get_cut_off_planning_h() returns a datetime.datetime.
    Calendar.DATE        → datetime.day
    Calendar.HOUR_OF_DAY → datetime.hour
    Calendar.MINUTE      → datetime.minute
    ⚠️ Adjust if the Python implementation uses a different type.
"""

import io
import configparser
import pytest


def _load_properties(filepath: str) -> dict:
    """
    Parse a Java-style .properties file (no section header) into a plain dict.
    Uses configparser with a synthetic [DEFAULT] section.
    Key case is preserved (optionxform = str).
    """
    config = configparser.RawConfigParser()
    config.optionxform = str  # preserve original key casing
    with open(filepath, "r") as f:
        config.read_string("[DEFAULT]\n" + f.read())
    return dict(config["DEFAULT"])


class TestFileManagementProperties:
    """Tests FileManagement methods related to data serialization."""

    DELTA = 1e-9

    @pytest.fixture(autouse=True)
    def setup(self, tmp_path, file_management):
        self.file_management = file_management
        self.temp_dir        = tmp_path

    # GPT generated
    def test_load_data_from_properties_file_should_load_properties_file(self):

        # Arrange
        properties_content = (
            "pathParameters=params.txt\n"
            "pathOUT=C:/output\n"
            "pathSimulator=simulator.exe\n"
            "pathToSimulatorResultFile=result.txt\n"
            "cuttOfPlanning=10\n"
            "typeCuttOfPlanning=INT\n"
        )
        input_stream = io.BytesIO(properties_content.encode("utf-8"))

        # Act
        options = self.file_management.load_data_from_properties_file(input_stream)

        # Assert
        assert options.get_path_parameters()               == "params.txt"
        assert options.get_folder_path_out()               == "C:/output"
        assert options.get_path_simulator()                == "simulator.exe"
        assert options.get_path_to_simulator_result_file() == "result.txt"
        assert options.get_type_of_cut_off_planning()      == "INT"
        assert options.get_cut_off_planning()              == 10

    def test_load_data_from_properties_file_should_load_criteria_planning_type(self):

        # Arrange
        properties_content = (
            "cuttOfPlanning=0.95\n"
            "typeCuttOfPlanning=CRITERIA\n"
        )
        input_stream = io.BytesIO(properties_content.encode("utf-8"))

        # Act
        options = self.file_management.load_data_from_properties_file(input_stream)

        # Assert
        assert options.get_type_of_cut_off_planning() == "CRITERIA"
        assert options.get_stop_criteria() == pytest.approx(0.95, abs=self.DELTA)

    # ChatGPT generated
    @pytest.mark.parametrize("type_,value", [
        ("DAY",     15),
        ("HOURS",   10),
        ("MINUTES", 45),
    ])
    def test_load_data_from_properties_file_should_load_calendar_based_planning_types(
        self, type_: str, value: int
    ):
        # Arrange
        properties_content = (
            f"cuttOfPlanning={value}\n"
            f"typeCuttOfPlanning={type_}\n"
        )
        input_stream = io.BytesIO(properties_content.encode("utf-8"))

        # Act
        options = self.file_management.load_data_from_properties_file(input_stream)

        # Assert
        assert options.get_type_of_cut_off_planning() == type_

        # ⚠️ Assumes get_cut_off_planning_h() returns a datetime.datetime.
        #    Calendar.DATE        → .day
        #    Calendar.HOUR_OF_DAY → .hour
        #    Calendar.MINUTE      → .minute
        calendar = options.get_cut_off_planning_h()
        if type_ == "DAY":
            assert calendar.day   == value
        elif type_ == "HOURS":
            assert calendar.hour  == value
        elif type_ == "MINUTES":
            assert calendar.minute == value

    # ChatGPT generated
    def test_write_data_in_properties_file_should_create_and_write_properties_file(self):

        # Arrange
        data = {"key1": "value1", "key2": "value2"}
        file = self.temp_dir / "test.properties"

        # Act
        self.file_management.write_data_in_properties_file(data, str(file), False)

        # Assert
        assert file.exists()
        props = _load_properties(str(file))
        assert props["key1"] == "value1"
        assert props["key2"] == "value2"

    # ChatGPT generated
    def test_write_data_in_properties_file_should_overwrite_existing_file(self):

        # Arrange
        file       = self.temp_dir / "test.properties"
        first_data = {"oldKey": "oldValue"}
        self.file_management.write_data_in_properties_file(first_data, str(file), False)

        second_data = {"newKey": "newValue"}

        # Act
        self.file_management.write_data_in_properties_file(second_data, str(file), False)

        # Assert
        props = _load_properties(str(file))
        assert props.get("oldKey") is None
        assert props["newKey"] == "newValue"

    # ChatGPT generated
    def test_write_data_in_properties_file_should_create_file_if_it_does_not_exist(self):

        # Arrange
        file = self.temp_dir / "newFile.properties"
        data = {"test": "value"}

        # Act
        self.file_management.write_data_in_properties_file(data, str(file), False)

        # Assert
        assert file.exists()

    # ChatGPT generated
    def test_write_data_in_properties_file_should_not_create_file_when_parent_directory_does_not_exist(self):

        # Arrange
        file = self.temp_dir / "unknown" / "folder" / "test.properties"
        data = {"key": "value"}

        # Act
        self.file_management.write_data_in_properties_file(data, str(file), False)

        # Assert
        assert not file.exists()
