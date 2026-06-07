"""
Java source : unitTests/fileManagement/FileManagementFileOperationsTests.java
Extends     : FileManagementTests  →  setup fixture in conftest.py

Translation notes:
  - assertDoesNotThrow(() -> method()) → just call method() directly.
    In pytest, any uncaught exception automatically fails the test.
  - Files.writeString(path, content) → path.write_text(content)
  - Files.exists(path)               → path.exists()
  - Files.readString(path)           → path.read_text()
  - Files.isDirectory(path)          → path.is_dir()
  - Files.createDirectory(path)      → path.mkdir()
  - assertTrue(x, "msg")            → assert x, "msg"
  - assertFalse(x, "msg")           → assert not x, "msg"
"""

import pytest
from pathlib import Path


class TestFileManagementFileOperations:
    """Tests FileManagement methods related to file system operations."""

    @pytest.fixture(autouse=True)
    def setup(self, tmp_path, file_management):
        self.file_management = file_management
        self.temp_dir        = tmp_path

    # Claude generated
    def test_move_file_should_move_file_when_origin_exists(self):

        # Arrange
        origin      = self.temp_dir / "origin.txt"
        destination = self.temp_dir / "destination.txt"
        origin.write_text("fileContent")

        # Act
        self.file_management.move_file(str(origin), str(destination))

        # Assert
        assert not origin.exists()
        assert destination.exists()
        assert destination.read_text() == "fileContent"

    # Claude generated
    def test_move_file_should_replace_destination_when_destination_already_exists(self):

        # Arrange
        origin      = self.temp_dir / "origin.txt"
        destination = self.temp_dir / "destination.txt"
        origin.write_text("newContent")
        destination.write_text("oldContent")

        # Act
        self.file_management.move_file(str(origin), str(destination))

        # Assert
        assert not origin.exists()
        assert destination.read_text() == "newContent"

    # Claude generated
    def test_move_file_should_not_throw_when_origin_does_not_exist(self):

        # Arrange
        non_existent_origin = str(self.temp_dir / "ghost.txt")
        destination         = str(self.temp_dir / "destination.txt")

        # Act & Assert — the method catches exceptions internally; nothing should propagate
        self.file_management.move_file(non_existent_origin, destination)
        assert not Path(destination).exists()

    # Claude generated
    def test_copy_file_should_copy_file_when_source_exists(self):

        # Arrange
        source      = self.temp_dir / "source.txt"
        destination = self.temp_dir / "destination.txt"
        source.write_text("file content")

        # Act
        self.file_management.copy_file(str(source), str(destination))

        # Assert
        assert source.exists(),      "Source file must still exist after copy"
        assert destination.exists(), "Destination file must have been created"
        assert destination.read_text() == "file content"

    # Claude generated
    def test_copy_file_should_replace_destination_when_destination_already_exists(self):

        # Arrange
        source      = self.temp_dir / "source.txt"
        destination = self.temp_dir / "destination.txt"
        source.write_text("new content")
        destination.write_text("old content")

        # Act
        self.file_management.copy_file(str(source), str(destination))

        # Assert
        assert source.exists(), "Source file must still exist after copy"
        assert destination.read_text() == "new content"

    # Claude generated
    def test_copy_file_should_not_throw_when_source_does_not_exist(self):

        # Arrange
        non_existent_source = str(self.temp_dir / "ghost.txt")
        destination         = str(self.temp_dir / "destination.txt")

        # Act & Assert — the method catches Exception internally; nothing should propagate
        self.file_management.copy_file(non_existent_source, destination)
        assert not Path(destination).exists(), \
            "No destination file should be created if source does not exist"

    # Claude generated
    def test_create_folder_should_create_folder_when_path_is_valid(self):

        # Arrange
        new_folder = self.temp_dir / "newFolder"

        # Act
        self.file_management.create_folder(str(new_folder))

        # Assert
        assert new_folder.exists(),  "Folder must exist after creation"
        assert new_folder.is_dir(),  "Created path must be a directory"

    # Claude generated
    def test_create_folder_should_not_throw_when_folder_already_exists(self):

        # Arrange
        existing_folder = self.temp_dir / "existingFolder"
        existing_folder.mkdir()
        (existing_folder / "file.txt").write_text("existing content")

        # Act & Assert — mkdir() returns False silently if folder exists; no exception expected
        self.file_management.create_folder(str(existing_folder))
        assert (existing_folder / "file.txt").exists(), \
            "Existing folder content must remain intact"

    # Claude generated
    def test_create_folder_should_not_create_folder_when_parent_does_not_exist(self):

        # Arrange
        nested_folder = self.temp_dir / "nonExistentParent" / "newFolder"

        # Act
        self.file_management.create_folder(str(nested_folder))

        # Assert
        assert not nested_folder.exists(), \
            "Folder must not be created if parent directory does not exist"
