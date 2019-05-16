import FreeCAD, FreeCADGui 
import FreeCAD as App
import _SMutils
import random

RAND_ICON = _SMutils.iconsPath() + '/Random.svg'
WHITE_ICON = _SMutils.iconsPath() + '/White.svg'
YELLOW_ICON = _SMutils.iconsPath() + '/Yellow.svg'
ORANGE_ICON = _SMutils.iconsPath() + '/Orange.svg'
RED_ICON = _SMutils.iconsPath() + '/Red.svg'
PURPLE_ICON = _SMutils.iconsPath() + '/Purple.svg'
BLUE_ICON = _SMutils.iconsPath() + '/Blue.svg'
CYAN_ICON = _SMutils.iconsPath() + '/Cyan.svg'
GREEN_ICON = _SMutils.iconsPath() + '/Green.svg'
BROWN_ICON = _SMutils.iconsPath() + '/Brown.svg'
BLACK_ICON = _SMutils.iconsPath() + '/Black.svg'  
PINK_ICON = _SMutils.iconsPath() + '/Pink.svg'
TRANS50_ICON = _SMutils.iconsPath() + '/Trans50.svg'
TRANS100_ICON = _SMutils.iconsPath() + '/Trans100.svg'
HIDE_ICON = _SMutils.iconsPath() + '/Hide.svg'
SHOW_ICON = _SMutils.iconsPath() + '/Show.svg'  
LINE_WIDTH_ICON = _SMutils.iconsPath() + '/Line_Width.svg' 

class Mod_Graphics_Propertys:
	def __init__(self, changevalue):
        	self.changevalue = changevalue
        	#FreeCAD.Console.PrintMessage(self.changevalue)	
		
	def Activated(self): 
		# Script to Scale Imperial mesh to metric
		FreeCAD.Console.PrintMessage('Modify Objects Module Started\n')
		
		sel = FreeCADGui.Selection.getSelection() # " sel " contains the items selected
		
		count = 0
		for obj in sel:
			obj = sel[count]
			#FreeCAD.Console.PrintMessage(self.changevalue + " Does this show\n")
			
			#Check for Random Colour Change
			if self.changevalue == "Rand_Col":
				Colour_ran1 = round(random.random(),2)
				Colour_ran2 = round(random.random(),2)
				Colour_ran3 = round(random.random(),2)
			
				#Change Object Colour Randomly
				FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor = (Colour_ran1,Colour_ran2,Colour_ran3)
				FreeCAD.Console.PrintMessage('Random Colour Change Object Processed ' + str(count) + '\n')
				
		    #Check for Transparency to 50%
			if self.changevalue == "Trans_50":
				FreeCADGui.ActiveDocument.getObject(obj.Name).Transparency = 50
				FreeCAD.Console.PrintMessage('50% Transparency Processed ' + str(count) + '\n')
		    #Check for Transparency to 0%
			if self.changevalue == "Trans_100":
				FreeCADGui.ActiveDocument.getObject(obj.Name).Transparency = 0
				FreeCAD.Console.PrintMessage('0% Transparency Processed ' + str(count) + '\n')
		    #Check for Hide Object
			if self.changevalue == "Hide_object":
				FreeCADGui.ActiveDocument.getObject(obj.Name).hide()
				FreeCAD.Console.PrintMessage('Hide Object Processed ' + str(count) + '\n')
		    #Check for Show Object
			if self.changevalue == "Show_object":
				FreeCADGui.ActiveDocument.getObject(obj.Name).show()
				FreeCAD.Console.PrintMessage('Show Object Processed ' + str(count) + '\n')
		    #Check for White Colour
			if self.changevalue == "White_Col":
				FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor = (1.0,1.0,1.0)
				FreeCAD.Console.PrintMessage('White Object Processed ' + str(count) + '\n')
		    #Check for Yellow Colour
			if self.changevalue == "Yellow_Col":
				FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor = (1.0,1.0,0.0)
				FreeCAD.Console.PrintMessage('Yellow Object Processed ' + str(count) + '\n')
		    #Check for Orange Colour
			if self.changevalue == "Orange_Col":
				FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor = (1.0,0.53,0.06)
				FreeCAD.Console.PrintMessage('Orange Object Processed ' + str(count) + '\n')
		    #Check for Red Colour
			if self.changevalue == "Red_Col":
				FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor = (1.0,0.0,0.0)
				FreeCAD.Console.PrintMessage('Red Object Processed ' + str(count) + '\n')
		    #Check for Pink Colour
			if self.changevalue == "Pink_Col":
				FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor = (1.0,0.0,0.5)
				FreeCAD.Console.PrintMessage('Pink Object Processed ' + str(count) + '\n')
		    #Check for White Colour
			if self.changevalue == "Purple_Col":
				FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor = (0.67,0.0,1.0)
				FreeCAD.Console.PrintMessage('Purple Object Processed ' + str(count) + '\n')
		    #Check for Yellow Colour
			if self.changevalue == "Blue_Col":
				FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor = (0.0,0.0,1.0)
				FreeCAD.Console.PrintMessage('Blue Object Processed ' + str(count) + '\n')
		    #Check for Orange Colour
			if self.changevalue == "Cyan_Col":
				FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor = (0.0,1.0,1.0)
				FreeCAD.Console.PrintMessage('Cyan Object Processed ' + str(count) + '\n')
		    #Check for Red Colour
			if self.changevalue == "Green_Col":
				FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor = (0.33,1.0,0.0)
				FreeCAD.Console.PrintMessage('Green Object Processed ' + str(count) + '\n')
		    #Check for Pink Colour
			if self.changevalue == "Brown_Col":
				FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor = (0.67,0.33,0.0)
				FreeCAD.Console.PrintMessage('Brown Object Processed ' + str(count) + '\n')
		    #Check for Pink Colour
			if self.changevalue == "Black_Col":
				FreeCADGui.ActiveDocument.getObject(obj.Name).ShapeColor = (0.0,0.0,0.0)
				FreeCAD.Console.PrintMessage('Black Object Processed ' + str(count) + '\n')
		    #Check for Line Width Change to change to 2.0
			if self.changevalue == "Line_Width_Change":
				FreeCADGui.ActiveDocument.getObject(obj.Name).LineWidth = 2.00
				FreeCAD.Console.PrintMessage('Black Object Processed ' + str(count) + '\n')
			 
			#Index Object Count in Loop
			count = count + 1
				
		FreeCAD.Console.PrintMessage('Objects Changed Successfully')
	def GetResources(self): 
		if self.changevalue == "Rand_Col":
			TOOL_ICON = RAND_ICON
			TOOLTIP_VAL = 'Modifies objects to Random Colour'
		if self.changevalue == "Trans_50":
			TOOL_ICON = TRANS50_ICON
			TOOLTIP_VAL = 'Changes objects 50% Transparency'	   
		if self.changevalue == "Trans_100":
			TOOL_ICON = TRANS100_ICON
			TOOLTIP_VAL = 'Changes objects 0% Transparency'	   
		if self.changevalue == "Hide_object":
			TOOL_ICON = HIDE_ICON
			TOOLTIP_VAL = 'Hides Selected Objects'	   
		if self.changevalue == "Show_object":
			TOOL_ICON = SHOW_ICON
			TOOLTIP_VAL = 'Unhides Selected Objects'	   
		if self.changevalue == "White_Col":
			TOOL_ICON = WHITE_ICON
			TOOLTIP_VAL = 'Changes objects to White Colour'		   
		if self.changevalue == "Yellow_Col":
			TOOL_ICON = YELLOW_ICON
			TOOLTIP_VAL = 'Changes objects to Yellow Colour'		   
		if self.changevalue == "Orange_Col":
			TOOL_ICON = ORANGE_ICON
			TOOLTIP_VAL = 'Changes objects to Orange Colour'		   
		if self.changevalue == "Red_Col":
			TOOL_ICON = RED_ICON
			TOOLTIP_VAL = 'Changes objects to Red Colour'		   
		if self.changevalue == "Pink_Col":
			TOOL_ICON = PINK_ICON
			TOOLTIP_VAL = 'Changes objects to Pink Colour'   
		if self.changevalue == "Purple_Col":
			TOOL_ICON = PURPLE_ICON
			TOOLTIP_VAL = 'Changes objects to Purple Colour'	   
		if self.changevalue == "Blue_Col":
			TOOL_ICON = BLUE_ICON
			TOOLTIP_VAL = 'Changes objects to Blue Colour'		   
		if self.changevalue == "Cyan_Col":
			TOOL_ICON = CYAN_ICON
			TOOLTIP_VAL = 'Changes objects to Cyan Colour'		   
		if self.changevalue == "Green_Col":
			TOOL_ICON = GREEN_ICON
			TOOLTIP_VAL = 'Changes objects to Green Colour'		   
		if self.changevalue == "Brown_Col":
			TOOL_ICON = BROWN_ICON
			TOOLTIP_VAL = 'Changes objects to Brown Colour'		   
		if self.changevalue == "Black_Col":
			TOOL_ICON = BLACK_ICON
			TOOLTIP_VAL = 'Changes objects to Black Colour'		   
		if self.changevalue == "Line_Width_Change":
			TOOL_ICON = LINE_WIDTH_ICON
			TOOLTIP_VAL = 'Changes Line Width to 2.0'		  		   
		   
		return {'Pixmap' : TOOL_ICON, 'MenuText': 'Short text', 'ToolTip': TOOLTIP_VAL} 
		

