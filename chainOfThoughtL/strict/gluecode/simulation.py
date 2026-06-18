from interfaces.start_program import StartProgram
from gluecode.concrete_modifier import ConcreteModifier
from gluecode.simple_simulation_handler import SimpleSimulationHandler


class Simulation(StartProgram):
    @staticmethod
    def main():
        """
        Main entry point.
        Loads config.properties from the current working directory,
        sets up modifiers and the simulation handler, then starts the experiment.
        """
        path_config_file = "config.properties"

        modifiers = [
            ConcreteModifier("val2", '+', 1.0, 0.5),
            ConcreteModifier("val2", '+', 10.0, 0.5),
        ]

        ssh = SimpleSimulationHandler(modifiers)
        StartProgram.start_program(path_config_file, ssh)


if __name__ == "__main__":
    Simulation.main()
