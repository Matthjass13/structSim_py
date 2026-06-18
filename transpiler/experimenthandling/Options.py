#!/usr/bin/env python
""" generated source for module Options """
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
import java.util.Calendar

# 
#  * Name : Options
#  * <p>
#  * Description : Class to specify the options to run the simulation
#  * <p>
#  * Date : 25 july 2017
#  * @version 1.0
#  * @author Audrey Dupont
#  *
#  
class Options(object):
    """ generated source for class Options """
    pathParameters = str()
    folderPathOUT = str()
    pathSimulator = str()
    cuttOfPlanning = int()
    cuttOfPlanningH = Calendar()
    typeOfCuttOfPlanning = str()
    stopCriteria = float()
    pathToSimulatorResultFile = str()

    def __init__(self):
        """ generated source for method __init__ """

    # 
    # 	 * Getter for pathParameters
    # 	 * @return path of the parameters
    # 	 
    def getPathParameters(self):
        """ generated source for method getPathParameters """
        return self.pathParameters

    # 
    # 	 * Setter for pathParameters
    # 	 * @param pathParameters : path of the parameters
    # 	 
    def setPathParameters(self, pathParameters):
        """ generated source for method setPathParameters """
        self.pathParameters = pathParameters

    # 
    # 	 * Getter for folderPathOut
    # 	 * @return path of the folder where the result will be save
    # 	 
    def getFolderPathOUT(self):
        """ generated source for method getFolderPathOUT """
        return self.folderPathOUT

    # 
    # 	 * Setter for folderPathOut
    # 	 * @param folderPathOUT : path of the folder where the result will be save
    # 	 
    def setFolderPathOUT(self, folderPathOUT):
        """ generated source for method setFolderPathOUT """
        self.folderPathOUT = folderPathOUT

    # 
    # 	 * Getter for pathSimulator
    # 	 * @return path of Simulator
    # 	 
    def getPathSimulator(self):
        """ generated source for method getPathSimulator """
        return self.pathSimulator

    # 
    # 	 * Setter for pathSimulator
    # 	 * @param pathSimulator : path of the simulator
    # 	 
    def setPathSimulator(self, pathSimulator):
        """ generated source for method setPathSimulator """
        self.pathSimulator = pathSimulator

    # 
    # 	 * Getter for cuttOfPlanning
    # 	 * @return when to stop the planning simulation
    # 	 
    def getCuttOfPlanning(self):
        """ generated source for method getCuttOfPlanning """
        return self.cuttOfPlanning

    # 
    # 	 * Setter for cuttOfPlanning
    # 	 * @param cuttOfPlanning : when to stop the planning simulation
    # 	 
    def setCuttOfPlanning(self, cuttOfPlanning):
        """ generated source for method setCuttOfPlanning """
        self.cuttOfPlanning = cuttOfPlanning

    # 
    # 	 * Getter for cuttOfPlanningH
    # 	 * @return time when to stop the planning simulation
    # 	 
    def getCuttOfPlanningH(self):
        """ generated source for method getCuttOfPlanningH """
        return self.cuttOfPlanningH

    # 
    # 	 * Setter for cuttOfPlanningH 
    # 	 * @param cuttOfPlanningH : time when to stop the planning simulation
    # 	 
    def setCuttOfPlanningH(self, cuttOfPlanningH):
        """ generated source for method setCuttOfPlanningH """
        self.cuttOfPlanningH = cuttOfPlanningH

    # 
    # 	 * Getter for typeOfCuttOfPlanning
    # 	 * @return the type of cuttOfPlanning
    # 	 
    def getTypeOfCuttOfPlanning(self):
        """ generated source for method getTypeOfCuttOfPlanning """
        return self.typeOfCuttOfPlanning

    # 
    # 	 * Setter for typeOfCuttOfPlanning
    # 	 * @param typeOfCuttOfPlanning : the type of cuttOfPlanning
    # 	 
    def setTypeOfCuttOfPlanning(self, typeOfCuttOfPlanning):
        """ generated source for method setTypeOfCuttOfPlanning """
        self.typeOfCuttOfPlanning = typeOfCuttOfPlanning

    # 
    # 	 * Getter for stopCriteria
    # 	 * @return stop criteria
    # 	 
    def getStopCriteria(self):
        """ generated source for method getStopCriteria """
        return self.stopCriteria

    # 
    # 	 * Setter for stopCriteria
    # 	 * @param stopCriteria : stop criteria
    # 	 
    def setStopCriteria(self, stopCriteria):
        """ generated source for method setStopCriteria """
        self.stopCriteria = stopCriteria

    # 
    # 	 * Getter for pathToSimulatorResultFolder
    # 	 * @return pathToSimulatorResultFolder
    # 	 * 
    def getPathToSimulatorResultFile(self):
        """ generated source for method getPathToSimulatorResultFile """
        return self.pathToSimulatorResultFile

    # 
    # 	 * Setter for pathToSimulatorResultFolder
    # 	 * @param pathToSimulatorResultFile
    # 	 * 
    def setPathToSimulatorResultFile(self, pathToSimulatorResultFile):
        """ generated source for method setPathToSimulatorResultFile """
        self.pathToSimulatorResultFile = pathToSimulatorResultFile

