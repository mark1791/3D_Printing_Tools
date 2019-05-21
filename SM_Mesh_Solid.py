import FreeCAD, FreeCADGui 
import FreeCAD as App
import _SMutils
import random
import Part
from datetime import datetime
from FreeCAD import Base

TOOL_ICON = _SMutils.iconsPath() + '/Mesh_to_Solid.svg'

class Solid_Mesh_Refined_Cmd: 
	def __init__(self, changevalue):
        	self.changevalue = changevalue
        	#FreeCAD.Console.PrintMessage(self.changevalue)
		
	def Activated(self): 
		# Script to convert a mesh to a solid
		FreeCAD.Console.PrintMessage('Module to Convert to a refined Solid Started\n')
		FreeCAD.Console.PrintMessage(datetime.now().strftime('%H:%M:%S') + '\n')
		Start_time = datetime.now()
		#changeval = str(self.changevalue)
		sel = FreeCADGui.Selection.getSelection() # " sel " contains the items selected
		
		#Setup the Progress bar
		progress_bar = Base.ProgressIndicator()
		count = 0
		for obj in sel:
			count = count + 1
			
		progress_bar.start("Converting " + str(count) + " Meshes to Refined Solids...",(count * 2)) #Calculate how many objects multiply by key steps of which 2
		
		count = 0
		
		for obj in sel:
			obj = sel[count]
			
			changeval = str(self.changevalue)
			
			if self.changevalue == "Solid_Mesh_Refined":
				#set doc to active document
				doc=App.activeDocument()
				FreeCAD.Console.PrintMessage(obj.Name + " Started Conversion to Solid\n")
				new_name = obj.Name+"_Solid_"+str(random.randrange(10**4, 10**5))
				box = doc.addObject("Part::Feature",new_name) 
				#Step 1 Create Part Shape
				box = Part.Shape()
				#Step 2 Convert Mesh to temporary part shape
				box.makeShapeFromMesh(FreeCAD.ActiveDocument.getObject(obj.Name).Mesh.Topology,0.100000) # Step 3
				#Step 3 move temporary shape to new object
				FreeCAD.ActiveDocument.getObject(new_name).Shape=box
				#Step 4 Purge the new solid
				FreeCAD.ActiveDocument.getObject(new_name).purgeTouched()
				progress_bar.next()
				#Step 5 Delete the temporary object
				del box
				FreeCAD.Console.PrintMessage(obj.Name + " Completed Conversion to Solid\n")
				#Step 6 refine mesh -  App.ActiveDocument.addObject('Part::Feature','Mesh_Solid').Shape=App.ActiveDocument.Mesh_Solid.Shape.removeSplitter() refine mesh
				FreeCAD.Console.PrintMessage(obj.Name + " Started Refinement of Solid\n")
				doc.addObject('Part::Feature',"Refined_"+new_name).Shape=doc.getObject(new_name).Shape.removeSplitter()
				#Step 7 Remove intermediate Solid
				doc.removeObject(new_name)
				FreeCAD.ActiveDocument.recompute()
				#Step 8 Recompute document
				FreeCAD.Console.PrintMessage(obj.Name + " Completed Refinement of Solid\n")
				progress_bar.next()
			
				FreeCAD.Console.PrintMessage('Object Processed ' + str(count) + '\n')
			count = count + 1
				
		Time_Taken = (datetime.now() - Start_time)
		progress_bar.stop
		Time_seconds = Time_Taken.total_seconds()
		FreeCAD.Console.PrintMessage("Module to convert from Mesh to Refined Solid Completed Successfully in " + str(Time_seconds) + "Seconds\n")

	def GetResources(self): 
		return {'Pixmap' : TOOL_ICON, 'MenuText': 'Short text', 'ToolTip': 'Module to convert Mesh to Refined Solids'} 
       

       
FreeCADGui.addCommand('Solid_Mesh_Refined_Cmd_Geometry', Solid_Mesh_Refined_Cmd("Solid_Mesh_Refined"))
