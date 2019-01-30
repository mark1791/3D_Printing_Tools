import FreeCAD, FreeCADGui, math
import FreeCAD as App
import _SMutils

DESCALE_ICON = _SMutils.iconsPath() + '\Descale.svg'
DESCALEPRINTER_ICON = _SMutils.iconsPath() + '\DescalePrinter.svg'
INCH_MM_ICON = _SMutils.iconsPath() + '\Inch_mm.svg'
MM_INCH_ICON = _SMutils.iconsPath() + '\mm_inch.svg'
SCALE50_ICON = _SMutils.iconsPath() + '\Scale50.svg'


class MeshXScaleGeomCmd:
   def __init__(self, changevalue):
        self.changevalue = changevalue
        #FreeCAD.Console.PrintMessage(self.changevalue)	
		
   def Activated(self): 
		# Resduce Mesh Manipulation Module
		FreeCAD.Console.PrintMessage('Mesh Manipulation Utlity Module Started\n')
		import Mesh,BuildRegularGeoms
		sel = FreeCADGui.Selection.getSelection() # " sel " contains the items selected
		#App.Console.PrintMessage(str(sel)+"Current Selected named part")
		mat=FreeCAD.Matrix()
		
		#Check for 50% Shrink Scale Mesh%
		if self.changevalue == "Descale_Com":
			FreeCAD.Console.PrintMessage('Shrink  Selected Objects Mesh by 50%\n')
			mat.scale(0.5,0.5,0.5)
			
		#Reduces Mesh by 95% to fit 150mm Printer Bed
		if self.changevalue == "Printer_Com":
			De_Scale_Factor = 0.00
			bedlength = 150.00
			Die_Length = 2400.00
			De_Scale_Factor = bedlength/Die_Length
			mat.scale(De_Scale_Factor,De_Scale_Factor,De_Scale_Factor)
			FreeCAD.Console.PrintMessage('Reduces  Selected Objects Mesh by 95% to fit 150mm Printer Bed\n')
		#Converts Imperial Mesh to Metric
		if self.changevalue == "Scale_Imperial_Com":
			FreeCAD.Console.PrintMessage('Converts  Selected Objects Imperial Mesh to Metric\n')
			mat.scale(25.4,25.4,25.4)
		#Converts Metric Mesh to Imperial
		if self.changevalue == "Scale_Metric_Com":
			FreeCAD.Console.PrintMessage('Converts Selected Objects Metric Mesh to Imperial\n')
			mat.scale(0.03937,0.03937,0.03937)
		#Scale Mesh by 50%
		if self.changevalue == "Scale50_Com":
			FreeCAD.Console.PrintMessage('Scale Selected Objects Mesh by 50%\n')
			mat.scale(2,2,2)
			
		#Use selected objects for Scaling Metric to Imperial
		sel = FreeCADGui.Selection.getSelection() # " sel " contains the items selected
		#if sel:
		count = 0
		for obj in sel:
			obj = sel[count]
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
       return {'Pixmap' : TOOL_ICON, 'MenuText': 'Short text', 'ToolTip': TOOLTIP_VAL} 
       
FreeCADGui.addCommand('Descale_Geometry', MeshXScaleGeomCmd("Descale_Com"))
FreeCADGui.addCommand('ReScale_Fit_Printer_Geometry', MeshXScaleGeomCmd("Printer_Com"))
FreeCADGui.addCommand('Scale_Imperial_mm', MeshXScaleGeomCmd("Scale_Imperial_Com"))
FreeCADGui.addCommand('Scale_mm_imperial', MeshXScaleGeomCmd("Scale_Metric_Com"))
FreeCADGui.addCommand('Scale50_Geometry', MeshXScaleGeomCmd("Scale50_Com"))
