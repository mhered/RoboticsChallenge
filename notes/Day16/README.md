# Day16 - How To Control A Full Robot Arm With Code

## Task

1. Copy`src/bar_examples/maci/maci/arm.py` into `src/my_robot_arm/my_robot_arm/arm.py`
2. in `arm.py` adjust the call to the `MoveIT2` node with `end_effector_name='gripper'` and `group_name ='arm'`
3. Modify the code to move the arm to a target joint position after moving to the home configuration. 
4. Launch the `my_robot_arm_Gazebo` task, move the arm manually to the desired goal and Execute while listening to the `/joint_states` topic with `$ ros2 topic echo /joint_states` to find out the joint positions of the goal state: 
   ```bash
   ---
   header:
     stamp:
       sec: 126
       nanosec: 260000000
     frame_id: ''
   name:
   - ur5_shoulder_pan_joint
   - ur5_shoulder_lift_joint
   - ur5_elbow_joint
   - ur5_wrist_1_joint
   - ur5_wrist_2_joint
   - ur5_wrist_3_joint
   - finger_joint
   position:
   - 0.13386034507103658
   - -1.3483869386130993
   - 1.4931502232541762
   - -0.8756904947793623
   - 1.388863205554156
   - 0.3726545947901117
   - 1.7440586090239478e-13
   velocity:
   - 1.2766480581016815e-14
   - -9.086481567166516e-14
   - 1.016166317757694e-13
   - -4.8176740374827887e-14
   - 1.060969888333485e-13
   - 2.531004919537061e-14
   - 3.6591823321385775e-19
   effort:
   - .nan
   - .nan
   - .nan
   - .nan
   - .nan
   - .nan
   - .nan
   ---
   ```

   Add this in `arm.py` as a python array: 
   ```
   pos_2 = [
       0.13386034507103658,
       -1.3483869386130993,
       1.4931502232541762,
       -0.8756904947793623,
       1.388863205554156,
       0.3726545947901117,
       1.7440586090239478e-13
   ]
   ```
5. In `src/my_robot_arm/CMakeLists.txt` install `arm.py` as a program that can be run:

```cmake
...
install(PROGRAMS
   my_robot_arm/gripper.py
   my_robot_arm/arm.py
   DESTINATION lib/${PROJECT_NAME}
)
```

5. Give `arm.py` execution permission: `$ chmod +x arm.py`
6. with `my_robot_arm_Gazebo` running, open a terminal, build and source, then execute with `$ ros2 run my_robot_arm arm.py` 

Success!!

![](./assets/Day16_teaser.gif)

