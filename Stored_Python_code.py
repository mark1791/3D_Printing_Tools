import Part, FreeCAD, math, PartGui, FreeCADGui
from FreeCAD import Base
import FreeCAD as App

# pick selected objects, where 1st selection is the trajectory and the 2nd is the section to sweep
s = FreeCADGui.Selection.getSelection()
try:
    shape1=s[0].Shape
    shape2=s[1].Shape
except:
    print "Wrong selection"
    return

# create a Part object
myObject=App.ActiveDocument.addObject("Part::Feature","Sweep")

makeSolid = 1
isFrenet = 1

# Create the 3d shape and set it to the Part object
Sweep = Part.Wire(shape1).makePipeShell([shape2],makeSolid,isFrenet)
myObject.Shape = Sweep

App.ActiveDocument.recompute()
obj = App.ActiveDocument.addObject('Part::Feature','NewChamfer')
App.ActiveDocument.recompute()
obj.Shape=App.ActiveDocument.Chamfer.Shape
App.ActiveDocument.ActiveObject.Label=App.ActiveDocument.Chamfer.Label

# tester for Feature Shape replacement
sel = FreeCADGui.Selection.getSelection()
if sel:
    obj = sel[0]
    sF=1.5
    myShape = obj.Shape.copy()
    myShape.scale(sF)
    Part.show(myShape)
	
	#mesh=App.ActiveDocument.ActiveObject.Mesh.copy()
		#mesh=App.activeDocument()
		#mesh.transform(mat)
		#Mesh.show(mesh)
		#import Part,PartGui 
		#doc=App.activeDocument() 
		# add a line element to the document and set its points 
		#l=Part.LineSegment()
		#l.StartPoint=(0.0,0.0,0.0)
		#l.EndPoint=(1000.0,1000.0,1000.0)
		#doc.addObject("Part::Feature","Line").Shape=l.toShape() 
		#doc.recompute()
		
		
		
		#sel = FreeCADGui.Selection.getSelectionEx()[0].ObjectName
		
		
		
		
		
		
import FreeCAD, FreeCADGui, Draft
#from FreeCAD import Base, Console
import FreeCAD as App


class TestCmd: 
   def Activated(self): 
		# -*- coding: utf-8 -*-
		import Mesh,BuildRegularGeoms
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
					#FreeCAD.Console.PrintMessage('\nWorks?\n')
					#mesh=obj.Name.Mesh.copy()
					#obj.Name.show(mesh)
					#FreeCAD.Console.PrintMessage('\nWorks?\n')
				except:
					FreeCAD.Console.PrintMessage('\nStart\n')
					App.Console.PrintMessage(str(a) +" "+ str(b) + "\n") # Displays the Name and the Label of the object
					sel = FreeCADGui.Selection.getSelection() # " sel " contains the items selected
					App.Console.PrintMessage(str(sel)+"Current Selected named part")
					#FreeCAD.Console.PrintMessage('\nWorks?\n')
					#mesh=b.Mesh.copy()
					#Mesh.show(mesh)
					FreeCAD.Console.PrintMessage('\nWorks?\n')

         #doc.removeObject("Box") # Clears the designated object
   def GetResources(self): 
       return {'Pixmap' : 'path_to_an_icon/myicon.png', 'MenuText': 'Short text', 'ToolTip': 'Reduces Mesh by 95%'} 
       
FreeCADGui.addCommand('Test_Geometry', TestCmd())




poly=Gui.Selection.getSelection()[0]
a=FreeCAD.ActiveDocument.addObject("Part::FeaturePython","CubicSurface_64")  # create an appropriate document object
AN.CubicSurface_64(a,poly) # fill that object with stuff
a.ViewObject.Proxy=0 # just set it to something different from None (this assignment is needed to run an internal notification)
a.ViewObject.DisplayMode = u"Shaded" # now you can set its display mode
a.ViewObject.ShapeColor = (0.33,0.67,1.00) # and color
FreeCAD.ActiveDocument.recompute()

a=FreeCAD.ActiveDocument.activeobject("Mesh::Feature","Cube")

import Mesh,BuildRegularGeoms
mat=FreeCAD.Matrix()
mat.scale(25.4,25.4,25.4)
mesh=App.ActiveDocument.ActiveObject.Mesh.copy()
mesh.transform(mat)
Mesh.show(mesh)

a=FreeCAD.ActiveDocument.ActiveObject.ViewObject.ShapeColor(1.0, 0.67, 1.0)
App.ActiveDocument.ActiveObject.ViewObject.ShapeColor(1.0,0.67,1.0)

FreeCADGui.getDocument("Unnamed").getObject("Cube001").ShapeColor = (0.33,0.33,0.00)

