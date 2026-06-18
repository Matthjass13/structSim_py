#!/usr/bin/env python
""" generated source for module FileManagement """
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
# package: ch.hevs.silab.structuredsim.util
import 

import java.io.BufferedReader

import java.io.BufferedWriter

import java.io.File

import java.io.FileInputStream

import java.io.FileNotFoundException

import java.io.FileOutputStream

import java.io.FileReader

import java.io.FileWriter

import java.io.IOException

import java.io.InputStream

import java.nio.file_.Files

import java.nio.file_.Path

import java.nio.file_.Paths

import java.nio.file_.StandardCopyOption

import java.util.Calendar

import java.util.LinkedHashMap

import java.util.Properties

import java.util.Vector

import ch.hevs.silab.structuredsim.interfaces.ASimulationSystemHandler

import org.apache.logging.log4j.LogManager

import org.apache.logging.log4j.Logger

import ch.hevs.silab.structuredsim.experimenthandling.Environment

import ch.hevs.silab.structuredsim.experimenthandling.Measure

import ch.hevs.silab.structuredsim.experimenthandling.Options

# 
#  * The goal of this class is to manage parameters and/or results files.
#  * <ul>
#  * <li>read data of the file</li>
#  * <li>put <key,value> data in an hashmap</li>
#  * <li>save a file</li>
#  * <li>get a value : give the key and receive back the corresponding value</li>
#  * </ul>
#  * Created on 09-07-2015. </br>
#  * Inspired by a class written by Marco Bruchmann and Rene Schumann
#  * 
#  * @author Caroline_Taramarcaz
#  * 
#  
class FileManagement(object):
    """ generated source for class FileManagement """
    #  Variables
    filename = str()
    options = Options()
    pathResult = str()
    pathSimulator = str()

    #  private static final Logger logger = LogManager.getLogger(FileManagement.class.__name__);
    # 
    # 	 * Empty Constructor
    # 	 
    def __init__(self):
        """ generated source for method __init__ """
        self.options = Options()

    # 
    # 	 * This method return a String with the content of a file
    # 	 * 
    # 	 * @return String
    # 	 * @throws IOException
    # 	 
    def contentOfAFile(self):
        """ generated source for method contentOfAFile """
        contentFile = ""
        if not (File(self.filename).isFile()):
            return "this is not a file"
        try:
            while (line = in_.readLine()) != None:
                contentFile = contentFile + line
            in_.close()
        except FileNotFoundException as e:
            e.printStackTrace()
            #  logger.info("Just a stack trace", e);
        return contentFile

    # 
    # 	 * This method move a file from a folder to another folder.
    # 	 * 
    # 	 * @param originFile
    # 	 *            : Origin path folder
    # 	 * @param destinationFile
    # 	 *            : destination path folder
    # 	 
    def moveFile(self, originFile, destinationFile):
        """ generated source for method moveFile """
        originPath = Paths.get(originFile)
        if not Files.exists(originPath):
            return
        destinationPath = Paths.get(destinationFile)
        try:
            Files.move(originPath, destinationPath, REPLACE_EXISTING)
        except IOException as e:
            # logger.error("Impossible to move this file");
            e.printStackTrace()

    # 
    # 	 * This method copy a file to another folder
    # 	 * 
    # 	 * @param file
    # 	 *            : Origin File to copy
    # 	 * @param destination
    # 	 *            : Destination folder
    # 	 
    def copyFile(self, file_, destination):
        """ generated source for method copyFile """
        fileToCopy = File(file_)
        dest = File(destination)
        try:
            Files.copy(fileToCopy.toPath(), dest.toPath(), StandardCopyOption.REPLACE_EXISTING)
        except Exception as e:
            pass
            # logger.error("This file in this folder already exist");

    #  Method to create an empty Folder
    # 	 * 
    # 	 * @param folderPath : Path
    # 	 
    def createFolder(self, folderPath):
        """ generated source for method createFolder """
        File(folderPath).mkdir()

    # 
    # 	 * Method to save the simulation result in a file
    # 	 * 
    # 	 * @param result : result to save
    # 	 * @param env : environment of the simulation
    # 	 * @return <b>String</b> : Path of the file where is saved the result file
    # 	 * @throws IOException
    # 	 
    def saveSimultationResult(self, result, env):
        """ generated source for method saveSimultationResult """
        properties = Properties()
        properties.put("Result", result)
        filePath = self.options.getFolderPathOUT() + "/" + "_sim" + env.getId() + "/results.txt"
        fops = FileOutputStream()
        try:
            fops = FileOutputStream(filePath, True)
            properties.store(fops, None)
            fops.flush()
            fops.close()
        except FileNotFoundException as e:
            e.printStackTrace()
            # logger.error("File not Found");
        return filePath

    # 
    # 	 * Method to load data from a properties file and put in an Hashmap
    # 	 * 
    # 	 * @param filePath
    # 	 *            : Path of the file
    # 	 * @return Options
    # 	 
    @overloaded
    def loadDataFromPropertiesFile(self, filePath):
        """ generated source for method loadDataFromPropertiesFile """
        properties = Properties()
        try:
            properties.load(ips)
            ips.close()
        except IOException as e:
            e.printStackTrace()
            # logger.error("Error to load Data from Properties file");
        cuttOfValue = properties.getProperty("cuttOfPlanning", "")
        for key in properties.stringPropertyNames():
            if key=="pathParameters":
                self.options.setPathParameters(properties.getProperty(key))
            elif key=="pathOUT":
                self.options.setFolderPathOUT(properties.getProperty(key))
            elif key=="pathSimulator":
                self.options.setPathSimulator(properties.getProperty(key))
            elif key=="pathToSimulatorResultFile":
                self.options.setPathToSimulatorResultFile(properties.getProperty(key))
            elif key=="cuttOfPlanning":
                cuttOfValue = properties.getProperty(key)
            elif key=="typeCuttOfPlanning":
                self.options.setTypeOfCuttOfPlanning(properties.getProperty(key))
                if properties.getProperty(key)=="INT":
                    self.options.setCuttOfPlanning(Integer.parseInt(cuttOfValue))
                elif properties.getProperty(key)=="DAY":
                    cal1.set(Calendar.DATE, Integer.parseInt(cuttOfValue))
                    self.options.setCuttOfPlanningH(cal1)
                elif properties.getProperty(key)=="HOURS":
                    cal2.set(Calendar.HOUR_OF_DAY, Integer.parseInt(cuttOfValue))
                    self.options.setCuttOfPlanningH(cal2)
                elif properties.getProperty(key)=="MINUTES":
                    cal3.set(Calendar.MINUTE, Integer.parseInt(cuttOfValue))
                    self.options.setCuttOfPlanningH(cal3)
                elif properties.getProperty(key)=="CRITERIA":
                    self.options.setStopCriteria(Double.parseDouble(cuttOfValue))
        return self.options

    # 
    # 	 * Same method as the previous one,
    # 	 * but using an InputStream instead of a String
    # 	 * @param ips
    # 	 * @return Options
    # 	 
    @loadDataFromPropertiesFile.register(object, InputStream)
    def loadDataFromPropertiesFile_0(self, ips):
        """ generated source for method loadDataFromPropertiesFile_0 """
        properties = Properties()
        try:
            properties.load(ips)
            ips.close()
        except IOException as e:
            e.printStackTrace()
            # logger.error("Error to load Data from Properties file");
        #  1. Read all simple values
        self.options.setPathParameters(properties.getProperty("pathParameters"))
        self.options.setFolderPathOUT(properties.getProperty("pathOUT"))
        self.options.setPathSimulator(properties.getProperty("pathSimulator"))
        self.options.setPathToSimulatorResultFile(properties.getProperty("pathToSimulatorResultFile"))
        #  2. Treat independant values
        cuttOfValue = properties.getProperty("cuttOfPlanning", "")
        typeCuttOf = properties.getProperty("typeCuttOfPlanning", "")
        self.options.setTypeOfCuttOfPlanning(typeCuttOf)
        if typeCuttOf=="INT":
            self.options.setCuttOfPlanning(Integer.parseInt(cuttOfValue))
        elif typeCuttOf=="DAY":
            cal1.set(Calendar.DATE, Integer.parseInt(cuttOfValue))
            self.options.setCuttOfPlanningH(cal1)
        elif typeCuttOf=="HOURS":
            cal2.set(Calendar.HOUR_OF_DAY, Integer.parseInt(cuttOfValue))
            self.options.setCuttOfPlanningH(cal2)
        elif typeCuttOf=="MINUTES":
            cal3.set(Calendar.MINUTE, Integer.parseInt(cuttOfValue))
            self.options.setCuttOfPlanningH(cal3)
        elif typeCuttOf=="CRITERIA":
            self.options.setStopCriteria(Double.parseDouble(cuttOfValue))
        return self.options

    # 
    # 	 * Method to write something in a properties file parameters :
    # 	 * <ul>
    # 	 * <li>String resultToWrite : The string to write in the file</li>
    # 	 * <li>String resultsFilePath : The path of the file</li>
    # 	 * <li>boolean keepPreviousResults
    # 	 * <ul>
    # 	 * <li>true if the new results has to be written at the end of the existing
    # 	 * file</li>
    # 	 * <li>false if the text of the file has to be overwritten.</li>
    # 	 * </ul>
    # 	 * </ul>
    # 	 * @param dataToWrite : an hashmap of data to write
    # 	 * @param filePath : path to the file
    # 	 * @param keepPreviousResults : to keep previous result or not?
    # 	 * 
    # 	 
    def writeDataInPropertiesFile(self, dataToWrite, filePath, keepPreviousResults):
        """ generated source for method writeDataInPropertiesFile """
        try:
            properties.putAll(dataToWrite)
            #  Write the results in the existing file, at the end of the file,
            # 			don't deleted what is already in the file.
            # 			Does create the file if it does not exist,
            # 			but launch exception when the folder is missing
            properties.store(fops, None)
            fops.close()
        except IOException as e:
            pass
            # logger.error(e.__str__());

    # 
    # 	 * Method to create a new folder for each simulation
    # 	 * @param e : current environment
    # 	 * @return return the string path where the folder is created
    # 	 
    def createNewFolder(self, e):
        """ generated source for method createNewFolder """
        self.pathResult = options.getFolderPathOUT() + "/" + "_sim" + e.getId()
        # create folder
        self.createFolder(self.pathResult)
        self.pathSimulator = options.getPathSimulator() + "/" + "_sim" + e.getId() + "/"
        self.createFolder(self.pathSimulator)
        return self.pathResult

    # 
    # 	 * Method to create a new Folder for the simulation
    # 	 * @param env : Environment
    # 	 * @exception IOException if the file can't be copied
    # 	 
    def createNewFolderSimulation(self, env, glueCode):
        """ generated source for method createNewFolderSimulation """
        pathNewFolder = self.createNewFolder(env)
        env.setPathSaveResult(pathNewFolder)
        # Save the new parameters file
        glueCode.writeParametersFile(env.getSetOfParameters(), pathNewFolder)
        content = File(self.pathResult).listFiles()
        for f in content:
            self.pathSimulator += f.__name__
            try:
                Files.copy(f.toPath(), newFile.toPath(), StandardCopyOption.REPLACE_EXISTING)
            except IOException as e:
                e.printStackTrace()
                # logger.error("Error when we create the new Folder of the simulation. "
                # + "Is the path in the config properties right ? ");

    def createMeasuresFile(self, measures, measuresFilePath):
        """ generated source for method createMeasuresFile """
        try:
            for m in measures:
                bw.write(m.getKey() + "=" + m.getValue())
                bw.newLine()
            bw.flush()
            bw.close()
        except Exception as e:
            pass
            # logger.error("Error whent we create de measures file");

    def createModifierFile(self, path, modifier):
        """ generated source for method createModifierFile """
        try:
            bw.write(modifier)
            bw.newLine()
            bw.flush()
            bw.close()
        except IOException as e:
            e.printStackTrace()
            # logger.error("Error to save the summary File");

    def getFilename(self):
        """ generated source for method getFilename """
        return self.filename

    def setFilename(self, filename):
        """ generated source for method setFilename """
        self.filename = filename

    def getOptions(self):
        """ generated source for method getOptions """
        return self.options

    def setOptions(self, options):
        """ generated source for method setOptions """
        self.options = options

