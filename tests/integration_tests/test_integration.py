"""
Java source : integrationTests/IntegrationTests.java

Tests the overall behavior of the framework.
Checks whether the output summary file is correctly computed given inputs.
Scenarios are illustrated with pictures in the integrationTests/ folder.

Translation notes:
  - System.getProperty("java.io.tmpdir").replace("\\","/") → tempfile.gettempdir()
  - Two path constants: PATH_OUT and PATH_SIM (pathSIM is new vs original Java version)
  - Files.createDirectories(pathOUT/pathSIM) → Path(...).mkdir(parents=True, exist_ok=True)
  - Thread.sleep(200)                →  time.sleep(0.2)   (ms → seconds)
  - Arrays.copyOfRange(arr, 0, n)    →  arr[:n]
  - BufferedReader/FileReader        →  built-in open()
  - new File(path).delete()          →  Path(path).unlink(missing_ok=True)
  - Files.createTempDirectory(...)   →  tempfile.mkdtemp()
  - BufferedWriter/FileWriter        →  open(..., 'w')
  - new FileInputStream(file)        →  open(file, 'rb')
  - Comparator.reverseOrder() walk   →  sorted(rglob('*'), reverse=True)
  - @ParameterizedTest @CsvSource    →  @pytest.mark.parametrize
  - List<AModifier>                  →  list[AModifier]
  - assertTrue(msg, cond)            →  assert cond, msg  (note: Java arg order is reversed)
"""

import os
import tempfile
import time
import pytest
from pathlib import Path
from typing import List

from structuredsim.gluecode import ConcreteModifier, SimpleSimulationHandler, Simulation
from structuredsim.interfaces import AModifier


