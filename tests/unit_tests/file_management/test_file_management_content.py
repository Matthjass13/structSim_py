"""
Java source : unitTests/fileManagement/FileManagementContentTests.java
Extends     : FileManagementTests  →  setup fixture in conftest.py

Translation notes:
  - @BeforeEach + @TempDir  →  autouse fixture injecting self.file_management / self.temp_dir
  - Files.writeString(path, content)            →  path.write_text(content)
  - Files.write(path, List.of("a","b","c"))     →  path.write_text("a\\nb\\nc\\n")
    (Java writes each string as a separate line with OS line separator)
  - Files.createFile(path)                      →  path.touch()
"""

import pytest


class TestFileManagementContent:
    """Tests FileManagement methods related to file reading."""

    DELTA = 1e-9

    @pytest.fixture(autouse=True)
    def setup(self, tmp_path, file_management):
        self.file_management = file_management
        self.temp_dir        = tmp_path

    # Claude generated
    def test_content_of_a_file_should_return_error_message_when_file_does_not_exist(self):

        # Arrange
        self.file_management.set_filename("/noFile.txt")

        # Act
        result = self.file_management.content_of_a_file()

        # Assert
        assert result == "this is not a file"

    # Claude generated
    def test_content_of_a_file_should_return_content_when_file_exists(self):

        # Arrange
        temp_file = self.temp_dir / "test.txt"
        temp_file.write_text("Hello World")
        self.file_management.set_filename(str(temp_file))

        # Act
        result = self.file_management.content_of_a_file()

        # Assert
        assert result == "Hello World"

    # Claude generated
    def test_content_of_a_file_should_concatenate_lines_when_file_has_multiple_lines(self):

        # Arrange
        temp_file = self.temp_dir / "multiline.txt"
        # Files.write(path, List.of("line1","line2","line3")) writes one line per entry
        temp_file.write_text("line1\nline2\nline3\n")
        self.file_management.set_filename(str(temp_file))

        # Act
        result = self.file_management.content_of_a_file()

        # Assert
        assert result == "line1line2line3"

    # Claude generated
    def test_content_of_a_file_should_return_empty_string_when_file_is_empty(self):

        # Arrange
        temp_file = self.temp_dir / "empty.txt"
        temp_file.touch()
        self.file_management.set_filename(str(temp_file))

        # Act
        result = self.file_management.content_of_a_file()

        # Assert
        assert result == ""
