import FreeCAD, FreeCADGui 
import FreeCAD as App
import _SMutils

TOOL_ICON = _SMutils.iconsPath() + '/Cube.svg'

class BoxMeshCmd: 
	def Activated(self): 
		# Here your write what your ScriptCmd does...
		FreeCAD.Console.PrintMessage('CreatBox\n')
		import Mesh,BuildRegularGeoms
		doc=App.activeDocument()
		# create a new empty mesh
		m = Mesh.Mesh()
		# build up box out of 12 facets
		m.addFacet(0.0,0.0,0.0, 0.0,0.0,150.0, 0.0,150.0,150.0)
		m.addFacet(0.0,0.0,0.0, 0.0,150.0,150.0, 0.0,150.0,0.0)
		m.addFacet(0.0,0.0,0.0, 150.0,0.0,0.0, 150.0,0.0,150.0)
		m.addFacet(0.0,0.0,0.0, 150.0,0.0,150.0, 0.0,0.0,150.0)
		m.addFacet(0.0,0.0,0.0, 0.0,150.0,0.0, 150.0,150.0,0.0)
		m.addFacet(0.0,0.0,0.0, 150.0,150.0,0.0, 150.0,0.0,0.0)
		m.addFacet(0.0,150.0,0.0, 0.0,150.0,150.0, 150.0,150.0,150.0)
		m.addFacet(0.0,150.0,0.0, 150.0,150.0,150.0, 150.0,150.0,0.0)
		m.addFacet(0.0,150.0,150.0, 0.0,0.0,150.0, 150.0,0.0,150.0)
		m.addFacet(0.0,150.0,150.0, 150.0,0.0,150.0, 150.0,150.0,150.0)
		m.addFacet(150.0,150.0,0.0, 150.0,150.0,150.0, 150.0,0.0,150.0)
		m.addFacet(150.0,150.0,0.0, 150.0,0.0,150.0, 150.0,0.0,0.0)
		# Create a Mesh Box 150mm x 150mm x 150mm to simulate Printer Bed extents
		me=doc.addObject("Mesh::Feature","Printer Bed Volume")
		me.Mesh=m
		FreeCAD.Console.PrintMessage('Mesh Box Created Successfully\n')
	def GetResources(self): 
		return {'Pixmap' : TOOL_ICON, 'MenuText': 'Short text', 'ToolTip': 'Creates 150mm x 150mm Mesh Cube'} 
       
FreeCADGui.addCommand('BoxMesh_Geometry', BoxMeshCmd())