class TestIntegration:
    """
    Java equivalent:
      private String pathOUT = System.getProperty("java.io.tmpdir").replace("\\","/") + "/structsim-results";
      private String pathSIM = System.getProperty("java.io.tmpdir").replace("\\","/") + "/structsim-simulator";
    """

    PATH_OUT = tempfile.gettempdir().replace("\\", "/") + "/structsim-results"
    PATH_SIM = tempfile.gettempdir().replace("\\", "/") + "/structsim-simulator"

    # ------------------------------------------------------------------ #
    #  Helper: scenario data                                               #
    # ------------------------------------------------------------------ #

    def _return_modifiers_from_scenario(self, scenario: int) -> List[AModifier]:
        """Returns a list of predefined modifiers depending on a scenario number."""
        if scenario == 1:
            return [ConcreteModifier(0.5)]
        elif scenario == 2:
            return [ConcreteModifier(0.2), ConcreteModifier(0.5)]
        elif scenario == 4:
            return [
                ConcreteModifier(0.1),
                ConcreteModifier(0.8),
                ConcreteModifier(0.5),
                ConcreteModifier(0.2),
            ]
        return []

    def _return_expected_lines_from_scenario(self, scenario: int) -> List[str]:
        """
        Returns the expected summary file lines depending on a scenario number.
        The tree might not be written fully depending on the cutoff value.
        """
        if scenario == 1:
            return [
                "Simulation ID : 1\t Probability : 0.5\t Modifier implemented :    *0.5",
                "Simulation ID : 2\t Probability : 0.25\t Modifier implemented :    *0.5   *0.5",
                "Simulation ID : 3\t Probability : 0.125\t Modifier implemented :    *0.5   *0.5   *0.5",
                "Simulation ID : 4\t Probability : 0.0625\t Modifier implemented :    *0.5   *0.5   *0.5   *0.5",
            ]
        elif scenario == 2:
            return [
                "Simulation ID : 1\t Probability : 0.2\t Modifier implemented :    *0.2",
                "Simulation ID : 2\t Probability : 0.5\t Modifier implemented :    *0.5",
                "Simulation ID : 3\t Probability : 0.1\t Modifier implemented :    *0.5   *0.2",
                "Simulation ID : 4\t Probability : 0.25\t Modifier implemented :    *0.5   *0.5",
                "Simulation ID : 5\t Probability : 0.05\t Modifier implemented :    *0.5   *0.5   *0.2",
                "Simulation ID : 6\t Probability : 0.125\t Modifier implemented :    *0.5   *0.5   *0.5",
                "Simulation ID : 7\t Probability : 0.04000000000000001\t Modifier implemented :    *0.2   *0.2",
                "Simulation ID : 8\t Probability : 0.1\t Modifier implemented :    *0.2   *0.5",
                "Simulation ID : 9\t Probability : 0.025\t Modifier implemented :    *0.5   *0.5   *0.5   *0.2",
                "Simulation ID : 10\t Probability : 0.0625\t Modifier implemented :    *0.5   *0.5   *0.5   *0.5",
                "Simulation ID : 11\t Probability : 0.020000000000000004\t Modifier implemented :    *0.5   *0.2   *0.2",
                "Simulation ID : 12\t Probability : 0.05\t Modifier implemented :    *0.5   *0.2   *0.5",
                "Simulation ID : 13\t Probability : 0.020000000000000004\t Modifier implemented :    *0.2   *0.5   *0.2",
                "Simulation ID : 14\t Probability : 0.05\t Modifier implemented :    *0.2   *0.5   *0.5",
            ]
        elif scenario == 4:
            return [
                "Simulation ID : 1\t Probability : 0.1\t Modifier implemented :    *0.1",
                "Simulation ID : 2\t Probability : 0.8\t Modifier implemented :    *0.8",
                "Simulation ID : 3\t Probability : 0.5\t Modifier implemented :    *0.5",
                "Simulation ID : 4\t Probability : 0.2\t Modifier implemented :    *0.2",

                "Simulation ID : 5\t Probability : 0.08000000000000002\t Modifier implemented :    *0.8   *0.1",
                "Simulation ID : 6\t Probability : 0.6400000000000001\t Modifier implemented :    *0.8   *0.8",
                "Simulation ID : 7\t Probability : 0.4\t Modifier implemented :    *0.8   *0.5",
                "Simulation ID : 8\t Probability : 0.16000000000000003\t Modifier implemented :    *0.8   *0.2",

                "Simulation ID : 9\t Probability : 0.06400000000000002\t Modifier implemented :    *0.8   *0.8   *0.1",
                "Simulation ID : 10\t Probability : 0.5120000000000001\t Modifier implemented :    *0.8   *0.8   *0.8",
                "Simulation ID : 11\t Probability : 0.32000000000000006\t Modifier implemented :    *0.8   *0.8   *0.5",
                "Simulation ID : 12\t Probability : 0.12800000000000003\t Modifier implemented :    *0.8   *0.8   *0.2",

                "Simulation ID : 13\t Probability : 0.051200000000000016\t Modifier implemented :    *0.8   *0.8   *0.8   *0.1",
                "Simulation ID : 14\t Probability : 0.40960000000000013\t Modifier implemented :    *0.8   *0.8   *0.8   *0.8",
                "Simulation ID : 15\t Probability : 0.25600000000000006\t Modifier implemented :    *0.8   *0.8   *0.8   *0.5",
                "Simulation ID : 16\t Probability : 0.10240000000000003\t Modifier implemented :    *0.8   *0.8   *0.8   *0.2",

                "Simulation ID : 17\t Probability : 0.05\t Modifier implemented :    *0.5   *0.1",
                "Simulation ID : 18\t Probability : 0.4\t Modifier implemented :    *0.5   *0.8",
                "Simulation ID : 19\t Probability : 0.25\t Modifier implemented :    *0.5   *0.5",
                "Simulation ID : 20\t Probability : 0.1\t Modifier implemented :    *0.5   *0.2",
            ]
        return []

    # ------------------------------------------------------------------ #
    #  Helper: filesystem cleanup                                          #
    # ------------------------------------------------------------------ #

    def _clean_output_directory(self) -> None:
        """
        Delete everything inside PATH_OUT without removing the directory itself.
        Java equivalent: Files.walk().sorted(reverseOrder()).filter(≠root).forEach(delete)
        """
        results_path = Path(self.PATH_OUT)
        if not results_path.exists():
            return
        for item in sorted(results_path.rglob("*"), reverse=True):
            try:
                if item.is_file() or item.is_symlink():
                    item.unlink()
                elif item.is_dir():
                    item.rmdir()
            except OSError:
                pass

    # ------------------------------------------------------------------ #
    #  Core helper: arrange → act → poll → assert                         #
    # ------------------------------------------------------------------ #

    def _run_and_assert_summary_file(
        self,
        cut_off_planning: str,
        type_cut_off_planning: str,
        modifiers: List[AModifier],
        expected_lines: List[str],
    ) -> None:
        """
        Shared helper used by all integration tests.
        Tests the content and line count of SummaryFile.txt.
        """
        # Arrange
        self._clean_output_directory()
        # Java: Files.createDirectories(Paths.get(pathOUT)) / Files.createDirectories(Paths.get(pathSIM))
        Path(self.PATH_OUT).mkdir(parents=True, exist_ok=True)
        Path(self.PATH_SIM).mkdir(parents=True, exist_ok=True)

        temp_dir    = tempfile.mkdtemp(prefix="structsim-test")
        temp_config = os.path.join(temp_dir, "config.properties")

        config_content = (
            f"pathOUT = {self.PATH_OUT}\n"
            "pathParameters = parameters.txt\n"
            f"pathSimulator = {self.PATH_SIM}\n"
            f"pathToSimulatorResultFile = {self.PATH_SIM}/results/results.txt\n"
            f"cuttOfPlanning = {cut_off_planning}\n"
            f"typeCuttOfPlanning = {type_cut_off_planning}\n"
        )
        with open(temp_config, "w") as f:
            f.write(config_content)

        with open(temp_config, "rb") as path_config_file:
            ssh = SimpleSimulationHandler(modifiers)

            # Act
            s = Simulation()
            s.start_program(path_config_file, ssh)

        # Poll — wait up to 15 s for SummaryFile.txt to be written and terminated by a blank line
        summary_file = Path(self.PATH_OUT) / "SummaryFile.txt"
        timeout = 15.0
        start   = time.time()
        lines: List[str] = []

        while time.time() - start < timeout:
            if summary_file.exists():
                lines = []
                found_blank_line = False
                try:
                    with open(summary_file, "r") as f:
                        for line in f:
                            if line.strip() == "":
                                found_blank_line = True
                                break
                            lines.append(line.rstrip("\r\n"))
                except IOError:
                    pass
                if found_blank_line:
                    break
            time.sleep(0.2)  # Thread.sleep(200) → time.sleep(0.2)

        # Assert
        assert summary_file.exists(), "SummaryFile.txt should exist"
        assert len(lines) == len(expected_lines), \
            f"Wrong number of simulations: expected {len(expected_lines)}, got {len(lines)}"
        for i, (actual, expected) in enumerate(zip(lines, expected_lines)):
            assert actual == expected, f"Incorrect content at line {i + 1}"

    # ------------------------------------------------------------------ #
    #  Tests                                                               #
    # ------------------------------------------------------------------ #

    @pytest.mark.parametrize("scenario_number, cut_off_planning", [
        (1, 1), (1, 2), (1, 3), (1, 4),
        (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
        (4, 1), (4, 2), (4, 3), (4, 4), (4, 5),
    ])
    def test_int_cutoff_type(self, scenario_number: int, cut_off_planning: int):
        """
        Tests the generated summary file with all scenarios and relevant INT cutoff values.
        Please don't change it, it took me a whole weekend to make it work.

        The cutoff represents the number of iterations of the algorithm
        (= number of times a node is explored).
        Lines to keep = numberOfIterations * numberOfModifiers
                      = cut_off_planning * scenario_number
        """
        type_cut_off_planning   = "INT"
        modifiers               = self._return_modifiers_from_scenario(scenario_number)
        expected_lines          = self._return_expected_lines_from_scenario(scenario_number)
        number_of_lines_to_keep = cut_off_planning * scenario_number
        exact_expected_lines    = expected_lines[:number_of_lines_to_keep]  # Arrays.copyOfRange

        self._run_and_assert_summary_file(
            str(cut_off_planning), type_cut_off_planning, modifiers, exact_expected_lines
        )

    @pytest.mark.parametrize("scenario_number, cut_off_planning, expected_number_of_lines", [
        (1, 0.1, 4), (1, 0.2, 3), (1, 0.3, 2), (1, 0.4, 2), (1, 0.5, 1),
        (1, 0.6, 1), (1, 0.7, 1), (1, 0.8, 1), (1, 0.9, 1),
        (2, 0.1, 10), (2, 0.2, 6), (2, 0.3, 4), (2, 0.4, 4), (2, 0.5, 2),
        (2, 0.6, 2),  (2, 0.7, 2), (2, 0.8, 2), (2, 0.9, 2),
        (4, 0.45, 20), (4, 0.5, 16), (4, 0.6, 12), (4, 0.7, 8), (4, 0.8, 4), (4, 0.9, 4),
    ])
    def test_criteria_cutoff_type(
        self,
        scenario_number: int,
        cut_off_planning: float,
        expected_number_of_lines: int,
    ):
        """Same as test_int_cutoff_type, but tests the CRITERIA cutoff type."""
        type_cut_off_planning = "CRITERIA"
        modifiers             = self._return_modifiers_from_scenario(scenario_number)
        expected_lines        = self._return_expected_lines_from_scenario(scenario_number)
        exact_expected_lines  = expected_lines[:expected_number_of_lines]

        self._run_and_assert_summary_file(
            str(cut_off_planning), type_cut_off_planning, modifiers, exact_expected_lines
        )

    @pytest.mark.parametrize("scenario_number, cut_off_planning, expected_number_of_lines", [
        (1, 1, 1),
        (2, 1, 2),
        (4, 1, 4),
    ])
    def test_criteria_cutoff_type_value_one(
        self,
        scenario_number: int,
        cut_off_planning: float,
        expected_number_of_lines: int,
    ):
        """
        Tests the CRITERIA cutoff type with value 1.
        With the current implementation of ExperimentPlanGenerator,
        a first iteration is always done, which is why we expect as many lines
        as there are modifiers.
        """
        type_cut_off_planning = "CRITERIA"
        modifiers             = self._return_modifiers_from_scenario(scenario_number)
        expected_lines        = self._return_expected_lines_from_scenario(scenario_number)
        exact_expected_lines  = expected_lines[:expected_number_of_lines]

        self._run_and_assert_summary_file(
            str(cut_off_planning), type_cut_off_planning, modifiers, exact_expected_lines
        )

    def test_criteria_cutoff_type_value_zero(self):
        """
        Tests the CRITERIA cutoff value of 0.
        In the current implementation, it causes the program not to run
        because the generated tree would be arithmetically infinite.
        An if statement in StartProgram prevents threads from running in this case.
        """
        type_cut_off_planning = "CRITERIA"
        scenario_number       = 1
        cut_off_planning      = 0
        modifiers             = self._return_modifiers_from_scenario(scenario_number)

        # Delete old summary file
        summary_file = Path(self.PATH_OUT) / "SummaryFile.txt"
        summary_file.unlink(missing_ok=True)

        temp_dir    = tempfile.mkdtemp(prefix="structsim-test")
        temp_config = os.path.join(temp_dir, "config.properties")

        config_content = (
            f"pathOUT = {self.PATH_OUT}\n"
            "pathParameters = parameters.txt\n"
            f"pathSimulator = {self.PATH_SIM}\n"
            f"pathToSimulatorResultFile = {self.PATH_SIM}/results/results.txt\n"
            f"cuttOfPlanning = {cut_off_planning}\n"
            f"typeCuttOfPlanning = {type_cut_off_planning}\n"
        )
        with open(temp_config, "w") as f:
            f.write(config_content)

        with open(temp_config, "rb") as path_config_file:
            ssh = SimpleSimulationHandler(modifiers)

            # Act
            s = Simulation()
            s.start_program(path_config_file, ssh)

        # Assert
        assert not summary_file.exists(), "SummaryFile.txt should not exist"
