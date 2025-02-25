# Day10 - How To Control A Robot Arm - The Easy Way

[Video Day 10](https://www.youtube.com/watch?v=Qts-iC2fEz0)

Teleoperating a robot arm is much more complex than driving wheels: many more motors and joints, changing pose typically involves moving every joint simultaneously while checking for self collisions

ROS2 package MoveIT2 to calculate trajectories

MACI robot arm 

2 planning groups `ur5` and `gripper`

* `ur5` allows moving the arm pulling from handles
* `gripper` no handles, can control joints individually

Note MACI Gripper requires that we control 4 joints because Gazebo cannot model mimic joints (a joint that copies another)

## Task

1. Run **MACI Gazebo** Task in VS Code
2. In **RViz** move the robot arm pulling the handles. IF collision is detected links go Red. If Planner fails try smaller move, faster scaling for vel and accel, longer plan time, tick Collision-aware IK (?)
3. Click the **Plan and Execute** button & watch the arm move.
4. Switch the planner group from `ur5` to `gripper`.
5. **Joints** Tab > Manually adjust the gripper joints 
6. Click **Plan and execute** & watch the gripper move

## Troubleshooting MoveIT

Plan and Execute generates movements of the arm and gripper but:

1. no color voxels (the collision model?) 
2. the arm never moves in gazebo (looks i am only planning, even tough I click plan and execute)  and 
3. I get a lot or error messages in the terminal, about missing frames. Any suggestions?

Inspecting error messages: `Failed to activate controller: maci_joint_state_broadcaster`

Adding a 10s `Timer Action` in the `spawn_maci.launch.py`to the spawner of node `maci_joint_state_broadcaster`  fixed it so I can now move the arm in gazebo.

 Still there is a number of errors remain at startup, the voxels are not showing and I really struggle to move the gripper.

* a first set of errors linked to the gripper and the kinematics solver (full log [here](./error_log.md)):

```
...
[move_group-5] [ERROR] [1739960144.035994938] [move_group.moveit.moveit.kinematics.kdl_kinematics_plugin]: Group 'gripper' is not a chain
[move_group-5] [ERROR] [1739960144.036022477] [move_group.moveit.moveit.ros.kinematics_plugin_loader]: Kinematics solver of type 'kdl_kinematics_plugin/KDLKinematicsPlugin' could not be initialized for group 'gripper'
[move_group-5] [ERROR] [1739960144.036033117] [move_group.moveit.moveit.ros.robot_model_loader]: Kinematics solver could not be instantiated for joint group gripper.
...
```

* then this one is not en ERROR but a SEVERE Warning:

```
...
[rviz2-6] Warning: class_loader.impl: SEVERE WARNING!!! A namespace collision has occurred with plugin factory for class rviz_default_plugins::displays::InteractiveMarkerDisplay. New factory will OVERWRITE existing one. This situation occurs when libraries containing plugins are directly linked against an executable (the one running right now generating this message). Please separate plugins out into their own library or just don't link against the library and use either class_loader::ClassLoader/MultiLibraryClassLoader to open.
...
```

* A few more, related to the action server `/recognize_objects` and again the gripper

```
...
[rviz2-6] [ERROR] [1739960147.365883716] [moveit_1723663066.moveit.ros.motion_planning_frame]: Action server: /recognize_objects not available
...
[rviz2-6] [ERROR] [1739960147.496705792] [moveit_1723663066.moveit.kinematics.kdl_kinematics_plugin]: Group 'gripper' is not a chain
[rviz2-6] [ERROR] [1739960147.496725776] [moveit_1723663066.moveit.ros.kinematics_plugin_loader]: Kinematics solver of type 'kdl_kinematics_plugin/KDLKinematicsPlugin' could not be initialized for group 'gripper'
[rviz2-6] [ERROR] [1739960147.496742939] [moveit_1723663066.moveit.ros.robot_model_loader]: Kinematics solver could not be instantiated for joint group gripper.
...
```

 And finally a bunch of errors about missing transforms:

```
...
[move_group-5] [ERROR] [1739960155.647872526] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape box with handle 13
[move_group-5] [ERROR] [1739960155.647945013] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape box with handle 17
[move_group-5] [ERROR] [1739960155.647961500] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape mesh with handle 4
[move_group-5] [ERROR] [1739960155.647974521] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape mesh with handle 5
[move_group-5] [ERROR] [1739960155.647986984] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape mesh with handle 3
[move_group-5] [ERROR] [1739960155.647999520] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape mesh with handle 7
[move_group-5] [ERROR] [1739960155.648011531] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape mesh with handle 9
[move_group-5] [ERROR] [1739960155.648026757] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape mesh with handle 6
[move_group-5] [ERROR] [1739960155.648038792] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape mesh with handle 8
[move_group-5] [ERROR] [1739960155.648050450] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape mesh with handle 11
[move_group-5] [ERROR] [1739960155.648062116] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape mesh with handle 15
[move_group-5] [ERROR] [1739960155.648073729] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape mesh with handle 10
[move_group-5] [ERROR] [1739960155.648085933] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape mesh with handle 14
[move_group-5] [ERROR] [1739960155.648097277] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape mesh with handle 12
[move_group-5] [ERROR] [1739960155.648108749] [move_group.moveit.moveit.ros.shape_mask]: Missing transform for shape mesh with handle 16
```

  
