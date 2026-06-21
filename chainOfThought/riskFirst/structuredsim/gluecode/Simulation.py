from typing import IO, List, Union

from gluecode.ConcreteModifier import ConcreteModifier
from gluecode.SimpleSimulationHandler import SimpleSimulationHandler
from interfaces.AModifier import AModifier
from interfaces.StartProgram import StartProgram


class Simulation(StartProgram):
    """
    Entry point class for the simulation framework.

    Java static main() with ClassLoader.getResourceAsStream() →
    Python start_program() that accepts a path or binary stream,
    so it works both when called from the CLI and from tests.
    """

    def main(self) -> None:
        """Convenience entry point using bundled default config."""
        import importlib.resources as pkg_resources
        import structuredsim.resources as res_pkg  # noqa: F401 — package marker

        with pkg_resources.open_binary("structuredsim.resources", "config.properties") as config:
            modifiers: List[AModifier] = [
                ConcreteModifier("val2", "+", 1.0, 0.5),
                ConcreteModifier("val2", "+", 10.0, 0.5),
            ]
            ssh = SimpleSimulationHandler(modifiers)
            self.start_program(config, ssh)


if __name__ == "__main__":
    Simulation().main()