import sys
sys.path.append(FreeCADPath)
import FreeCAD
import Part
doc = FreeCAD.newDocument("doc")
v1_i = FreeCAD.Vector(0,0,0)
v2_i = FreeCAD.Vector(1,1,1)    
dir_i = v2_i - v1_i
bar_width = .25
cyl_i  = Part.makeCylinder(bar_width,dir_i.Length,v1_i,dir_i)        
cyl = doc.addObject("Part::Feature", "cyl")
cyl.Shape = cyl_i
doc.recompute()
cyl.ViewObject.DiffuseColor=(.69,.53,.31)
doc.recompute()   
Part.export(cyl,FinalPath)    
FreeCAD.closeDocument("doc")
FreeCAD.ActiveDocument = None

for obj in FreeCAD.ActiveDocument.Objects:
    if hasattr(obj,"Shape"):
        print "Object: ", obj, "Shape type: ", obj.Shape.Type
		
		
		
		
vo = box.ViewObject

Now you can also change the properties of the "View" tab:

vo.Transparency = 80
vo.hide()
vo.show()


class Mod_Graphics_Propertys: 
   #def __init__(self, name)
        #self.name = name 
   
   def Activated(self): 
		# Script to Scale Imperial mesh to metric
		FreeCAD.Console.PrintMessage('Random Colour Change Started\n')
		
		sel = FreeCADGui.Selection.getSelection() # " sel " contains the items selected
		#if sel:
		count = 0
		for obj in sel:
			obj = sel[count]
			if self.name = "Random":
			  Colour_ran1 = round(random.random(),2)
			  Colour_ran2 = round(random.random(),2)
			  Colour_ran3 = round(random.random(),2)
			
			  FreeCAD.Console.PrintMessage(obj.Name + "\n")
			
			#Change Object Colour Randomly
			
			  FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor = (Colour_ran1,Colour_ran2,Colour_ran3)
			
			FreeCAD.Console.PrintMessage('Object Processed ' + str(count) + '\n')
			count = count + 1
				
		FreeCAD.Console.PrintMessage('Colours Changed Successfully')
   def GetResources(self): 
       return {'Pixmap' : TOOL_ICON, 'MenuText': 'Short text', 'ToolTip': 'Modifies objects to Random Colour'} 
	  
#FreeCADGui.addCommand('Random_Colour_Object', Mod_Graphics_Propertys("Random"))

FreeCAD.getDocument("Unnamed").addObject("Part::Feature","Cube001")
>>> __shape__=Part.Shape()
>>> __shape__.makeShapeFromMesh(FreeCAD.getDocument("Unnamed").getObject("Cube").Mesh.Topology,0.100000)
>>> FreeCAD.getDocument("Unnamed").getObject("Cube001").Shape=__shape__
>>> FreeCAD.getDocument("Unnamed").getObject("Cube001").purgeTouched()
>>> del __shape__
>>> 
import Part
>>> FreeCAD.getDocument("Unnamed").addObject("Part::Feature","Printer_Bed_Volume001")
>>> __shape__=Part.Shape()
>>> __shape__.makeShapeFromMesh(FreeCAD.getDocument("Unnamed").getObject("Printer_Bed_Volume").Mesh.Topology,0.100000)
>>> FreeCAD.getDocument("Unnamed").getObject("Printer_Bed_Volume001").Shape=__shape__
>>> FreeCAD.getDocument("Unnamed").getObject("Printer_Bed_Volume001").purgeTouched()
>>> del __shape__
#


import Part, FreeCAD, math, PartGui, FreeCADGui
from FreeCAD import Base, Console
sel = FreeCADGui.Selection.getSelection() # " sel " contains the items selected
if len(sel)!=3 :
  # If there are no 3 objects selected, an error is displayed in the report view
  # The \r and \n at the end of line mean return and the newline CR + LF.
  Console.PrintError("Select 3 points exactly\r\n")
else :
  points=[]
  for obj in sel:
    points.append(obj.Shape.BoundBox.Center)

  for pt in points:
    # display of the coordinates in the report view
    Console.PrintMessage(str(pt.x)+"\r\n")
    Console.PrintMessage(str(pt.y)+"\r\n")
    Console.PrintMessage(str(pt.z)+"\r\n")

  Console.PrintMessage(str(pt[1]) + "\r\n")
  
  
  import Draft
numberOfPoints = 3	# minimum 2
selectedEdge = FreeCADGui.Selection.getSelectionEx()[0].SubObjects[0].copy()
points  = selectedEdge.discretize(numberOfPoints)

for i in points:
    Draft.makePoint(i)   # create points
	
	
https://www.freecadweb.org/wiki/Topological_data_scripting