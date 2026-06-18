"""
Chain-of-thought for Simulation:
1. Java-specific constructs:
   - Extends StartProgram (inherits static method).
   - main(String[] args) entry point.
   - Simulation.class.getClassLoader().getResourceAsStream("config.properties") for classpath loading.
   - new ArrayList<AModifier>() with add() calls.
2. Python equivalents:
   - Class inherits from StartProgram (or just calls start_program directly since it's static).
   - if __name__ == "__main__" replaces main().
   - Config file loaded from same directory as this script using pathlib.
   - List literal for modifiers.
3. Risks/deviations:
   - Java loads config.properties as a classpath resource; Python loads it relative to this file.
   - The config.properties and params.properties files must exist alongside the script or at
     the paths configured within config.properties.
"""

import os
import sys
from pathlib import Path

# Allow running from any working directory
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gluecode.concrete_modifier import ConcreteModifier
from gluecode.simple_simulation_handler import SimpleSimulationHandler
from interfaces.start_program import StartProgram


class Simulation(StartProgram):
    """Main entry point — mirrors the Java Simulation class."""
    pass


if __name__ == "__main__":
    config_file = Path(__file__).parent / "config.properties"

    modifiers = [
        ConcreteModifier("val2", "+", 1.0, 0.5),
        ConcreteModifier("val2", "+", 10.0, 0.5),
    ]

    ssh = SimpleSimulationHandler(modifiers)
    Simulation.start_program(str(config_file), ssh)
