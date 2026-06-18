from gluecode.concrete_modifier import ConcreteModifier
from gluecode.simple_simulation_handler import SimpleSimulationHandler
from interfaces.start_program import StartProgram


def main():
    """
    Entry point – mirrors Simulation.java.

    Loads config.properties from the working directory, registers two
    ConcreteModifiers, and launches the three-thread simulation pipeline.
    """
    config_path = "config.properties"

    modifiers = [
        ConcreteModifier("val2", "+", 1.0, 0.5),
        ConcreteModifier("val2", "+", 10.0, 0.5),
    ]

    handler = SimpleSimulationHandler(modifiers)
    StartProgram.start_program(config_path, handler)


if __name__ == "__main__":
    main()
