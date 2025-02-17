# Day08 - How To Add Your Custom Link To Your Robot

## Setting up FreeCAD

A modern version of FreeCAD is needed that uses a version of python compatible with the python 3.12 used in ubuntu noble:

* downloaded the latest stable Freecad AppImage in their [releases page](https://github.com/FreeCAD/FreeCAD/releases)  [FreeCAD_1.0.0-conda-Linux-x86_64-py311.AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Linux-x86_64-py311.AppImage) (uses python 3.11) 

* installed it - I used [AppImageLauncher](https://github.com/TheAssassin/AppImageLauncher/releases), an app that takes care of moving the `*.AppImage` to `~/Applications` folder, giving it execution permission, and integrating the App icon in the desktop. Just double-click on the file and click on **Integrate and Run**, this copied the executable to the following path:

```bash
/home/mhered/Applications/FreeCAD_1.0.0-conda-Linux-x86_64-py311_762d03e714090fee85c2cd69af722050.AppImage
```

## Setting up CROSS

Followed instructions in the repo https://github.com/galou/freecad.cross TLDR; install from FreeCAD as AddOn

- In FreeCAD, menu "Edit / Preferences ..."
- Category "Addon Manager"
- Add an entry to "Custom repository" by clicking on the "+" sign.
- Repository URL: `https://github.com/galou/freecad.cross.git`, branch: `main`
- Click on "OK" to close the dialog "Preferences"
- Back to FreeCAD's main window, menu "Tools / Addon manager"
- Search and install the workbench via the [Addon Manager](https://wiki.freecad.org/Std_AddonMgr)

## Launching FreeCAD with CROSS

As explained in the repo instructions, to be able to use ROS-related functionalities of the CROSS workbench FreeCAD must be launched from the command line as follows (otherwise CROSS will have limited functionality):

- Open a terminal
- Source your ROS workspace
- Launch FreeCAD with the extra Python modules set by ROS, `freecad --module-path ${PYTHONPATH//:/' --module-path '}` (replacing `freecad` by your FreeCAD executable). This bash magic will add for example `--module-path path1 --module-path path2` if `$PYTHONPATH` is `path1:path2`.

Implemented in `./run_freecad_baremetal.sh` (edited from the original `.vscode/scripts/run_freecad.bash` to move to workspace folder and point at the right executable:

```bash
#!/bin/bash

source /opt/ros/jazzy/setup.bash
source install/setup.bash

echo "Starting FreeCAD, please wait ..."
export ROS_DISTRO=jazzy
/home/mhered/Applications/FreeCAD_1.0.0-conda-Linux-x86_64-py311_762d03e714090fee85c2cd69af722050.AppImage --appimage-extract-and-run --module-path ${PYTHONPATH//:/' --module-path '} 
```

## Integrating the tray

QUESTION Is this needed in the end? `$ pip3 install py-urdf-reader --break-system-packages` ?? With the old version of FreeCAD the import URDF option in the CROSS bench was grayed out and I got the warning message: `No module named 'urdf_parser_py'` but it seems to work now...

1. Launch FreeCAD with ROS 

2. Open the file `krytn_tray.FCStd`

3. In CROSS workbench Import URDF from `src/bar_examples/krytn/robot_description/krytn.urdf.xacro`

   
