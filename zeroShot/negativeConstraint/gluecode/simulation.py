from gluecode.concrete_modifier import ConcreteModifier
from gluecode.simple_simulation_handler import SimpleSimulationHandler
from interfaces.start_program import StartProgram


class Simulation(StartProgram):
    """Concrete entry point mirroring Simulation.java."""

    @staticmethod
    def main():
        config_file = "config.properties"

        modifiers = [
            ConcreteModifier("val2", '+', 1.0, 0.5),
            ConcreteModifier("val2", '+', 10.0, 0.5),
        ]

        ssh = SimpleSimulationHandler(modifiers)
        StartProgram.start_program(config_file, ssh)


def main():
    config_file = "config.properties"

    modifiers = [
        ConcreteModifier("val2", '+', 1.0, 0.5),
        ConcreteModifier("val2", '+', 10.0, 0.5),
    ]

    ssh = SimpleSimulationHandler(modifiers)

    StartProgram.start_program(config_file, ssh)


if __name__ == "__main__":
    main()
