from gluecode.concrete_modifier import ConcreteModifier
from gluecode.simple_simulation_handler import SimpleSimulationHandler
from interfaces.start_program import StartProgram


class Simulation(StartProgram):
    """Entry point for the example simulation."""

    @staticmethod
    def main() -> None:
        modifiers = [
            ConcreteModifier("val2", "+", 1.0, 0.5),
            ConcreteModifier("val2", "+", 10.0, 0.5),
        ]

        ssh = SimpleSimulationHandler(modifiers)

        with open("config.properties", "rb") as config_file:
            StartProgram.start_program(config_file, ssh)


if __name__ == "__main__":
    Simulation.main()
