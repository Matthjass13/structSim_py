#!/usr/bin/env python
""" generated source for module StartProgram """
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
# package: ch.hevs.silab.structuredsim.interfaces
import java.io.IOException

import java.io.InputStream

import java.util.Vector

import java.util.concurrent.BlockingQueue

import java.util.concurrent.PriorityBlockingQueue

import ch.hevs.silab.structuredsim.experimenthandling.Environment

import ch.hevs.silab.structuredsim.experimenthandling.ExperimentPlanGenerator

import ch.hevs.silab.structuredsim.experimenthandling.ExperimentSimulatorHandler

import ch.hevs.silab.structuredsim.experimenthandling.Options

import ch.hevs.silab.structuredsim.experimenthandling.Parameter

import ch.hevs.silab.structuredsim.gluecode.Simulation

import ch.hevs.silab.structuredsim.util.FileManagement

# 
#  * Name : StartProgram
#  * <p>
#  * Description : Class to start the program. Need to use the method startProgram.
#  * <p>
#  * Date : 25 july 2017
#  * @version 1.0
#  * @author Audrey Dupont
#  
class StartProgram(object):
    """ generated source for class StartProgram """
    # 
    # 	 * Method to start the program
    # 	 * 
    # 	 * @param pathConfigFile : Path to the confi file
    # 	 * @param glueCode : glue code object
    # 	 * @throws IOException
    # 	 
    @classmethod
    def startProgram(cls, pathConfigFile, glueCode):
        """ generated source for method startProgram """
        fm = FileManagement()
        #  Create an instance of the "GlueCode"
        glueCodeClass = ASimulationSystemHandler(glueCode)
        #  Load the configuration properties file
        o = fm.loadDataFromPropertiesFile(pathConfigFile)
        #  Parameter
        #  Get the List of the Parameters
        listParam = None
        isParams = Simulation.__class__.getClassLoader().getResourceAsStream(o.getPathParameters())
        listParam = glueCodeClass.readParametersFile(isParams)
        baseEnv = Environment(0, listParam, 1)
        queue = PriorityBlockingQueue()
        resultQueue = PriorityBlockingQueue()
        glueCodeClass.setOptions(o)
        if not o.getTypeOfCuttOfPlanning() == "CRITERIA" or o.getStopCriteria() > 0:
            planningThread.setName("Planning Thread")
            planningThread.start()
            simultationThread.setName("Simulation Thread")
            simultationThread.start()

