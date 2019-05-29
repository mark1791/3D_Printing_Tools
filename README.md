# FreeCAD 3D Printing Tools
A FreeCAD Workbench for working on imported Meshes.  

# Description
This workbench has a number of features to help working with imported `.stl` models.  
Utilizing the functionality available within the FreeCAD Mesh Design workbench this workbench helps the user to scale and modify meshes.

## Features

* The ability to convert imperial mesh(es) to Metric and vice-versa.  
* Scale a mesh up/down 50%.  
* Scale mesh a set factor.  
* Scale Mesh to fit a 3D printer bed size.  
* Generate an STL box by the size of the printer bed for reference.  
* Convert mesh(es) to solid(s).  
* Make a transparent object.  
* Make an object's transparancy Solid.  
* Show/Hide an object.  
* Change colours of objects to 11 different colours.  
* Change the color of a group of objects to a random colour.  
* Change the line width to 2.0  
* Show the bounding box of an STL mesh.  
* Define the printer bed size.  
* Define the size of the object to be scaled from.  
* Define the Scale factor for the mesh to be scaled, ex. 0.5 = 50% scale; 2.0 = 200% scale.

## Requirements
* FreeCAD v0.X.Y  
* Python3  
* Qt5

## Installation

### Addon Manager
3D Printing Tools workbench has been added to the [FreeCAD-adoons](https://github.com/FreeCAD/FreeCAD-addons) repository and is therefore available to download from the built-in [Addon Manager](https://github.com/FreeCAD/FreeCAD-addons#1-builtin-addon-manager).  
**Note:** Restarting FreeCAD is required to enable the workbench.

### Manual Installation
1. Use `git clone` or download the `.zip` file of this repo directly in to your [FreeCAD `Mod/` directory](https://www.freecadweb.org/wiki/Installing_more_workbenches).  
2. Restart FreeCAD 

## Feedback  
If you have feedback or need to report bugs please participate on the related [3D Printing Tools FreeCAD Forum Post](https://forum.freecadweb.org/viewtopic.php?f=9&t=36564). 

## License
LGPL v2.1