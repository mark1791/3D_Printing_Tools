import FreeCAD, FreeCADGui, Draft
#from FreeCAD import Base, Console
import FreeCAD as App

class TestCmd: 
   def Activated(self): 
		# -*- coding: utf-8 -*-
		
		# List all objects of the document
		doc = FreeCAD.ActiveDocument
		objs = FreeCAD.ActiveDocument.Objects
		#App.Console.PrintMessage(str(objs) + "\n")
		#App.Console.PrintMessage(str(len(FreeCAD.ActiveDocument.Objects)) + " Objects"  + "\n")

		for obj in objs:
				a = obj.Name                                             # list the Name  of the object  (not modifiable)
				b = obj.Label                                            # list the Label of the object  (modifiable)
				try:
					c = obj.LabelText                                    # list the LabeText of the text (modifiable)
					App.Console.PrintMessage(str(a) +" "+ str(b) +" "+ str(c) + "\n") # Displays the Name the Label and the text
				except:
					App.Console.PrintMessage(str(a) +" "+ str(b) + "\n") # Displays the Name and the Label of the object

         #doc.removeObject("Box") # Clears the designated object
   def GetResources(self): 
       return {'Pixmap' : 'path_to_an_icon/myicon.png', 'MenuText': 'Short text', 'ToolTip': 'Reduces Mesh by 95%'} 
       
FreeCADGui.addCommand('Test_Geometry', TestCmd())
