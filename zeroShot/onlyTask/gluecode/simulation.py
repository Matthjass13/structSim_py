from noStrategy.gluecode.concrete_modifier import ConcreteModifier
from noStrategy.gluecode.simple_simulation_handler import SimpleSimulationHandler
from noStrategy.start_program import StartProgram


class Simulation(StartProgram):

    @staticmethod
    def main():
        config_file = "config.properties"

        modifiers = [
            ConcreteModifier("val2", '+', 1.0, 0.5),
            ConcreteModifier("val2", '+', 10.0, 0.5),
        ]

        ssh = SimpleSimulationHandler(modifiers)

        StartProgram.start_program(config_file, ssh)


if __name__ == "__main__":
    Simulation.main()
