"""
Java source : unitTests/fileManagement/FileManagementExportFilesTests.java
Extends     : FileManagementTests  →  setup fixture in conftest.py

Translation notes:
  - In Java, each test method declares its OWN @TempDir Path tempDir parameter,
    which shadows the class-level @TempDir from the parent.
    In Python, tmp_path is injected directly as a test method parameter,
    which gives each test method its own fresh temporary directory.
    The autouse setup fixture does NOT set self.temp_dir here (intentional).
  - Vector<Measure>  →  list[Measure]
  - Files.exists(path)       →  path.exists()
  - Files.readAllLines(path) →  path.read_text().splitlines()
"""

import pytest
from structuredsim.experimenthandling import Measure


class TestFileManagementExportFiles:
    """Tests FileManagement methods related to measures and modifiers export."""

    @pytest.fixture(autouse=True)
    def setup(self, file_management):
        # No self.temp_dir here: each test injects its own tmp_path (see Java)
        self.file_management = file_management

    # ChatGPT generated
    def test_create_measures_file_should_create_measures_file(self, tmp_path):

        # Arrange
        measures = [
            Measure("throughput", "12"),
            Measure("latency",    "50"),
        ]
        measures_file = tmp_path / "measures.txt"

        # Act
        self.file_management.create_measures_file(measures, str(measures_file))

        # Assert
        assert measures_file.exists()
        lines = measures_file.read_text().splitlines()
        assert len(lines) == 2
        assert lines[0] == "throughput=12"
        assert lines[1] == "latency=50"

    # ChatGPT generated
    def test_create_modifier_file_should_create_summary_file(self, tmp_path):

        # Arrange
        modifier = "SIMULATION_FINISHED"

        # Act
        self.file_management.create_modifier_file(str(tmp_path), modifier)

        # Assert
        summary_file = tmp_path / "SummaryFile.txt"
        assert summary_file.exists()
        lines = summary_file.read_text().splitlines()
        assert len(lines) == 1
        assert lines[0] == modifier
