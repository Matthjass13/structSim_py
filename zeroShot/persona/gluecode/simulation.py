from gluecode.concrete_modifier import ConcreteModifier
from gluecode.simple_simulation_handler import SimpleSimulationHandler
from interfaces.start_program import StartProgram


class Simulation(StartProgram):
    """
    Concrete entry point – mirrors Simulation.java (extends StartProgram).
    Inherits start_program() as a static method callable on instances.
    """
    pass


def main():
    config_path = "config.properties"

    modifiers = [
        ConcreteModifier("val2", "+", 1.0, 0.5),
        ConcreteModifier("val2", "+", 10.0, 0.5),
    ]

    handler = SimpleSimulationHandler(modifiers)
    Simulation.start_program(config_path, handler)


if __name__ == "__main__":
    main()
