# Cura PostProcessingPlugin
# Author: Erik Bongers - based on DisplayFilenameAndLayerOnLCD by Amanda de Castilho
# Date:     July 5, 2019

# Description:  This plugin inserts a line at the start of each layer
#               The line contains
#                   - a user-defined label or the filename
#                   - the current layer
#                   - total number of layers.
#               The G-code M117 is used to display the full message.
# TODO:
#
from ..Script import Script
from UM.Application import Application

class DisplayFileAndLayersV2(Script):
    def __init__(self):
        super().__init__()

    def getSettingDataString(self):
        return """{
            "name": "Display filename and layer V2",
            "key": "DisplayFileAndLayersV2",
            "metadata": {},
            "version": 2,
            "settings":
            {
                "name":
                {
                    "label": "text to display:",
                    "description": "By default the current filename will be displayed on the LCD. Enter text here to override the filename and display something else.",
                    "type": "str",
                    "default_value": ""
                }
            }
        }"""
    
    def execute(self, data):
        maxLineLen = 19 # change this value for longer or shorter line lenghts on the display of your printer.
        if self.getSettingValueByKey("name") != "":
            name = self.getSettingValueByKey("name")
        else:
            name = Application.getInstance().getPrintInformation().jobName       
        i = 1
        layerCnt = 0
        for layer in data:
            layer_index = data.index(layer)
            lines = layer.split("\n")
            for line in lines:
                if line.startswith(";LAYER:"):
                    layerCnt += 1

        for layer in data:
            txtLayers = str(i) + "/" + str(layerCnt)
            display_text = "M117 " + name[0:maxLineLen-len(txtLayers)] + " " + txtLayers
            layer_index = data.index(layer)
            lines = layer.split("\n")
            for line in lines:
                if line.startswith(";LAYER:"):
                    line_index = lines.index(line)
                    lines.insert(line_index + 1, display_text)
                    i += 1
            final_lines = "\n".join(lines)
            data[layer_index] = final_lines
            
        return data
