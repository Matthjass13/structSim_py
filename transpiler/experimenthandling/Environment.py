#!/usr/bin/env python
""" generated source for module Environment """
# 
#  * Copyright (c) 2017 HES-SO Valais - Smart Infrastructure Laboratory (http://silab.hes.ch)
#  *
#  * This file is part of StructuredSimulationFramework.
#  *
#  * The StructuredSimulationFramework is free software: you can redistribute it and/or modify
#  * it under the terms of the GNU General Public License as published by
#  * the Free Software Foundation, either version 3 of the License, or
#  * (at your option) any later version.
#  *
#  * The StructuredSimulationFramework is distributed in the hope that it will be useful,
#  * but WITHOUT ANY WARRANTY; without even the implied warranty of
#  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
#  * See the GNU General Public License for more details.
#  *
#  * You should have received a copy of the GNU General Public License
#  * along with StructuredSimulationFramework.
#  * If not, see <http://www.gnu.org/licenses/>.
#  * 
# package: ch.hevs.silab.structuredsim.experimenthandling
import java.util.ArrayList

import java.util.List

import java.util.Vector

# 
#  * Name : Environment 
#  * <p>
#  * Description : An environment is the state of the simulation in the instant T. This class
#  * contains an ID, a list of Parameters and a probability that this state can
#  * occur.
#  * <p>
#  * Date : 25 july 2017
#  * @version 1.0
#  * @author Caroline Taramarcaz
#  *
#  
class Environment(Comparable, Environment):
    """ generated source for class Environment """
    id = int()
    setOfParameters = Vector()
    probability = float()
    pathSaveResult = str()
    trace = ArrayList()

    # 
    # 	 * Constructor
    # 	 * 
    # 	 * @param id : ID
    # 	 * @param setOfParameters : List of Parameters of this Environment
    # 	 * @param probability : Probability
    # 	 
    @overloaded
    def __init__(self, id, setOfParameters, probability):
        """ generated source for method __init__ """
        super(Environment, self).__init__()
        self.id = id
        self.setOfParameters = setOfParameters
        self.probability = probability

    # 
    # 	 * Constructor to create a new Environment by copy another
    # 	 * @param id : ID
    # 	 * @param e : Environment
    # 	 
    @__init__.register(object, int, Environment)
    def __init___0(self, id, e):
        """ generated source for method __init___0 """
        super(Environment, self).__init__()
        self.id = id
        self.setOfParameters = Vector()
        for p in e.setOfParameters:
            self.setOfParameters.add(Parameter(p))
            #  Constructor by copy
        self.probability = e.probability
        self.trace = ArrayList()
        for s in e.trace:
            self.trace.add(s)

    # 
    # 	 * Default constructor to facilitate the writing
    # 	 * of the units tests of the FileManagement class
    # 	 
    @__init__.register(object)
    def __init___1(self):
        """ generated source for method __init___1 """
        super(Environment, self).__init__()
        self.__init__(1, Vector(), 1)

    # 
    # 	 * Getter for id
    # 	 * @return ID
    # 	 
    def getId(self):
        """ generated source for method getId """
        return self.id

    # 
    # 	 * Getter for setOfParameters
    # 	 * @return set of parameters
    # 	 
    def getSetOfParameters(self):
        """ generated source for method getSetOfParameters """
        return self.setOfParameters

    # 
    # 	 * Setter for setOfParameters
    # 	 * @param setOfParameters : set of parameters
    # 	 
    def setSetOfParameters(self, setOfParameters):
        """ generated source for method setSetOfParameters """
        self.setOfParameters = setOfParameters

    # 
    # 	 * Getter for probability
    # 	 * @return probability
    # 	 
    def getProbability(self):
        """ generated source for method getProbability """
        return self.probability

    # 
    # 	 * Setter for probability
    # 	 * @param probability : probability
    # 	 
    def setProbability(self, probability):
        """ generated source for method setProbability """
        self.probability = probability

    # 
    # 	 * Getter for pathSaveResult
    # 	 * @return path where the result are saved
    # 	 
    def getPathSaveResult(self):
        """ generated source for method getPathSaveResult """
        return self.pathSaveResult

    # 
    # 	 * Setter for pathSaveResult
    # 	 * @param pathSaveResult : path where the result are savedt 
    # 	 
    def setPathSaveResult(self, pathSaveResult):
        """ generated source for method setPathSaveResult """
        self.pathSaveResult = pathSaveResult

    def __str__Modifier(self):
        """ generated source for method toStringModifier """
        result = ""
        for s in trace:
            result += "   " + s
        return "Simulation ID : " + self.id + "\t Probability : " + self.probability + "\t Modifier implemented : " + result

    def getTrace(self):
        """ generated source for method getTrace """
        return self.trace

    def setTrace(self, trace):
        """ generated source for method setTrace """
        self.trace = trace

    # 
    # 	 Allow to order environments by ascending order of probability
    # 	 @return
    # 	 1 if first environment is more probable,
    # 	 -1 if first environment is less probable,
    # 	 0 if they have equal probability
    # 	 
    def compareTo(self, other):
        """ generated source for method compareTo """
        return Double.compare(self.probability, other.probability)