FreeCADGui.addCommand('Random_Colour_Object', Mod_Graphics_Propertys("Rand_Col"))
FreeCADGui.addCommand('Transparency50_Object', Mod_Graphics_Propertys("Trans_50"))
FreeCADGui.addCommand('Transparency100_Object', Mod_Graphics_Propertys("Trans_100"))
FreeCADGui.addCommand('Hide_Object', Mod_Graphics_Propertys("Hide_object"))
FreeCADGui.addCommand('Show_Object', Mod_Graphics_Propertys("Show_object"))
FreeCADGui.addCommand('White_Colour_Object', Mod_Graphics_Propertys("White_Col"))
FreeCADGui.addCommand('Yellow_Colour_Object', Mod_Graphics_Propertys("Yellow_Col"))
FreeCADGui.addCommand('Orange_Colour_Object', Mod_Graphics_Propertys("Orange_Col"))
FreeCADGui.addCommand('Red_Colour_Object', Mod_Graphics_Propertys("Red_Col"))
FreeCADGui.addCommand('Pink_Colour_Object', Mod_Graphics_Propertys("Pink_Col"))
FreeCADGui.addCommand('Purple_Colour_Object', Mod_Graphics_Propertys("Purple_Col"))
FreeCADGui.addCommand('Blue_Colour_Object', Mod_Graphics_Propertys("Blue_Col"))
FreeCADGui.addCommand('Cyan_Colour_Object', Mod_Graphics_Propertys("Cyan_Col"))
FreeCADGui.addCommand('Green_Colour_Object', Mod_Graphics_Propertys("Green_Col"))
FreeCADGui.addCommand('Brown_Colour_Object', Mod_Graphics_Propertys("Brown_Col"))
FreeCADGui.addCommand('Black_Colour_Object', Mod_Graphics_Propertys("Black_Col"))
FreeCADGui.addCommand('Line_Width_Change_Object', Mod_Graphics_Propertys("Line_Width_Change"))
