import arcpy
import time

class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "Toolbox"
        self.alias = ""

        # List of tool classes associated with this toolbox
        self.tools = [GraduatedColorsRenderer]

class GraduatedColorsRenderer(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "graduatedcolor"
        self.description = "create a graduated colored map based on a specific attribute of a layer"
        self.canRunInBackground = False
        self.category = "MapTools"

    def getParameterInfo(self):
        """Define parameter definitions"""
        # original project name
        param0 = arcpy.Parameter(
            displayName="Input ArcGIS Pro Project Name",
            name="aprxInputName",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        # which layer you want to classify to create a color map
        param1 = arcpy.Parameter(
            displayName="Layer To Classify",
            name="LayerToClassify",
            datatype="GPLayer",
            parameterType="Required",
            direction="Input"
        )
        # output folder location
        param2 = arcpy.Parameter(
            displayName="Output Location",
            name="OutputLocation",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        )
        # output project name
        param3 = arcpy.Parameter(
            displayName="Output Project Name",
            name="OutputProjectName",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        
        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        # define progessor variables
        readTime = 3 # the time for users to read the progress
        start = 0 # beginning position of the progressor
        max = 100 # end position of the progressor
        step = 33 # the progress interval to move the progressor along
        
        # setup progressor
        arcpy.SetProgressor("step", "Validating Project File...", start, max, step)
        time.sleep(readTime) # pause the execution for 3 seconds
        
        # add mesaage to the results pane
        arcpy.AddMessage("Validating Project File...")
        
        # project file
        project = arcpy.mp.ArcGISProject(parameters[0].valueAsText)
        
        # grabs the first instance of a map from the .aprx
        campus = project.listMaps('Map')[0]
        
        # increment progressor
        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Finding your map layer...")
        time.sleep(readTime)
        
        # loop through the layers of the map
        for layer in campus.listLayers():
            if layer.isFeatureLayer:
                # copy the layer's symbology
                symbology = layer.symbology
                # make sure the symbology has renderer attribute
                if hasattr(symbology, 'renderer'):
                    # check layer name
                    if layer.name == parameters[1].valueAsText: # check if the layer name matched the input layer
                        
                        # increment progressor
                        arcpy.SetProgressorPosition(start + step) # now it is 33% completed
                        arcpy.SetProgressorLabel("Calculating and classifying....")
                        time.sleep(readTime)
                        arcpy.AddMessage("Calculating and classifying...")
                        
                        # update the copy's renderer to "graduated colors renderer"
                        symbology.updateRenderer('GraduatedColorsRenderer')
                        
                        # which field arcpy should base the choropleth off of
                        symbology.renderer.classificationField = "Shape_Area"
                        
                        # increment progressor
                        arcpy.SetProgressorPosition(start + step*2) # now it is 66% completed
                        arcpy.SetProgressorLabel("Cleaning up...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Cleaning up...")
                        
                        # set number of classes for the map
                        symbology.renderer.breakCounty = 5
                        
                        # set color ramp
                        symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]
                        
                        # set the layer's actual symbology equal to the copy's
                        layer.symbology = symbology
                        
                        arcpy.AddMessage("Finish Generating Layer...")
                    else:
                        print("No layer found")
                        
        #Increment Progressor
        arcpy.SetProgressorPosition(start + step*3) # now it is 99% completed
        arcpy.SetProgressorLabel("Saving...")
        time.sleep(readTime)
        arcpy.AddMessage("Saving...")
        
        # param 2 is the folder location and param 3 is the name of the new project
        project.saveACopy(parameters[2].valueAsText + "\\" + parameters[3].valueAsText + ".aprx")
        
        return

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return