#!/usr/bin/env python
""" generated source for module SimpleSimulationHandler """
# package: ch.hevs.silab.structuredsim.gluecode
import ch.hevs.silab.structuredsim.experimenthandling.Measure

import ch.hevs.silab.structuredsim.interfaces.AModifier

import ch.hevs.silab.structuredsim.experimenthandling.Parameter

import ch.hevs.silab.structuredsim.interfaces.ASimulationSystemHandler

import java.io

import java.util.ArrayList

import java.util.List

import java.util.Vector

class SimpleSimulationHandler(ASimulationSystemHandler):
    """ generated source for class SimpleSimulationHandler """
    modifiers = ArrayList()

    @overloaded
    def __init__(self):
        """ generated source for method __init__ """
        super(SimpleSimulationHandler, self).__init__()

    @__init__.register(object, List)
    def __init___0(self, modifiers):
        """ generated source for method __init___0 """
        super(SimpleSimulationHandler, self).__init__()
        self.modifiers = modifiers

    def extractMeasures(self, resultsFilePath):
        """ generated source for method extractMeasures """
        separator = "="
        measuresList = Vector()
        measureKey = str()
        measureValue = str()
        in_ = BufferedReader()
        try:
            in_ = BufferedReader(InputStreamReader(FileInputStream(resultsFilePath), "UTF-8"))
            while (line = in_.readLine()) != None:
                measureKey = line.substring(0, pos)
                measureValue = (line.substring(pos + 1, len(line)))
                measuresList.add(Measure(measureKey, measureValue))
            in_.close()
        except IOException as e:
            e.printStackTrace()
        return measuresList

    def initiateModifierList(self):
        """ generated source for method initiateModifierList """
        listModifierClass = modifiers
        return listModifierClass

    @overloaded
    def readParametersFile(self, parametersFilePath):
        """ generated source for method readParametersFile """
        separator = "="
        parametersList = Vector()
        key = str()
        value = float()
        in_ = BufferedReader()
        try:
            in_ = BufferedReader(InputStreamReader(FileInputStream(parametersFilePath), "UTF-8"))
            while (line = in_.readLine()) != None:
                key = line.substring(0, pos)
                value = Double.parseDouble(line.substring(pos + 1, len(line)))
                parametersList.add(Parameter(key, value))
            in_.close()
        except IOException as e:
            e.printStackTrace()
        return parametersList

    @readParametersFile.register(object, InputStream)
    def readParametersFile_0(self, inputStream):
        """ generated source for method readParametersFile_0 """
        separator = "="
        parametersList = Vector()
        key = str()
        value = float()
        try:
            while (line = in_.readLine()) != None:
                key = line.substring(0, pos)
                value = Double.parseDouble(line.substring(pos + 1, len(line)))
                parametersList.add(Parameter(key, value))
            in_.close()
        except IOException as e:
            e.printStackTrace()
        return parametersList

    def writeParametersFile(self, setOfParameters, locationToStore):
        """ generated source for method writeParametersFile """
        try:
            for p in setOfParameters:
                bw.write(p.getKey() + "=" + p.getValue())
                bw.newLine()
            bw.flush()
            bw.close()
        except Exception as e:
            e.printStackTrace()

    def startSimulation(self, pathToInputFile):
        """ generated source for method startSimulation """
        resultFile = options.getPathToSimulatorResultFile()
        File(resultFile).getParentFile().mkdirs()
        try:
            File(resultFile).createNewFile()
        except IOException as e:
            e.printStackTrace()

    def stopProgram(self):
        """ generated source for method stopProgram """

