# CuraScripts
Extension scripts for the Cura slicer (3D printing)

## DisplayFileAndLayersV2
This script is an alternative to (and based on) the original DisplayFilenameAndLayerOnLCD.py script by Amanda de Castilho, that comes preinstalled with Cura.
It shows the following at the LCD screen:
  - The filename or a user text
  - The current layer being printed
  - The total number of layers

The length of the full text line is limited to 21 characters, which is the limit of the LCD on an Ender 3 printer.
The filename or user text is trimmed to accomodate this, so that the layer numbers are always in view.
The layer numbering starts at 1, as opposed to 0-based indexing. (not all 3D-printer users are programmers :) )

The script is tested with Cura 4.1.0, but will probably work with version 3 as well.

To install:
  * open Cura > Help menu > Show Configuration Folder
  * Save script in this folder.
After installation it should appear in the Post-processing/Modify G-code extension.
