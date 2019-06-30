# -*- coding: utf-8 -*-

__title__ = "3D Printing Tools workbench"
__author__ = "Mark Hillier"
__license__ = "LGPL 2.1"
__doc__ = "FreeCAD workbench that offers a collection of tools mainly related to Scaling Meshes and modifiying geometry properties to help when preparing to do 3D Printing."

import os
import sys
import _SMutils

path_scaleWB = os.path.dirname(_SMutils.__file__)
#sys.path.append(os.path.join(path_scaleWB, 'Gui'))
path_scaleWB_icons =  os.path.join( path_scaleWB, 'Resources', 'icons')
_SMutils.setIconsPath(path_scaleWB_icons)
global main_ScaleWB_Icon
main_ScaleWB_Icon = os.path.join( path_scaleWB_icons , '3D_Printing_Tools.svg')


class ScriptXWorkbench (Workbench): 
	MenuText = "3D Printing Tools"
	global main_ScaleWB_Icon
	Icon = main_ScaleWB_Icon
	
	def Initialize(self):
		import SM_Graphic_Properties # Import Graphic Properties Code
		import SM_Mesh_Utils # Import Mesh utilitys Module
		import SM_Mesh_Solid # Import module to convert a mesh to a refined Solid

		list = ["Scale_Imperial_mm","Scale_mm_imperial","Descale_Geometry","Scale50_Geometry","Scale_Factor_Geom","ReScale_Fit_Printer_Geometry","BoxMesh_Geometry","Solid_Mesh_Refined_Cmd_Geometry","Transparency50_Object","Transparency100_Object","Hide_Object","Show_Object","Random_Colour_Object","White_Colour_Object","Yellow_Colour_Object","Orange_Colour_Object","Red_Colour_Object","Pink_Colour_Object","Purple_Colour_Object","Blue_Colour_Object","Cyan_Colour_Object","Green_Colour_Object","Brown_Colour_Object","Black_Colour_Object","Line_Width_Change_Object","Bounding_Box_Geom","Bed_length_S","Die_Length_S","Scale_Factor_S"] # Contains the commands
		self.appendToolbar("My Scripts",list) 
        
Gui.addWorkbench(ScriptXWorkbench())
