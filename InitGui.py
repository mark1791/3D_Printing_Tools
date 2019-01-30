# -*- coding: utf-8 -*-

__title__ = "Mesh Utilities workbench"
__author__ = "Mark Hillier"
__license__ = "LGPL 2.1"
__doc__ = "FreeCAD workbench that offers a collection of tools mainly related to Scaling Meshes and modifiying geometry properties."

import os
import sys
import _SMutils

path_scaleWB = os.path.dirname(_SMutils.__file__)
#sys.path.append(os.path.join(path_scaleWB, 'Gui'))
path_scaleWB_icons =  os.path.join( path_scaleWB, 'Resources', 'icons')
_SMutils.setIconsPath(path_scaleWB_icons)
global main_ScaleWB_Icon
main_ScaleWB_Icon = os.path.join( path_scaleWB_icons , 'Scale_Mesh.svg')


class ScriptXWorkbench (Workbench): 
    MenuText = "Mesh Utils"
    global main_ScaleWB_Icon
    Icon = main_ScaleWB_Icon
	
    def Initialize(self):
	  import SM_MeshBox_Geom # Mesh Box creates a 150mm cubed size mesh box to simulate printer bed size
	  import SM_Graphic_Properties # Import Graphic Properties Code
	  import SM_Mesh_Utils # Import Mesh utilitys Module
	  import SM_Mesh_Solid # Import module to convert a mesh to a refined Solid
	  import Test_Mod # Test Code Module
	  
	  list = ["Scale_Imperial_mm","Scale_mm_imperial","Descale_Geometry","Scale50_Geometry","ReScale_Fit_Printer_Geometry","BoxMesh_Geometry","Solid_Mesh_Refined_Cmd_Geometry","Transparency50_Object","Transparency100_Object","Hide_Object","Show_Object","Random_Colour_Object","White_Colour_Object","Yellow_Colour_Object","Orange_Colour_Object","Red_Colour_Object","Pink_Colour_Object","Purple_Colour_Object","Blue_Colour_Object","Cyan_Colour_Object","Green_Colour_Object","Brown_Colour_Object","Black_Colour_Object","Line_Width_Change_Object","Test_Geometry"] # Contains the commands
	  self.appendToolbar("My Scripts",list) 
        
Gui.addWorkbench(ScriptXWorkbench())