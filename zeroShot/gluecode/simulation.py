import importlib.resources
import os

from gluecode.concrete_modifier import ConcreteModifier
from gluecode.simple_simulation_handler import SimpleSimulationHandler
from interfaces.start_program import StartProgram


class Simulation(StartProgram):
    """Mock-up code for a simple simulation. Entry point for the framework."""

    @staticmethod
    def main() -> None:
        config_file_path = os.path.join(os.path.dirname(__file__), "..", "config.properties")

        modifiers = [
            ConcreteModifier("val2", "+", 1.0, 0.5),
            ConcreteModifier("val2", "+", 10.0, 0.5),
        ]

        ssh = SimpleSimulationHandler(modifiers)

        StartProgram.start_program(config_file_path, ssh)


if __name__ == "__main__":
    import logging
    logging.basicConfig(level=logging.DEBUG)
    Simulation.main()
