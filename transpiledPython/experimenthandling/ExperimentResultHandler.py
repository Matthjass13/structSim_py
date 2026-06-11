#!/usr/bin/env python
""" generated source for module ExperimentResultHandler """
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
import java.util.Vector

import java.util.concurrent.BlockingQueue

import ch.hevs.silab.structuredsim.interfaces.ASimulationSystemHandler

import org.apache.logging.log4j.LogManager

import org.apache.logging.log4j.Logger

import ch.hevs.silab.structuredsim.util.FileManagement

# 
#  * Name : ExperimentResultHandler
#  * <p>
#  * Description : This thread is for displaying where the results are saved
#  * <p>
#  * Date : 25 july 2017
#  * 
#  * @version 1.0
#  * @author Caroline Taramarcaz
#  *
#  
class ExperimentResultHandler(Runnable):
    """ generated source for class ExperimentResultHandler """
    #  Variable
    resultsQueue = BlockingQueue()
    glueCode = ASimulationSystemHandler()
    fm = FileManagement()

    # private static final Logger logger = LogManager.getLogger(ExperimentResultHandler.class.__name__);
    options = Options()

    # 
    # 	 * Third Thread Constructor.
    # 	 * 
    # 	 * @param resultsQueue
    # 	 *            : BlockingQueue to get the list fulfilled
    # 	 * @param glueCode
    # 	 *            : Class of the glueCode
    # 	 
    def __init__(self, resultsQueue, glueCode, fm, o):
        """ generated source for method __init__ """
        super(ExperimentResultHandler, self).__init__()
        self.resultsQueue = resultsQueue
        self.glueCode = ASimulationSystemHandler(glueCode)
        self.fm = fm
        self.options = o

    def run(self):
        """ generated source for method run """
        # 
        # 			 * fm.saveSummaryFile(resultsQueue); code to create summaryFile...
        # 			 * Need to be modify
        # 			 * 
        # 			 * // Print the path for (Environment env : resultsQueue) {
        # 			 * print "->" + env.getPathSaveResult(); Path path =
        # 			 * Paths.get(env.getPathSaveResult()); path = path.getParent(); File
        # 			 * content[] = new File(path.__str__()).listFiles(); for (File f :
        # 			 * content) { File newFileResult = new
        # 			 * File(options.getPathSimulator() + "/" + "_sim" + env.getId() +
        # 			 * "/results.txt"); try { if (f.__name__.contains("results")) {
        # 			 * Files.copy(f.toPath(), newFileResult.toPath(),
        # 			 * StandardCopyOption.REPLACE_EXISTING); } } catch (IOException e) {
        # 			 * e.printStackTrace(); } }
        # 			 * 
        # 			 * }
        # 			 
        if not self.resultsQueue.isEmpty():
            for str_ in resultsQueue:
                # logger.debug("Result queue string : " + str);
                # logger.debug("Folder where it's saved : " + folderToSave);
                # logger.debug("Name Simulation : " + nameSimulation) ;
                self.fm.createMeasuresFile(measures, folderToSave + "/measures.txt")
                self.fm.copyFile(folderToSave + "/measures.txt", self.options.pathSimulator + "/" + nameSimulation + "/measures.txt")
        else:
            Thread.currentThread().interrupt()

