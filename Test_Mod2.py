import FreeCAD, FreeCADGui, Draft, Part
#from FreeCAD import Base, Console
import FreeCAD as App
import Mesh,BuildRegularGeoms

FreeCAD.Console.PrintMessage('Command Entered')
class VisCmd: 
	def Activated(self):
		FreeCAD.Console.PrintMessage('Proc Entered')
		length = 0.0
		for o in FreeCADGui.Selection.getSelectionEx():
			for s in o.SubObjects:
				length += s.Length
				#s.copy()
				FreeCAD.Console.PrintMessage(str(length))
		FreeCAD.Console.PrintMessage('Proc Exit')
	def GetResources(self): 
		return {'Pixmap' : 'path_to_an_icon/myicon.png', 'MenuText': 'Short text', 'ToolTip': 'Reduces Mesh by 95%'} 
       
FreeCADGui.addCommand('Vis_Geometry', VisCmd())
