#!/usr/bin/env python
""" generated source for module IManageParametersFile """
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
import java.io.InputStream

import java.util.Vector

import ch.hevs.silab.structuredsim.experimenthandling.Parameter

# 
#  * Name : IManageParametersFile
#  * <p>
#  * Description : This interface define methods to manage parameters files .
#  * <p>
#  * Date : 25 July 2017
#  * @version 1.0 
#  * @author Caroline Taramarcaz
#  
class IManageParametersFile(object):
    """ generated source for interface IManageParametersFile """
    __metaclass__ = ABCMeta
    # 
    # 	 * Method to read a parameters File used by your simulator.
    # 	 * 
    # 	 * @param parametersFilePath : Path where the parameters File is saved. This path is describe on the config.properties file.
    # 	 * @return :The return variable must be a vector of Parameter.
    # 	 * @see Parameter
    # 	 
    @abstractmethod
    @overloaded
    def readParametersFile(self, parametersFilePath):
        """ generated source for method readParametersFile """

    # 
    # 	 * Method to read parameters from an InputStream instead
    # 	 * @author Matthias Gaillard
    # 	 
    @abstractmethod
    @readParametersFile.register(object, InputStream)
    def readParametersFile_0(self, inputStream):
        """ generated source for method readParametersFile_0 """

    # 
    # 	 * Method to write a new file of parameters that will be used by your
    # 	 * simulator EACH TIME that a Parameter change !
    # 	 * 
    # 	 * @param setOfParameters : Vector of Parameters that must be saved.
    # 	 * @param locationToStore
    # 	 *            : Path where the parameters file we'll be saved. </br>
    # 	 *            Each new parameters file are saved in the corresponding
    # 	 *            simulation folder. </br>
    # 	 *            <i>Example : {pathOUT}/sim1 = Folder of the 1st
    # 	 *            simulation.</i>
    # 	 *            <p>
    # 	 *            Don't forget to insert the name of your file. </br>
    # 	 *            Example : {registrationPath} + "/MyParametersFile.txt"
    # 	 *            </p>
    # 	 * @see Parameter
    # 	 
    @abstractmethod
    def writeParametersFile(self, setOfParameters, locationToStore):
        """ generated source for method writeParametersFile """

