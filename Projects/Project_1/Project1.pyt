# -*- coding: utf-8 -*-

import arcpy
from Project_1 import importJSON

class Toolbox:
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the 
        name of the .pyt file).
        """
        self.label = "Toolbox"
        self.alias = "toolbox"
        
        # List of tool classes associated with this toolbox
        self.tools = [Tool]




class Tool:
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Project1 tool"
        self.description = ""

    def getParameterInfo(self):
        """Define the tool parameters."""
        input_json = arcpy.Parameter(
            name='input_json',
            displayName='Input JSON file',
            direction = 'Input',
            datatype = 'DEFile',
            parameterType = 'Required'
        )
        outputfile = arcpy.Parameter(
            name='outputfile',)
            
            




def isLicensed(self):
    """
    Set whether the tool is licensed to execute.
    """
    return True

def updateParameters(self, parameters):
    """
    Modify the values and properties of parameters before internal
    validation is performed. This method is called whenever a parameter
    has been changed.
    """
    return

def updateMessages(self, parameters):
    """
    Modify the messages created by internal validation for each tool
    parameters. This method is called after internal validation.
    """
    return

def execute(self, parameters, messages):
    """This source code of the tool."""
    input = parameters[0].valuesAsText
    output = parameters[1].valueAsText
    importJSON()
    return

def postExecute(self, parameters):
    """This method takes place after outputs ate processed and 
    added to the display.
    """
    return