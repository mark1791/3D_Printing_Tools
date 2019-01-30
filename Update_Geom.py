import FreeCAD, FreeCADGui 
import FreeCAD as App

class UpdateGeomCmd: 
   def Activated(self): 
		# Here your write what your ScriptCmd does...
		FreeCAD.Console.PrintMessage('Hello, World!')
		import Mesh,BuildRegularGeoms
		mat=FreeCAD.Matrix()
		mat.scale(25.4,25.4,25.4)
		mesh=App.ActiveDocument.ActiveObject.Mesh.copy()
		#mesh=App.activeDocument()
		mesh.transform(mat)
		Mesh.show(mesh)
		#import Part,PartGui 
		#doc=App.activeDocument() 
		# add a line element to the document and set its points 
		#l=Part.LineSegment()
		#l.StartPoint=(0.0,0.0,0.0)
		#l.EndPoint=(1000.0,1000.0,1000.0)
		#doc.addObject("Part::Feature","Line").Shape=l.toShape() 
		#doc.recompute()
		FreeCAD.Console.PrintMessage('Update got here')
   def GetResources(self): 
       return {'Pixmap' : 'path_to_an_icon/myicon.png', 'MenuText': 'Short text', 'ToolTip': 'More detailed text'} 
       
FreeCADGui.addCommand('Update_Geometry', UpdateGeomCmd())
