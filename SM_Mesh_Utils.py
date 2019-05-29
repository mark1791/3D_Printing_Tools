import FreeCAD, FreeCADGui, math
import FreeCAD as App
import Mesh,BuildRegularGeoms
from PySide import QtGui, QtCore
import _SMutils

DESCALE_ICON = _SMutils.iconsPath() + '/Descale.svg'
DESCALEPRINTER_ICON = _SMutils.iconsPath() + '/DescalePrinter.svg'
INCH_MM_ICON = _SMutils.iconsPath() + '/Inch_mm.svg'
MM_INCH_ICON = _SMutils.iconsPath() + '/mm_inch.svg'
SCALE50_ICON = _SMutils.iconsPath() + '/Scale50.svg'
SCALE_BY_FACTOR = _SMutils.iconsPath() + '/Scalebyfactor.svg'
BEDLENGTH_ICON = _SMutils.iconsPath() + '/Bedlength.svg'
DIELENGTH_ICON = _SMutils.iconsPath() + '/Dielength.svg'
SCALE_FACTOR_ICON = _SMutils.iconsPath() + '/Scalefactor.svg'
SCALE_BY_FACTOR_ICON = _SMutils.iconsPath() + '/Scalebyfactor.svg'
CUBE_ICON = _SMutils.iconsPath() + '/Cube.svg'
BOUNDING_ICON = _SMutils.iconsPath() + '/BoundingBox.svg'


