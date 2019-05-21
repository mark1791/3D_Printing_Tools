import FreeCAD, FreeCADGui 
import FreeCAD as App
import _SMutils
import random
import Part

TOOL_ICON = _SMutils.iconsPath() + '\Test.svg'

class TestCmd: 
   def __init__(self, changevalue):
        #changeval = ""
        self.changevalue = changevalue
        #FreeCAD.Console.PrintMessage(self.changevalue)
		
   def Activated(self): 
		# Script to Scale Imperial mesh to metric
		FreeCAD.Console.PrintMessage('Random Colour Change Started\n')
		#changeval = str(self.changevalue)
		sel = FreeCADGui.Selection.getSelection() # " sel " contains the items selected
		
		count = 0
		for obj in sel:
			obj = sel[count]
			#FreeCAD.Console.PrintMessage(self.changevalue + " Does this show\n")
			changeval = str(self.changevalue)
			#FreeCAD.Console.PrintMessage(changeval + " XXXX\n")
			if self.changevalue == "Rand_Col":
			   #set doc to active document
			   doc=App.activeDocument()
			   
			   new_name = obj.Name+"_Solid_"+str(random.randrange(10**4, 10**5))
			   box = doc.addObject("Part::Box",new_name) # Step 1
			   #FreeCAD.Console.PrintMessage(obj.Name + "\n")
			   #Step 1 Create Part Shape
			   box = Part.Shape()
			   #Step 2 Convert Mesh to temporary part shape
			   box.makeShapeFromMesh(FreeCAD.ActiveDocument.getObject(obj.Name).Mesh.Topology,0.100000) # Step 3
			   #Step 3 move temporary shape to new object
			   #FreeCAD.getDocument("Unnamed").getObject(new_name).Shape=box
			   FreeCAD.ActiveDocument.getObject(new_name).Shape=box
			   #Step 4 Purge the new solid
			   #FreeCAD.getDocument("Unnamed").getObject(new_name).purgeTouched()
			   FreeCAD.ActiveDocument.getObject(new_name).purgeTouched()
			   #Step 5 Delete the temporary object
			   del box
			   #Step 6 refine mesh -  App.ActiveDocument.addObject('Part::Feature','Mesh_Solid').Shape=App.ActiveDocument.Mesh_Solid.Shape.removeSplitter() refine mesh4
			   #App.ActiveDocument.addObject('Part::Feature','Mesh_Solid').Shape=App.ActiveDocument.getObject(new_name).Shape.removeSplitter() #refine mesh
			   doc.addObject('Part::Feature',"Refined_"+new_name).Shape=doc.getObject(new_name).Shape.removeSplitter()
			   #FreeCAD.ActiveDocument.getObject(new_name).hide()
			   FreeCAD.ActiveDocument.recompute()
			   FreeCAD.Console.PrintMessage(self.changevalue + " Does this show\n")
			   FreeCAD.Console.PrintMessage(obj.Name + "\n")
			
			   #Change Object Colour Randomly
			
			   #FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor = (Colour_ran1,Colour_ran2,Colour_ran3)
			
			   FreeCAD.Console.PrintMessage('Object Processed ' + str(count) + '\n')
			count = count + 1
				
		FreeCAD.Console.PrintMessage('Colours Changed Successfully')

   def GetResources(self): 
       return {'Pixmap' : TOOL_ICON, 'MenuText': 'Short text', 'ToolTip': 'Test Icon Module to test new code before implementation into master code base'} 
       

       
FreeCADGui.addCommand('Test_Geometry', TestCmd("Rand_Col"))
