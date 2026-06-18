#!/usr/bin/env python
""" generated source for module ExperimentPlanGenerator """
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

import java.util.Calendar

import java.util.Collections

import java.util.List

import java.util.concurrent.BlockingQueue

import java.util.concurrent.TimeUnit

import ch.hevs.silab.structuredsim.interfaces.ASimulationSystemHandler

import org.apache.logging.log4j.LogManager

import org.apache.logging.log4j.Logger

import ch.hevs.silab.structuredsim.interfaces.AModifier

import ch.hevs.silab.structuredsim.interfaces.IManageModifier

import ch.hevs.silab.structuredsim.util.FileManagement

# 
#  * Name : ExperimentPlanGenerator
#  * <p>
#  * Description : First thread that create the "planning" queue
#  *<p>
#  * Date : 25 July 2017
#  * @version 1.0
#  * @author Caroline Taramarcaz
#  *
#  
class ExperimentPlanGenerator(Runnable):
    """ generated source for class ExperimentPlanGenerator """
    # Variable
    baseEnvironment = Environment()
    planningQueue = BlockingQueue()
    options = Options()
    glueCode = ASimulationSystemHandler()
    endTime = 0
    cuttOfFormat = ""
    result = ""
    fm = FileManagement()

    # private static final Logger logger = LogManager.getLogger(ExperimentPlanGenerator.class.__name__);
    isFinish = False

    # 
    # 	 * First Thread constructor
    # 	 * @param planningQueue : The BlockignQueue where the environment will be saved
    # 	 * @param baseEnv : the base environment. State 0
    # 	 * @param o = Options file
    # 	 * @param glueCode = Class of the glueCode
    # 	 
    def __init__(self, planningQueue, baseEnv, o, glueCode, fm):
        """ generated source for method __init__ """
        super(ExperimentPlanGenerator, self).__init__()
        self.baseEnvironment = baseEnv
        self.planningQueue = planningQueue
        self.options = o
        self.glueCode = ASimulationSystemHandler(glueCode)
        self.fm = fm
        (IManageModifier(glueCode)).initiateModifierList()

    # 
    # 	 * Creating a new Environment based on the first Environment (Base)
    # 	 * @param baseEnv : Base Environment
    # 	 * @return The new Environment created
    # 	 
    def createNextEnvironments(self, baseEnv):
        """ generated source for method createNextEnvironments """
        toExplore = ArrayList()
        self.fm.createNewFolderSimulation(baseEnv, self.glueCode)
        listModifiers = self.glueCode.getListModifierClass()
        toExplore.add(baseEnv)
        addEnvToQueue(baseEnv)
        parentEnv = Environment()
        currentEnv = Environment()
        idCpt = baseEnv.getId()
        cpt = 0
        while not toExplore.isEmpty():
            #  This break statement stops the program at the right time.
            if self.options.getTypeOfCuttOfPlanning() == "INT" and cpt >= options.getCuttOfPlanning():
                break
            parentEnv = toExplore.remove(0)
            for modifier in listModifiers:
                idCpt += 1
                currentEnv = Environment(idCpt, parentEnv)
                currentEnv = modifier.applyModifier(currentEnv)
                currentEnv.getTrace().add(modifier.__name__)
                # logger.debug("--------------------------------------------" +currentEnv.id + " " +  currentEnv.trace.__str__());
                currentEnv.setProbability(parentEnv.getProbability() * modifier.getProbability())
                if self.options.getTypeOfCuttOfPlanning() == "CRITERIA" and currentEnv.getProbability() > options.getStopCriteria():
                    toExplore.add(currentEnv)
                if self.options.getTypeOfCuttOfPlanning() == "INT":
                    toExplore.add(currentEnv)
                self.fm.createNewFolderSimulation(currentEnv, self.glueCode)
                addEnvToQueue(currentEnv)
                createModifierFile(currentEnv)
            cpt += 1
            # logger.debug("CPT : " + cpt);
            #  We sort the environments by reverse order,
            # 			to put the most probable one in first position 
            toExplore.sort(Collections.reverseOrder())

    def createModifierFile(self, e):
        """ generated source for method createModifierFile """
        newLine = System.getProperty("line.separator")
        self.result += e.toStringModifier() + newLine
        self.fm.createModifierFile(self.options.folderPathOUT, self.result)

    # 
    # 	 * Add an Environment to the BlockingQueue. A trace is printed to indicate if the environment has been added.
    # 	 * @param e : Environment to Add
    # 	 
    def addEnvToQueue(self, e):
        """ generated source for method addEnvToQueue """
        wasAdded = False
        wasAdded = planningQueue.add(e)
        # 
        # 		if(wasAdded)
        # 			logger.debug("Event : " + e.id +" is added !");
        # 		else
        # 			logger.error("Event : " + e.id +" is not added !");
        # 		

    def run(self):
        """ generated source for method run """
        # Generate the number of Environment that we want
        currentTime = System.currentTimeMillis()
        # logger.debug("option = " + options.getTypeOfCuttOfPlanning());
        if self.options.getTypeOfCuttOfPlanning()=="INT":
            self.createNextEnvironments(self.baseEnvironment)
        elif self.options.getTypeOfCuttOfPlanning()=="CRITERIA":
            self.createNextEnvironments(self.baseEnvironment)
        elif self.options.getTypeOfCuttOfPlanning()=="DAY":
            self.endTime = currentTime + TimeUnit.DAYS.toMillis(options.getCuttOfPlanningH().get(Calendar.DATE))
            self.cuttOfFormat = "TIME"
        elif self.options.getTypeOfCuttOfPlanning()=="HOURS":
            self.endTime = currentTime + TimeUnit.HOURS.toMillis(options.getCuttOfPlanningH().get(Calendar.HOUR_OF_DAY))
            self.cuttOfFormat = "TIME"
        elif self.options.getTypeOfCuttOfPlanning()=="MINUTES":
            self.endTime = currentTime + TimeUnit.MINUTES.toMillis(options.getCuttOfPlanningH().get(Calendar.MINUTE))
            self.cuttOfFormat = "TIME"
        if self.cuttOfFormat.contains("TIME"):
            while System.currentTimeMillis() < endTime:
                self.createNextEnvironments(self.baseEnvironment)
        self.isFinish = True
        self.fm.copyFile(self.options.folderPathOUT + "/SummaryFile.txt", self.options.pathSimulator + "/SummaryFile.txt")