class MeshXScaleGeomCmd:
	def __init__(self, changevalue):
			self.changevalue = changevalue
			global scale_factor
			global bedlength
			global Die_Length
			global BoundingBoxShow
			bedlength = 205.00#Set to Anycubic bed size
			Die_Length = 2400.00
			scale_factor = 0.5
			BoundingBoxShow = True
			#mat_scale_on = False
        	#FreeCAD.Console.PrintMessage(self.changevalue)	
		
	def Activated(self): 
		# Resduce Mesh Manipulation Module
		FreeCAD.Console.PrintMessage('Mesh Manipulation Utlity Module Started\n')
		import Mesh,BuildRegularGeoms
		
		#Setup for global variables change the Printer Bed size
		if self.changevalue == "Bed_Length_Size":
			global bedlength
			bedlength = global_variable_func(bedlength, "Printer Bed Length", "Enter Size of Printer Bed Size(", True)
			FreeCAD.Console.PrintMessage("Printer Bed Length change to " + str(bedlength))
			mat_scale_on = False
			
		#Change Bed size Global Value
		if self.changevalue == "Die_Length_Size":
			global Die_Length
			Die_Length = global_variable_func(Die_Length, "Die Size", "Enter Size of Die to scale down(", True)
			FreeCAD.Console.PrintMessage("Die size changed to " + str(Die_Length))
			mat_scale_on = False
		
		#Change Variable Scale Value
		if self.changevalue == "Global_Scale_Value":
			global scale_factor
			scale_factor = global_variable_func(scale_factor, "Scale Factor", "Enter Scale Factor of Die to scale(", True)
			FreeCAD.Console.PrintMessage("Die size changed to " + str(scale_factor))
			mat_scale_on = False
			
		sel = FreeCADGui.Selection.getSelection() # " sel " contains the items selected
		#App.Console.PrintMessage(str(sel)+"Current Selected named part")
		mat=FreeCAD.Matrix()
		
		#Check for 50% Shrink Scale Mesh%
		if self.changevalue == "Descale_Com":
			FreeCAD.Console.PrintMessage('Shrink  Selected Objects Mesh by 50%\n')
			mat.scale(0.5,0.5,0.5)
			mat_scale_on = True
			
		#Check for 50% Shrink Scale Mesh%
		if self.changevalue == "Scale_by_factor":
			FreeCAD.Console.PrintMessage('Scale geometry by variable scale factor\n')
			mat.scale(scale_factor,scale_factor,scale_factor)
			mat_scale_on = True
			
		#Reduces Mesh by 95% to fit 150mm Printer Bed
		if self.changevalue == "Printer_Com":
			#global scale_factor
			De_Scale_Factor = 0.00
			#bedlength = 150.00
			#Die_Length = 2400.00
			De_Scale_Factor = bedlength/Die_Length
			mat.scale(De_Scale_Factor,De_Scale_Factor,De_Scale_Factor)
			scale_factor = De_Scale_Factor
			FreeCAD.Console.PrintMessage('Reduces  Selected Objects Mesh by 95% to fit 150mm Printer Bed\n')
			mat_scale_on = True
		#Converts Imperial Mesh to Metric
		if self.changevalue == "Scale_Imperial_Com":
			FreeCAD.Console.PrintMessage('Converts  Selected Objects Imperial Mesh to Metric\n')
			mat.scale(25.4,25.4,25.4)
			mat_scale_on = True
		#Converts Metric Mesh to Imperial
		if self.changevalue == "Scale_Metric_Com":
			FreeCAD.Console.PrintMessage('Converts Selected Objects Metric Mesh to Imperial\n')
			mat.scale(0.03937,0.03937,0.03937)
			mat_scale_on = True
		#Scale Mesh by 50%
		if self.changevalue == "Scale50_Com":
			FreeCAD.Console.PrintMessage('Scale Selected Objects Mesh by 50%\n')
			mat.scale(2,2,2)
			mat_scale_on = True
		#Create Printer Cube Box
		if self.changevalue == "Printer_Box":
			FreeCAD.Console.PrintMessage('CreatBox\n')
			doc=App.activeDocument()
			# create a new empty mesh
			m = Mesh.Mesh()
			# build up box out of 12 facets
			m.addFacet(0.0,0.0,0.0, 0.0,0.0,bedlength, 0.0,bedlength,bedlength)
			m.addFacet(0.0,0.0,0.0, 0.0,bedlength,bedlength, 0.0,bedlength,0.0)
			m.addFacet(0.0,0.0,0.0, bedlength,0.0,0.0, bedlength,0.0,bedlength)
			m.addFacet(0.0,0.0,0.0, bedlength,0.0,bedlength, 0.0,0.0,bedlength)
			m.addFacet(0.0,0.0,0.0, 0.0,bedlength,0.0, bedlength,bedlength,0.0)
			m.addFacet(0.0,0.0,0.0, bedlength,bedlength,0.0, bedlength,0.0,0.0)
			m.addFacet(0.0,bedlength,0.0, 0.0,bedlength,bedlength, bedlength,bedlength,bedlength)
			m.addFacet(0.0,bedlength,0.0, bedlength,bedlength,bedlength, bedlength,bedlength,0.0)
			m.addFacet(0.0,bedlength,bedlength, 0.0,0.0,bedlength, bedlength,0.0,bedlength)
			m.addFacet(0.0,bedlength,bedlength, bedlength,0.0,bedlength, bedlength,bedlength,bedlength)
			m.addFacet(bedlength,bedlength,0.0, bedlength,bedlength,bedlength, bedlength,0.0,bedlength)
			m.addFacet(bedlength,bedlength,0.0, bedlength,0.0,bedlength, bedlength,0.0,0.0)
			# Create a Mesh Box 150mm x 150mm x 150mm to simulate Printer Bed extents
			me=doc.addObject("Mesh::Feature","Printer Bed Volume")
			me.Mesh=m
			FreeCAD.Console.PrintMessage('Mesh Box Created Successfully\n')
			mat_scale_on = False
		
		#Trun on Bounding Box
		if self.changevalue == "Bounding_Box_Show":
			mat_scale_on = True
			
		#Use selected objects for Scaling Metric to Imperial
		sel = FreeCADGui.Selection.getSelection() # " sel " contains the items selected
		#if sel:
		count = 0
		if mat_scale_on == True:
			for obj in sel:
				obj = sel[count]
				if self.changevalue == "Bounding_Box_Show":
					global BoundingBoxShow
					if BoundingBoxShow == True:
						FreeCADGui.ActiveDocument.getObject(obj.Label).BoundingBox = BoundingBoxShow
						BoundingBoxShow = False
					else:
						FreeCADGui.ActiveDocument.getObject(obj.Label).BoundingBox = BoundingBoxShow
						BoundingBoxShow = True
					
				else:
					mesh = obj.Mesh.copy()
					mesh.transform(mat)
					Mesh.show(mesh)
					FreeCAD.Console.PrintMessage('Object Processed ' + str(count) + '\n')
				count = count + 1
		FreeCAD.Console.PrintMessage('Mesh Manipulation Utlity Module Completed')
		
	def GetResources(self):  
		if self.changevalue == "Descale_Com":
			TOOL_ICON = DESCALE_ICON
			TOOLTIP_VAL = 'Reduces Mesh by 50%'
		if self.changevalue == "Printer_Com":
			TOOL_ICON = DESCALEPRINTER_ICON
			TOOLTIP_VAL = 'Reduces Mesh by 95% to fit 150mm Printer Bed'	   
		if self.changevalue == "Scale_Imperial_Com":
			TOOL_ICON = INCH_MM_ICON
			TOOLTIP_VAL = 'Converts Imperial Mesh to Metric'	   
		if self.changevalue == "Scale_Metric_Com":
			TOOL_ICON = MM_INCH_ICON
			TOOLTIP_VAL = 'Converts Metric Mesh to Imperial'	   
		if self.changevalue == "Scale50_Com":
			TOOL_ICON = SCALE50_ICON
			TOOLTIP_VAL = 'Scale Mesh by 50%'	   
		if self.changevalue == "Bed_Length_Size":
			TOOL_ICON = BEDLENGTH_ICON
			TOOLTIP_VAL = 'Change default Bed Length Size'	   
		if self.changevalue == "Die_Length_Size":
			TOOL_ICON = DIELENGTH_ICON
			TOOLTIP_VAL = 'Change default Die Length Size'	   
		if self.changevalue == "Global_Scale_Value":
			TOOL_ICON = SCALE_FACTOR_ICON
			TOOLTIP_VAL = 'Change default Variable scale factor'   
		if self.changevalue == "Printer_Box":
			TOOL_ICON = CUBE_ICON
			TOOLTIP_VAL = 'Create mesh box size of Printer'   
		if self.changevalue == "Scale_by_factor":
			TOOL_ICON = SCALE_BY_FACTOR_ICON
			TOOLTIP_VAL = 'Scale Geometry by variable scale factor'  
		if self.changevalue == "Bounding_Box_Show":
			TOOL_ICON = BOUNDING_ICON
			TOOLTIP_VAL = 'Turn on and off the Bounding box size'				
		return {'Pixmap' : TOOL_ICON, 'MenuText': 'Short text', 'ToolTip': TOOLTIP_VAL} 
       
