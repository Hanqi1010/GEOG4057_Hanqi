# -*- coding: utf-8 -*-
import random
import arcpy

class Toolbox(object):
    def __init__(self):
        self.label = "Random Sampling Tools"
        self.alias = "randomsampling"
        # List of tool classes associated with this toolbox
        self.tools = [RandomSampleTool]

class RandomSampleTool(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Random Sampling Tool"
        self.description = ""
        self.canRunInBackground = False
        
    def getParameterInfo(self):
        """Define parameter definitions"""
        input_features = arcpy.Parameter(
            name="input_features",
            displayName="Input Features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input")
        output_features = arcpy.Parameter(
            name="output_features",
            displayName="Output Features",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Output")
        no_of_features = arcpy.Parameter(
            name="number_of_features",
            displayName="Number of Features",
            datatype="GPLong",
            parameterType="Required",
            direction="Input")
        no_of_features.filter.type = "Range"
        no_of_features.filter.list = [1, 100000]
        parameters = [input_features, output_features, no_of_features]
        return parameters


    def isLicensed(self):
        """Set whether the tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter. This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        inputfc = parameters[0].valueAsText
        outputfc = parameters[1].valueAsText
        outcount = parameters[2].value
        inlist = []
        with arcpy.da.SearchCursor(inputfc, "OID@") as cursor:
            for row in cursor:
                id = row[0]
                inlist.append(id)
        randomlist = random.sample(inlist, outcount)
        desc = arcpy.da.Describe(inputfc)
        fldname = desc["OIDFieldName"]
        sqlfield = arcpy.AddFieldDelimiters(inputfc, fldname)
        sqlexp = f"{sqlfield} IN {tuple(randomlist)}"
        arcpy.Select_analysis(inputfc, outputfc, sqlexp)
        messages.addMessage("{0} random features selected from {1}".format(outcount,inputfc))
        return
    

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
