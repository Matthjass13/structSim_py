#!/usr/bin/env python
""" generated source for module Measure """
# 
# * Copyright (c) 2017 HES-SO Valais - Smart Infrastructure Laboratory (http://silab.hes.ch)
# *
# * This file is part of StructuredSimulationFramework.
# *
# * The StructuredSimulationFramework is free software: you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation, either version 3 of the License, or
# * (at your option) any later version.
# *
# * The StructuredSimulationFramework is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
#  * See the GNU General Public License for more details.
# *
#  * You should have received a copy of the GNU General Public License
# * along with StructuredSimulationFramework.
# * If not, see <http://www.gnu.org/licenses/>.
# * 
# package: ch.hevs.silab.structuredsim.experimenthandling
# 
#  * Name : Measure
#  * <p>
#  * Description : This class define characteristics of Measure that can be extract from simulation's results files.
#  * <p>
#  * Date : 25 july 2017
#  * @version 1.0
#  * @author Caroline Taramarcaz
#  *
#  
class Measure(object):
    """ generated source for class Measure """
    #  Variables
    key = str()
    value = str()

    # 
    # 	 * Constructor of the class Measure
    # 	 * 
    # 	 * @param key : key of the measure
    # 	 * @param value : value of the measure
    # 	 
    def __init__(self, key, value):
        """ generated source for method __init__ """
        self.key = key
        self.value = value

    # 
    # 	 * Getter for value
    # 	 * @return value
    # 	 
    def getValue(self):
        """ generated source for method getValue """
        return self.value

    # 
    # 	 * Setter for value
    # 	 * @param value : value
    # 	 
    def setValue(self, value):
        """ generated source for method setValue """
        self.value = value

    # 
    # 	 * Getter for key
    # 	 * @return key
    # 	 
    def getKey(self):
        """ generated source for method getKey """
        return self.key

    # 
    # 	 * Setter for key
    # 	 * @param key : key
    # 	 
    def setKey(self, key):
        """ generated source for method setKey """
        self.key = key

    def __str__(self):
        """ generated source for method toString """
        return "Key : " + self.key + " Value : " + self.value