FreeCADGui.addCommand('Descale_Geometry', MeshXScaleGeomCmd("Descale_Com"))
FreeCADGui.addCommand('ReScale_Fit_Printer_Geometry', MeshXScaleGeomCmd("Printer_Com"))
FreeCADGui.addCommand('Scale_Imperial_mm', MeshXScaleGeomCmd("Scale_Imperial_Com"))
FreeCADGui.addCommand('Scale_mm_imperial', MeshXScaleGeomCmd("Scale_Metric_Com"))
FreeCADGui.addCommand('Scale50_Geometry', MeshXScaleGeomCmd("Scale50_Com"))
FreeCADGui.addCommand('Bed_length_S', MeshXScaleGeomCmd("Bed_Length_Size"))
FreeCADGui.addCommand('Die_Length_S', MeshXScaleGeomCmd("Die_Length_Size"))
FreeCADGui.addCommand('Scale_Factor_S', MeshXScaleGeomCmd("Global_Scale_Value"))
FreeCADGui.addCommand('BoxMesh_Geometry', MeshXScaleGeomCmd("Printer_Box"))
FreeCADGui.addCommand('Scale_Factor_Geom', MeshXScaleGeomCmd("Scale_by_factor"))
FreeCADGui.addCommand('Bounding_Box_Geom', MeshXScaleGeomCmd("Bounding_Box_Show"))

def global_variable_func(variable_value, box_name, message_name, variable_type):

	reply = QtGui.QInputDialog.getText(None, box_name,message_name + str(variable_value) + ") value currently:")
	if reply[1]:
		# user clicked OKi
		if not reply[0]:
			variable_value = variable_value
		else:
			if variable_type == True:
				variable_value = float(reply[0])
			else:
				variable_value = str(reply[0])
			#FreeCAD.Console.PrintMessage(reply[0])
	else:
		# user clicked Cancel
		variable_value = variable_value # which will be "" if they clicked Cancel
	#FreeCAD.Console.PrintMessage("Line/Point Length Distance changed to " + str(reply[0]))
	return variable_value

	
	#FreeCADGui.getDocument("Unnamed").getObject("out").BoundingBox = True