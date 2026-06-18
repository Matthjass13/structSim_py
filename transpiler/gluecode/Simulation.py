#!/usr/bin/env python
""" generated source for module Simulation """
# package: ch.hevs.silab.structuredsim.gluecode
import ch.hevs.silab.structuredsim.interfaces.AModifier

import ch.hevs.silab.structuredsim.interfaces.StartProgram

import java.io.IOException

import java.io.InputStream

import java.util.ArrayList

import java.util.List

class Simulation(StartProgram):
    """ generated source for class Simulation """
    #  Mock-up code for a simple simulation
    @classmethod
    def main(cls, args):
        """ generated source for method main """
        pathConfigFile = Simulation.__class__.getClassLoader().getResourceAsStream("config.properties")
        modifiers = ArrayList()
        modifiers.add(ConcreteModifier("val2", '+', 1.0, 0.5))
        modifiers.add(ConcreteModifier("val2", '+', 10.0, 0.5))
        ssh = SimpleSimulationHandler(modifiers)
        startProgram(pathConfigFile, ssh)


if __name__ == '__main__':
    import sys
    Simulation.main(sys.argv)

