#!/usr/bin/env python
""" generated source for module AModifier """
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
# package: ch.hevs.silab.structuredsim.interfaces
import java.util.Vector

import ch.hevs.silab.structuredsim.experimenthandling.Environment

import ch.hevs.silab.structuredsim.experimenthandling.Options

import ch.hevs.silab.structuredsim.experimenthandling.Parameter

# 
#  * Name : AModifier
#  * <p>
#  * Description : This interface define a method to modify the value of a parameter
#  * <p>
#  * Date : 25 july 2017
#  * @version 1.0
#  * @author Caroline Taramarcaz
#  *
#  
class AModifier(object):
    """ generated source for class AModifier """
    probability = float()
    name = str()

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        self.probability = 0.0
        self.name = "AModifier"

    # 
    # 	 * This constructor is used in the integration tests
    # 	 * @param probability
    # 	 * @param name
    # 	 
    @__init__.register(object, float, str)
    def __init___0(self, probability, name):
        """ generated source for method __init___0 """
        self.probability = probability
        self.name = name

    # 
    # 	 * Method to apply like an Algorithm to modify a parameters </br>
    # 	 * In case you must change the value from another parameters : 
    # 	 * <ul>
    # 	 * <li>
    # 	 * set the probability with the method setProbability
    # 	 * </li>
    # 	 * <li>
    # 	 * set the value "ValueToChange" from the object options. <p><i>Example : options.setValueToChange("val2");</i>
    # 	 * </li>
    # 	 * <li>
    # 	 * use the method getParameterToModify to get the Parameter. <p><i>Example : Parameters newParam = getParameterToModify(env.getSetOfParameters(), options.getValueToChange);</i>
    # 	 * </li>
    # 	 * </ul>
    # 	 * @param env : Environment. An Environment is one state of the simulation at the instant T.
    # 	 * @return : environment.
    # 	 
    def applyModifier(self, env):
        """ generated source for method applyModifier """

    # 
    # 	 * Getter for probability
    # 	 * @return probability
    # 	 
    def getProbability(self):
        """ generated source for method getProbability """
        return self.probability

    # 
    # 	 * Setter of probability
    # 	 * @param probability : probability
    # 	 
    def setProbability(self, probability):
        """ generated source for method setProbability """
        self.probability = probability

    def getName(self):
        """ generated source for method getName """
        return self.name

    def setName(self, name):
        """ generated source for method setName """
        self.name = name

