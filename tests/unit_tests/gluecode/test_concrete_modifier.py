"""
Java source : unitTests/gluecode/ConcreteModifierTests.java

Translation notes:
  - extends TestCase (JUnit 4) + @Test (JUnit 5)  →  pytest class, no inheritance
  - @ParameterizedTest @CsvSource with switch      →  @pytest.mark.parametrize with
    statement for expected values                     an explicit expected column;
                                                      cleaner and avoids branching in tests
  - Vector<Parameter>                              →  plain Python list
  - findValue (Java static method)                 →  ConcreteModifier.find_value (static)
  - assertEquals(double, double, delta)            →  assert == pytest.approx(abs=DELTA)
"""

import pytest
from structuredsim.experimenthandling import Environment, Parameter
from structuredsim.gluecode import ConcreteModifier


DELTA = 1e-9


class TestConcreteModifier:

    @pytest.mark.parametrize("operator, value, expected", [
        ('+', 1, 2.0),    # 1 + 1 = 2
        ('-', 2, -1.0),   # 1 - 2 = -1
        ('*', 3,  3.0),   # 1 * 3 = 3
        ('/', 4,  0.25),  # 1 / 4 = 0.25
    ])
    def test_apply_modifier_should_update_environment_correctly(
        self, operator: str, value: float, expected: float
    ):
        # Arrange
        e = Environment()
        v = [Parameter("val1", 1)]
        e.set_set_of_parameters(v)
        modifier = ConcreteModifier("val1", operator, value)

        # Act
        e = modifier.apply_modifier(e)

        # Assert
        assert e.get_set_of_parameters()[0].get_value() == pytest.approx(expected, abs=DELTA)

    def test_find_value_should_find_value_in_a_list(self):

        # Arrange
        params = [
            Parameter("val1",  3),
            Parameter("val2", 10),
            Parameter("val3",  7),
        ]

        # Act
        result = ConcreteModifier.find_value(params, "val2")

        # Assert
        assert result == pytest.approx(10, abs=DELTA)

    def test_find_value_should_return_minus_1_when_nothing_is_found(self):

        # Arrange
        params = [
            Parameter("val1",  3),
            Parameter("val2", 10),
            Parameter("val3",  7),
        ]

        # Act
        result = ConcreteModifier.find_value(params, "val31416")

        # Assert
        assert result == pytest.approx(-1, abs=DELTA)
