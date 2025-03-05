# Day14 - How To Setup The ROS2 Standard For Joint Control And How To Control Joints With Code

Configure the gripper using `ros2_control`

Note: `ros2 control` operates outside of ROS topics, services and actions to ensure low latency and reliability, but exposes interfaces to the ROS ecosystem

## Task

1. In `gazebo.launch.py` , `generate_launch_description()` add a task to run the `spawner` node from the `controller_manager` package to initialize the high level controllers `joint_state_broadcaster` and `gripper_controller` (copy and adapt from `src/bar_examples/maci/launch/spawn_maci.launch.py`):

```python
from launch.actions import TimerAction

...

	# Step 5: Enable the ros2 controllers
	start_controllers  = TimerAction(
		period=20.0,
	    actions=[
	    	Node(
	        	package="controller_manager",
	            executable="spawner",
	            arguments=['joint_state_broadcaster', 'gripper_controller'],
	            output="screen",
    	    )
    	]
	)
    return LaunchDescription([
        use_sim_time_launch_arg,
        use_rviz_arg,
        robot_state_publisher,
        rviz,
        gazebo,
        spawn,
        start_controllers,
    ])

```

2. In `my_robot_arm.urdf.xacro` add:

   * a `ros2_control` tag to add a position `command_interface` and position and velocity `state_interfaces` to the `finger_joint`
   * a gazebo tag to load the `gz_ros2_control-system` plugin with `config/ros2_control.yaml`as parameter file

   Note the `ros2_control` tag of `maci.urdf.xacro` is interesting as reference, defines a macro and calls it for each joint to reduce repetition.

```
  <ros2_control name="my_robot_arm" type="system">
    <hardware>
      <plugin>gz_ros2_control/GazeboSimSystem</plugin>
    </hardware>
    <joint name="finger_joint">
      <command_interface name="position"/>
      <state_interface name="position">
        <param name="initial_value">0.0</param>
      </state_interface>
      <state_interface name="velocity"/>
    </joint>
  </ros2_control>
  <gazebo>
    <plugin filename="gz_ros2_control-system" name="gz_ros2_control::GazeboSimROS2ControlPlugin">
      <parameters>$(find my_robot_arm)/config/ros2_control.yaml</parameters>
    </plugin>
  </gazebo>
```

2. Add a `ros2_controllers.yaml` file to the `config` directory, and populate it:

```yaml
controller_manager:
  ros__parameters:
    update_rate: 100 # Hz
    gripper_controller:
      type: joint_trajectory_controller/JointTrajectoryController
    joint_state_broadcaster:
      type: joint_state_broadcaster/JointStateBroadcaster
    use_sim_time: True

joint_state_broadcaster:
  ros__parameters:
    use_sim_time: True

gripper_controller:
  ros__parameters:
    joints:
      - finger_joint
    command_interfaces:
      - position
    state_interfaces:
      - position
      - velocity
```

3. In  `CMakeLists.txt`  add the new `config`  folder to the `install` directive

```cmake
...
install(DIRECTORY launch meshes rviz urdf config
  DESTINATION share/${PROJECT_NAME}
)
...
```

4. Build, source and launch and interrogate the system using ` ros2 control list_controllers`,  `ros2 control list_hardware_interfaces` and `ros2 action` 

```bash
$ ros2 control list_controllers
gripper_controller      joint_trajectory_controller/JointTrajectoryController  active
joint_state_broadcaster joint_state_broadcaster/JointStateBroadcaster          active

$ ros2 control list_hardware_interfaces
[INFO] [1741127442.997917703] [_ros2cli_579287]: waiting for service /controller_manager/list_hardware_interfaces to become available...
command interfaces
        finger_joint/position [available] [claimed]
state interfaces
        finger_joint/position
        finger_joint/velocity
$ ros2 action list
/gripper_controller/follow_joint_trajectory
```

Question 1: repetitive warning that there is no valid clock source:

```
[gazebo-4] [WARN] [1741131398.750750067] [controller_manager]: No clock received, using time argument instead! Check your node's clock configuration (use_sim_time parameter) and if a valid clock source is available
```

