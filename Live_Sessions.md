# Live Sessions

## 7/2/2025 - Live Session #1 (kick off meeting)

Works for Nexus

Krytn & MACI Coffee robot

Read "Atomic Habits" James Clear - sprint to change self perception

"show your work" - a record, as a way to appreciate what we learn and get noticed

tag john vial

roughly 1 hour per day then write and share what I learnt for 28 consecutive days

Days 0-9 - Krytn Coffee Robot - standard ROS navigation stack then extend it using FreeCAD (add a tray)

10-19 MACI robot arm - adding collision avoidance. Controlling a robot arm is complicated. Extend it with our own gripper then pick up a can from a tray

20-28 build your own robot - find something relevant to you and simulate it! Will provide templates.

Additional Bonus videos to extend: real robots, frameworks and templates, AI...

Join Discord!

7 daily tasks each week (do the task and post about it)

Play with github copilot can help get unstuck

Copilot

Pearce - Engineering degree. Did robotics without ROS (was extracurricular). Doing PM in navy

11 pax in the cohort

## 14/2/2025 - Live Session #2

we are on Day 7 (I am on Day 6 so not bad)

Days 10-19 we'll work with MACI arm, design a custom gripper and configure it with ros2_control

simulate picking a coke can

Next Live session Sat 22/2 3pm Perth

Other colleagues: Vangelis Mathe??, Pedro Aguilera

Problems you can solve with a wheeled robot? Restaurant, Mowing, Vacuum, Swimming pools, Warehouse Logistics, in mapping in construction: drawing walls on a construction site based on plans

Advice: Thread is not so good for discoverability in twitter

### Tasks

Take a look at `.vscode/scripts`

`tasks.json` defines tasks, e.g.

```bash
        ...
        {
            "label": "freecad",
            "detail": "start freecad",
            "type": "shell",
            "command": "bash .vscode/scripts/run_freecad.sh",
            "problemMatcher": []
        },
        ...
```

Then `run_freecad.sh`:

```bash
#!/bin/bash

source /opt/ros/jazzy/setup.bash
source install/setup.bash

echo "Starting FreeCAD, please wait ..."
export ROS_DISTRO=jazzy
/home/ubuntu/FreeCAD.AppImage --appimage-extract-and-run --module-path ${PYTHONPATH//:/' --module-path '} 
```

### fix for Teleop Task

```
from launch.actions import TimerAction
...
robot = TimerAction(
	period=10.0,
    actions=[
    	Node(
        		package='ros_gz_sim', 					executable="create",     				arguments=[                    				"-topic", 							"/robot_description",                     "-z", "0.5",                				],                					name="spawn_robot",                		output="both"
        	)
        ]
	)
```

### FreeCAD

need to download the Freecad weekly build because the one in snap uses python 3.10 which does not work well with the python 3.12 used in ubuntu noble

the Freecad weekly uses 3.11

https://github.com/FreeCAD/FreeCAD-Bundle/releases/tag/weekly-builds:

* [FreeCAD_weekly-builds-40176-conda-Linux-x86_64-py311.AppImage](https://github.com/FreeCAD/FreeCAD-Bundle/releases/download/weekly-builds/FreeCAD_weekly-builds-40176-conda-Linux-x86_64-py311.AppImage)

Actually the stable Freecad AppImage also uses python 3.11, may get away with this:

https://github.com/FreeCAD/FreeCAD/releases

* [FreeCAD_1.0.0-conda-Linux-x86_64-py311.AppImage](https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Linux-x86_64-py311.AppImage)

Had to remove the previous version of freecad ( installed with snap) first

```bash
$ sudo snap remove freecad
```

To install an AppImage it is necessary to download the AppImage file, move to `~/Applications` folder, give it execution permission, then download an icon and create manually a desktop launcher. 
I use AppImageLauncher for that (downloaded from https://github.com/TheAssassin/AppImageLauncher/releases, simply download the deb file and double click on it to install. which takes care of integrating the App icon in desktop 

```bash
$ mkdir -p ~/Applications
$ wget https://github.com/FreeCAD/FreeCAD/releases/download/1.0.0/FreeCAD_1.0.0-conda-Linux-x86_64-py311.AppImage
```

Double click on the file and click on **Integrate and Run**



https://github.com/galou/freecad.cross

freecad --module-path ${PYTHONPATH//:/' --module-path '}

make sure to source your workspace before running freecad

pip install py-urdf-reader --allow-system-break

run Freecad with this system path

app image extract and run 

./Freecad-v-etc --appimage-extract-and-run --module-path ...

check out an example in vscode modify the path to the app image you download



