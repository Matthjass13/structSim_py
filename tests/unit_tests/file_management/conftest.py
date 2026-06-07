"""
Shared fixtures for all file_management tests.

Java equivalent: FileManagementTests.java
  - @BeforeEach setUp()      → file_management fixture
  - @TempDir Path tempDir    → tmp_path pytest built-in fixture (injected in each class)

The file_management fixture is automatically discovered by pytest for every
test module in this directory; each test class injects it via an autouse setup.
"""

import pytest
from structuredsim.util import FileManagement

@pytest.fixture
def file_management():
    """Provides a fresh FileManagement instance for each test."""
    return FileManagement()
