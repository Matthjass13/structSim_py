#!/usr/bin/env python
""" generated source for module Parameter """
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
#  * Name : Parameters
#  * <p>
#  * Description : This class define characteristics of Parameters
#  * </p>
#  * Date : 15 july 2015
#  * @version 1.0
#  * @author Caroline Taramarcaz.
#  
class Parameter(object):
    """ generated source for class Parameter """
    key = str()
    value = float()

    # 
    # 	 * Constructor of the class Parameters
    # 	 * @param key : key of the parameter
    # 	 * @param value : value of the parameter
    # 	 
    @overloaded
    def __init__(self, key, value):
        """ generated source for method __init__ """
        self.key = key
        self.value = value

    # 
    # 	 * Constructor
    # 	 * @param p : parameters
    # 	 
    @__init__.register(object, Parameter)
    def __init___0(self, p):
        """ generated source for method __init___0 """
        self.key = p.key
        self.value = p.value

    def __str__(self):
        """ generated source for method toString """
        return "key : " + self.key + " value : " + self.value

    # 
    # 	 * Getter for the key
    # 	 * @return key
    # 	 
    def getKey(self):
        """ generated source for method getKey """
        return self.key

    # 
    # 	 * Setter for the key
    # 	 * @param key : key
    # 	 
    def setKey(self, key):
        """ generated source for method setKey """
        self.key = key

    # 
    # 	 * Getter for the value
    # 	 * @return value
    # 	 
    def getValue(self):
        """ generated source for method getValue """
        return self.value

    # 
    # 	 * Setter for the value
    # 	 * @param value : value
    # 	 
    def setValue(self, value):
        """ generated source for method setValue """
        self.value = value