Indeed `/clock` topic exists but there is no traffic. After adding - see below - the gazebo `bridge` (simplified from  `gazebo.launch.py` in `maci`  ) the `/clock` traffic looks right and the warning has disappeared: 

```
 # Gazebo Bridge: This brings data (sensors/clock) out of gazebo into ROS.
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=['/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
                   ],
        output='screen')
    return LaunchDescription([
        use_sim_time_launch_arg,
        use_rviz_arg,
        robot_state_publisher,
        rviz,
        gazebo,
        spawn,
        start_controllers,
        bridge
    ])
```

Question 2: After configuring `ros2_control`  I was expecting the gripper should move in gazebo when we manually move the corresponding `joint_state_publisher` slider, but it does not.  @John said it should not even be launched so I set the `gui` flag to `False` to prevent the `joint_state_publisher` from running:

```
    rviz = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            PathJoinSubstitution([
                FindPackageShare(resources_package),
                'launch',
                'display.launch.py',
            ]),
        ]),
        condition=IfCondition(use_rviz),
        launch_arguments={'gui': 'false'}.items(),
    )
```

Yeah, but why?



Next we will control the joint by software

5. Copy the `gripper.py` file from `src/bar_examples/maci/maci/` into a new folder `src/my_robot_arm/my_robot_arm/`. Adjust its parameters so that it connects to the `FollowJointTrajectory`  action associated that you configured when setting up the controllers. 

3. Make the `gripper.py` script executable with `chmod +x src/my_robot_arm/my_robot_arm/gripper.py`
4. In  `CMakeLists.txt` register  `gripper.py` as a script that can be run using `ros2 run ` (to copying the install directive from the `maci` `CMakeLists.txt`)

```cmake
...
install(PROGRAMS
   my_robot_arm/gripper.py
   DESTINATION lib/${PROJECT_NAME}
)
```

8. Run your node (`ros2 run my_robot_arm gripper.py -j 0.03` ) and observe the gripper joint moving. 

## Troubleshooting

Everything seems to load ok, no errors. I run the `gripper.py` script and get the expected result:

```bash
$ ros2 run my_robot_arm gripper.py -j 0.034
server found
trajectory_msgs.msg.JointTrajectory(header=std_msgs.msg.Header(stamp=builtin_interfaces.msg.Time(sec=0, nanosec=0), frame_id=''), joint_names=['finger_joint'], points=[trajectory_msgs.msg.JointTrajectoryPoint(positions=[0.034], velocities=[], accelerations=[], effort=[], time_from_start=builtin_interfaces.msg.Duration(sec=0, nanosec=0))])
waiting for goal complete
Hi from my_robot_arm.
```

And it works: the gripper in Gazebo moves as expected.  I run it again, a second time, for a different position, and it works again.  But then after that, it just stops responding.  I tried many times and it is repetitive: works twice then no more.  Inspecting the stdout two things stand out:

1. Note this [stdout](./stdout.md)  dump os prior to adding the bridge. so the clock warnings are still there (most I replaced by `...`)

2. The logs for the two successful moves look like this:

```
...
[gazebo-4] [INFO] [1741131392.077697645] [gripper_controller]: Received new action goal
[gazebo-4] [INFO] [1741131392.077737220] [gripper_controller]: Accepted new action goal
[gazebo-4] [INFO] [1741131392.333088386] [gripper_controller]: Goal reached, success!
...
```

while those for the failed ones look like this:

```
...
[gazebo-4] [INFO] [1741131397.595267607] [gripper_controller]: Received new action goal
[gazebo-4] [INFO] [1741131397.595313906] [gripper_controller]: Accepted new action goal
...
[gazebo-4] [WARN] [1741131398.620612932] [gripper_controller]: Aborted due to goal_time_tolerance exceeding by 1.010000 seconds
...
```

I played with trajectory tolerances, tried increasing the goal time tolerance to 5 secs ... no difference. 

## Bonus - Threads and Callbacks

Video: https://www.youtube.com/watch?v=c8njYP3e9E4https://www.youtube.com/watch?v=c8njYP3e9E4

Examples in`src/bar_examples/threading_examples/threading_examples`

PENDING!
