#!/usr/bin/env python
""" generated source for module ConcreteModifier """
# package: ch.hevs.silab.structuredsim.gluecode
import ch.hevs.silab.structuredsim.experimenthandling.Environment

import ch.hevs.silab.structuredsim.experimenthandling.ExperimentPlanGenerator

import ch.hevs.silab.structuredsim.experimenthandling.Parameter

import ch.hevs.silab.structuredsim.interfaces.AModifier

import org.apache.logging.log4j.LogManager

import org.apache.logging.log4j.Logger

import java.util.Vector

class ConcreteModifier(AModifier):
    """ generated source for class ConcreteModifier """
    #  private static final Logger logger = LogManager.getLogger(ConcreteModifier.class.__name__);
    keyToChange = str()
    operator = Character()

    # 
    #      * Value to add/substract/multiply/divide to the key
    #      
    delta = float()

    @overloaded
    def __init__(self, keyToChange, operator, delta, probability):
        """ generated source for method __init__ """
        super(ConcreteModifier, self).__init__(operator + "" + delta)
        self.keyToChange = keyToChange
        self.probability = probability
        self.operator = operator
        self.delta = delta

    @__init__.register(object, str, Character, float)
    def __init___0(self, keyToChange, operator, delta):
        """ generated source for method __init___0 """
        super(ConcreteModifier, self).__init__()
        self.__init__(keyToChange, operator, delta, 1)

    @__init__.register(object, float)
    def __init___1(self, delta):
        """ generated source for method __init___1 """
        super(ConcreteModifier, self).__init__()
        self.__init__("val1", '*', delta, delta)

    @__init__.register(object)
    def __init___2(self):
        """ generated source for method __init___2 """
        super(ConcreteModifier, self).__init__()

    def applyModifier(self, env):
        """ generated source for method applyModifier """
        params = env.getSetOfParameters()
        for p in params:
            #  logger.debug("param=" + p.getKey() + " keyToChange=" + keyToChange);
            if p.getKey() == self.keyToChange:
                if self.operator=='+':
                    p.setValue(p.getValue() + self.delta)
                elif self.operator=='-':
                    p.setValue(p.getValue() - self.delta)
                elif self.operator=='*':
                    p.setValue(p.getValue() * self.delta)
                elif self.operator=='/':
                    p.setValue(p.getValue() / self.delta)
        return env

    @classmethod
    def findValue(cls, params, key):
        """ generated source for method findValue """
        value = None
        for p in params:
            if p.getKey() == key:
                return p.getValue()
        return -1

