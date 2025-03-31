# Day17 - How To Create A Gazebo World - Adding Something To Pickup

## Part 1: Care for a Coke?

1. Launch the simulation: `Ctrl` + `Shift` + `P` > **Tasks: Run Task** > **my_robot_arm Gazebo**

2. Open the **Resource Spawner** and insert a coffee table and a coke can

3. Save the world as `my_robot_arm/urdf/coke_pickup.sdf`, and edit the XML file to:

   * delete the model of the robot arm (will be spawned by the launch file) 

   * set the `Static` tag to `False` for  the Coke model 

   * scale the `visual` and `collision` meshes of the Coke model (the can is too slim) adding `<scale>1.1 1.1 1.1</scale>` 
   * modify the inertial properties of the Coke can. Assumed a solid cylinder approximation for a European Coke can (mass = 0.35 kg, radius = 0.033 m, height = 0.115 m):

```
<inertial>
  <mass>0.35</mass>
  <inertia>
    <ixx>0.000481</ixx>
    <iyy>0.000481</iyy>
    <izz>0.000191</izz>
    <ixy>0</ixy>
    <ixz>0</ixz>
    <iyz>0</iyz>
  </inertia>
  <pose>0 0 0 0 0 0</pose>
</inertial>
```

4. Modify the launch file `gazebo.launch.py` to:

* open the newly created world file instead of the default `empty.sdf`

```python
...
    # Gazebo Sim.
    pkg_ros_gz_sim = get_package_share_directory('ros_gz_sim')

    world_file = os.path.join(
        get_package_share_directory(resources_package),
        'urdf',
        'coke_pickup.sdf'
    )
  
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_ros_gz_sim, 'launch', 'gz_sim.launch.py'),
        ),
        launch_arguments=dict(gz_args=f'-r {world_file} --verbose').items(),
    )
...
```

* spawn the robotic arm a little lower (z=1.0m)

```python
...
	# Step 3. Spawn a robot in gazebo by listening to the published topic.
    robot = Node(
        package='ros_gz_sim',
        executable="create",
        arguments=[
            "-topic", "/robot_description", 
            "-z", "1.0", # was 0.5 but then arm hits floor
        ],
        name="spawn_robot",
        output="both"
...
```

5. Move the robot arm directly above the Coke can manually, get the joint positions with `ros2 topic echo` `/joint_states`  and add a new saved pose by manually editing `my_robot_arm_moveit/config/my_robot_arm.srdf`:

```    xml
<group_state name="Approach" group="arm">
	<joint name="ur5_shoulder_pan_joint" value="0.4080"/>
    <joint name="ur5_shoulder_lift_joint" value="0.2496"/>
    <joint name="ur5_elbow_joint" value="-0.9990"/>
    <joint name="ur5_wrist_1_joint" value="-2.4071"/>
    <joint name="ur5_wrist_2_joint" value="-0.3955"/>
    <joint name="ur5_wrist_3_joint" value="0.0101"/>
</group_state>
```

Note:  check out if this new saved pose (added manually) survives loading into the wizard and saving again (!!)

Note there is a mistake in the scaling: In practice, **diameter is roughly the same** — the EU can is just **shorter**. Hence the most realistic way to scale should be `<scale>1 1 0.943</scale>`

|              | U.S. Can (355 ml) | EU Can (330 ml) | Ratio (EU / US) |
| ------------ | ----------------- | --------------- | --------------- |
| **Height**   | ~122 mm           | ~115 mm         | **0.943**       |
| **Diameter** | ~66 mm            | ~66 mm          | **1.0**         |
| **Volume**   | 355 ml            | 330 ml          | **0.930**       |

In any case, I need to tilt the robot arm to prevent the can from falling

![](./assets/Day17_teaser.gif)

## Part2 - Adding Sensors
