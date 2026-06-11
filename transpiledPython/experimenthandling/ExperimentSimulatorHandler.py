#!/usr/bin/env python
""" generated source for module ExperimentSimulatorHandler """
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
import java.util.concurrent.BlockingQueue

import ch.hevs.silab.structuredsim.interfaces.ASimulationSystemHandler

import org.apache.logging.log4j.LogManager

import org.apache.logging.log4j.Logger

import ch.hevs.silab.structuredsim.util.FileManagement

# 
#  * Name : ExperimentSimulatorHandler
#  * <p>
#  * Description : This is the simulation thread
#  * <p>
#  * Date : 25 july 2017
#  * @version 1.0
#  * @author Caroline Taramarcaz
#  
class ExperimentSimulatorHandler(Runnable):
    """ generated source for class ExperimentSimulatorHandler """
    #  Variable
    environnmentQueue = BlockingQueue()
    resultsQueue = BlockingQueue()
    glueCode = ASimulationSystemHandler()
    options = Options()
    fm = FileManagement()

    # private static final Logger logger = LogManager.getLogger(ExperimentSimulatorHandler.class.__name__);
    plan = ExperimentPlanGenerator()

    # 
    # 	 * Constructor of the second thread for the simulation
    # 	 * 
    # 	 * @param environnementQueue
    # 	 *            : The BlockignQueue where the environment will be saved
    # 	 * @param o
    # 	 *            : options object
    # 	 * @param glueCode
    # 	 *            : Class of the glueCode
    # 	 
    def __init__(self, environnementQueue, resultsQueue, o, glueCode, fm, plan):
        """ generated source for method __init__ """
        super(ExperimentSimulatorHandler, self).__init__()
        self.environnmentQueue = environnementQueue
        self.options = o
        self.glueCode = ASimulationSystemHandler(glueCode)
        self.resultsQueue = resultsQueue
        self.fm = fm
        self.plan = plan

    # 
    # 	 * Method to save the result
    # 	 * @return path where the file will be saved
    # 	 
    def run(self):
        """ generated source for method run """
        result = ExperimentResultHandler(self.resultsQueue, self.glueCode, self.fm, self.options)
        resultThread = Thread(result)
        resultThread.setName("Result Thread")
        while True:
            try:
                # logger.debug("Size of the Simulation Queue : " + len(environnmentQueue));
                self.glueCode.startSimulation(self.options.getPathParameters())
                # logger.debug(resultPathForThisSimulation);
                self.fm.copyFile(self.options.pathToSimulatorResultFile, resultPathForThisSimulation)
                self.fm.copyFile(self.options.pathToSimulatorResultFile, self.options.pathSimulator + "/" + env.pathSaveResult.substring(env.pathSaveResult.lastIndexOf("/") + 1, len(env.pathSaveResult)) + "/results_sim" + env.id + ".txt")
                self.resultsQueue.add(resultPathForThisSimulation)
                #  to get out of the loop
                if self.plan.isFinish:
                    if self.environnmentQueue.isEmpty():
                        # logger.debug("It's empty ! and it's not the first time that we try to read the queue !");
                        break
            except Exception as e:
                e.printStackTrace()
                # logger.error("Error in the run of the Thread Simulator");
            if not ((True)):
                break
        resultThread.start()

