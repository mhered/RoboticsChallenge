```bash
 *  Executing task: bash .vscode/scripts/maci_gazebo.sh 

Starting >>> maci    
Starting >>> gamecity
Starting >>> krytn
Starting >>> krytn_tray
Starting >>> magni_description
Starting >>> my_first_robot
Starting >>> my_room
Starting >>> pymoveit2
Starting >>> robotiq_2f_140_gripper_visualization
Starting >>> sensors
Starting >>> threading_examples
Starting >>> twist_stamper
Finished <<< gamecity [0.16s]                                                                                                       
Finished <<< krytn_tray [0.16s]
Finished <<< my_first_robot [0.17s]
Finished <<< maci [0.19s]
Starting >>> maci_moveit
Finished <<< magni_description [0.19s]                                                                                                            
Finished <<< my_room [0.20s]
Finished <<< krytn [0.22s]
Finished <<< robotiq_2f_140_gripper_visualization [0.21s]
Finished <<< threading_examples [0.21s]
Finished <<< sensors [0.22s]
Finished <<< twist_stamper [0.22s]
Finished <<< maci_moveit [0.14s]                                                       
Finished <<< pymoveit2 [0.43s]                    

Summary: 13 packages finished [0.59s]
[INFO] [launch]: All log files can be found below /home/mhered/.ros/log/2025-02-19-11-15-42-795039-Vader-1010253
[INFO] [launch]: Default logging verbosity is set to INFO
[INFO] [gazebo-1]: process started with pid [1010289]
[INFO] [parameter_bridge-2]: process started with pid [1010290]
[INFO] [robot_state_publisher-3]: process started with pid [1010291]
[INFO] [create-4]: process started with pid [1010293]
[INFO] [move_group-5]: process started with pid [1010294]
[INFO] [rviz2-6]: process started with pid [1010295]
[INFO] [ros2-7]: process started with pid [1010297]
[INFO] [ros2-8]: process started with pid [1010298]
[create-4] [INFO] [1739960143.993678608] [spawn_robot]: Requesting list of world names.
[robot_state_publisher-3] [INFO] [1739960143.999203706] [robot_state_publisher]: Robot initialized
[parameter_bridge-2] [INFO] [1739960144.016167917] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/clock (gz.msgs.Clock) -> /clock (rosgraph_msgs/msg/Clock)] (Lazy 0)
[parameter_bridge-2] [INFO] [1739960144.017818319] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/realsense/image (gz.msgs.Image) -> /realsense/image (sensor_msgs/msg/Image)] (Lazy 0)
[parameter_bridge-2] [INFO] [1739960144.019793937] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/realsense/depth (gz.msgs.Image) -> /realsense/depth (sensor_msgs/msg/Image)] (Lazy 0)
[parameter_bridge-2] [INFO] [1739960144.020128046] [ros_gz_bridge]: Creating GZ->ROS Bridge: [/realsense/points (gz.msgs.PointCloudPacked) -> /realsense/points (sensor_msgs/msg/PointCloud2)] (Lazy 0)
[move_group-5] [INFO] [1739960144.021105564] [move_group.moveit.moveit.ros.rdf_loader]: Loaded robot model in 0.00307659 seconds
[move_group-5] [INFO] [1739960144.021190977] [move_group.moveit.moveit.core.robot_model]: Loading robot model 'maci'...
[move_group-5] [INFO] [1739960144.035813485] [move_group.moveit.moveit.kinematics.kdl_kinematics_plugin]: Joint weights for group 'ur5': 1 1 1 1 1 1
[move_group-5] [ERROR] [1739960144.035994938] [move_group.moveit.moveit.kinematics.kdl_kinematics_plugin]: Group 'gripper' is not a chain
[move_group-5] [ERROR] [1739960144.036022477] [move_group.moveit.moveit.ros.kinematics_plugin_loader]: Kinematics solver of type 'kdl_kinematics_plugin/KDLKinematicsPlugin' could not be initialized for group 'gripper'
[move_group-5] [ERROR] [1739960144.036033117] [move_group.moveit.moveit.ros.robot_model_loader]: Kinematics solver could not be instantiated for joint group gripper.
[move_group-5] [INFO] [1739960144.081293388] [move_group.moveit.moveit.ros.planning_scene_monitor]: Publishing maintained planning scene on 'monitored_planning_scene'
[move_group-5] [INFO] [1739960144.081447328] [move_group.moveit.moveit.ros.moveit_cpp]: Listening to 'joint_states' for joint states
[move_group-5] [INFO] [1739960144.082126791] [move_group.moveit.moveit.ros.current_state_monitor]: Listening to joint states on topic 'joint_states'
[move_group-5] [INFO] [1739960144.082680118] [move_group.moveit.moveit.ros.planning_scene_monitor]: Listening to '/attached_collision_object' for attached collision objects
[move_group-5] [INFO] [1739960144.082705260] [move_group.moveit.moveit.ros.planning_scene_monitor]: Stopping existing planning scene publisher.
[move_group-5] [INFO] [1739960144.082857127] [move_group.moveit.moveit.ros.planning_scene_monitor]: Stopped publishing maintained planning scene.
[move_group-5] [INFO] [1739960144.083195343] [move_group.moveit.moveit.ros.planning_scene_monitor]: Publishing maintained planning scene on 'monitored_planning_scene'
[move_group-5] [INFO] [1739960144.083262725] [move_group.moveit.moveit.ros.planning_scene_monitor]: Starting planning scene monitor
[move_group-5] [INFO] [1739960144.083515372] [move_group.moveit.moveit.ros.planning_scene_monitor]: Listening to '/planning_scene'
[move_group-5] [INFO] [1739960144.083529564] [move_group.moveit.moveit.ros.planning_scene_monitor]: Starting world geometry update monitor for collision objects, attached objects, octomap updates.
[move_group-5] [INFO] [1739960144.084118339] [move_group.moveit.moveit.ros.planning_scene_monitor]: Listening to 'collision_object'
[move_group-5] [INFO] [1739960144.084385164] [move_group.moveit.moveit.ros.planning_scene_monitor]: Listening to 'planning_scene_world' for planning scene world geometry
[move_group-5] [WARN] [1739960144.085116565] [move_group.moveit.moveit.ros.occupancy_map_monitor]: Resolution not specified for Octomap. Assuming resolution = 0.1 instead
[move_group-5] [INFO] [1739960144.155905487] [move_group.moveit.moveit.ros.pointcloud_octomap_updater]: Listening to '/realsense/points' using message filter with target frame 'world '
[move_group-5] [INFO] [1739960144.160267018] [move_group.moveit.moveit.ros.planning_pipeline]: Successfully loaded planner 'CHOMP'
[move_group-5] [INFO] [1739960144.160861001] [move_group]: Try loading adapter 'default_planning_request_adapters/ResolveConstraintFrames'
[move_group-5] [INFO] [1739960144.161758665] [move_group]: Loaded adapter 'default_planning_request_adapters/ResolveConstraintFrames'
[move_group-5] [INFO] [1739960144.161774375] [move_group]: Try loading adapter 'default_planning_request_adapters/ValidateWorkspaceBounds'
[move_group-5] [INFO] [1739960144.161922610] [move_group]: Loaded adapter 'default_planning_request_adapters/ValidateWorkspaceBounds'
[move_group-5] [INFO] [1739960144.161928010] [move_group]: Try loading adapter 'default_planning_request_adapters/CheckStartStateBounds'
[move_group-5] [INFO] [1739960144.161945414] [move_group]: Loaded adapter 'default_planning_request_adapters/CheckStartStateBounds'
[move_group-5] [INFO] [1739960144.161948085] [move_group]: Try loading adapter 'default_planning_request_adapters/CheckStartStateCollision'
[move_group-5] [INFO] [1739960144.161955941] [move_group]: Loaded adapter 'default_planning_request_adapters/CheckStartStateCollision'
[move_group-5] [INFO] [1739960144.162503791] [move_group]: Try loading adapter 'default_planning_response_adapters/AddTimeOptimalParameterization'
[move_group-5] [INFO] [1739960144.165351295] [move_group]: Loaded adapter 'default_planning_response_adapters/AddTimeOptimalParameterization'
[move_group-5] [INFO] [1739960144.165370426] [move_group]: Try loading adapter 'default_planning_response_adapters/ValidateSolution'
[move_group-5] [INFO] [1739960144.167782075] [move_group]: Loaded adapter 'default_planning_response_adapters/ValidateSolution'
[move_group-5] [INFO] [1739960144.167794867] [move_group]: Try loading adapter 'default_planning_response_adapters/DisplayMotionPath'
[move_group-5] [INFO] [1739960144.168162728] [move_group]: Loaded adapter 'default_planning_response_adapters/DisplayMotionPath'
[move_group-5] [INFO] [1739960144.177296197] [move_group.moveit.moveit.ros.planning_pipeline]: Successfully loaded planner 'OMPL'
[move_group-5] [INFO] [1739960144.177800365] [move_group]: Try loading adapter 'default_planning_request_adapters/ResolveConstraintFrames'
[move_group-5] [INFO] [1739960144.177843703] [move_group]: Loaded adapter 'default_planning_request_adapters/ResolveConstraintFrames'
[move_group-5] [INFO] [1739960144.177847475] [move_group]: Try loading adapter 'default_planning_request_adapters/ValidateWorkspaceBounds'
[move_group-5] [INFO] [1739960144.177988598] [move_group]: Loaded adapter 'default_planning_request_adapters/ValidateWorkspaceBounds'
[move_group-5] [INFO] [1739960144.177992471] [move_group]: Try loading adapter 'default_planning_request_adapters/CheckStartStateBounds'
[move_group-5] [INFO] [1739960144.178002816] [move_group]: Loaded adapter 'default_planning_request_adapters/CheckStartStateBounds'
[move_group-5] [INFO] [1739960144.178004802] [move_group]: Try loading adapter 'default_planning_request_adapters/CheckStartStateCollision'
[move_group-5] [INFO] [1739960144.178011373] [move_group]: Loaded adapter 'default_planning_request_adapters/CheckStartStateCollision'
[move_group-5] [INFO] [1739960144.178406761] [move_group]: Try loading adapter 'default_planning_response_adapters/AddTimeOptimalParameterization'
[move_group-5] [INFO] [1739960144.178563498] [move_group]: Loaded adapter 'default_planning_response_adapters/AddTimeOptimalParameterization'
[move_group-5] [INFO] [1739960144.178567903] [move_group]: Try loading adapter 'default_planning_response_adapters/ValidateSolution'
[move_group-5] [INFO] [1739960144.178872533] [move_group]: Loaded adapter 'default_planning_response_adapters/ValidateSolution'
[move_group-5] [INFO] [1739960144.178881521] [move_group]: Try loading adapter 'default_planning_response_adapters/DisplayMotionPath'
[move_group-5] [INFO] [1739960144.179049724] [move_group]: Loaded adapter 'default_planning_response_adapters/DisplayMotionPath'
[move_group-5] [INFO] [1739960144.180602605] [move_group.moveit.moveit.planners.pilz.joint_limits_aggregator]: Reading limits from namespace robot_description_planning
[move_group-5] [INFO] [1739960144.184672610] [move_group.moveit.moveit.planners.pilz.command_planner]: Available plugins: pilz_industrial_motion_planner/PlanningContextLoaderCIRC pilz_industrial_motion_planner/PlanningContextLoaderLIN pilz_industrial_motion_planner/PlanningContextLoaderPTP 
[move_group-5] [INFO] [1739960144.184716336] [move_group.moveit.moveit.planners.pilz.command_planner]: About to load: pilz_industrial_motion_planner/PlanningContextLoaderCIRC
[move_group-5] [INFO] [1739960144.185767815] [move_group.moveit.moveit.planners.pilz.command_planner]: Registered Algorithm [CIRC]
[move_group-5] [INFO] [1739960144.185786858] [move_group.moveit.moveit.planners.pilz.command_planner]: About to load: pilz_industrial_motion_planner/PlanningContextLoaderLIN
[move_group-5] [INFO] [1739960144.186529457] [move_group.moveit.moveit.planners.pilz.command_planner]: Registered Algorithm [LIN]
[move_group-5] [INFO] [1739960144.186546118] [move_group.moveit.moveit.planners.pilz.command_planner]: About to load: pilz_industrial_motion_planner/PlanningContextLoaderPTP
[move_group-5] [INFO] [1739960144.187141334] [move_group.moveit.moveit.planners.pilz.command_planner]: Registered Algorithm [PTP]
[move_group-5] [INFO] [1739960144.187155673] [move_group.moveit.moveit.ros.planning_pipeline]: Successfully loaded planner 'Pilz Industrial Motion Planner'
[move_group-5] [INFO] [1739960144.187769682] [move_group]: Try loading adapter 'default_planning_request_adapters/ResolveConstraintFrames'
[move_group-5] [INFO] [1739960144.187823635] [move_group]: Loaded adapter 'default_planning_request_adapters/ResolveConstraintFrames'
[move_group-5] [INFO] [1739960144.187828349] [move_group]: Try loading adapter 'default_planning_request_adapters/ValidateWorkspaceBounds'
[move_group-5] [INFO] [1739960144.188083218] [move_group]: Loaded adapter 'default_planning_request_adapters/ValidateWorkspaceBounds'
[move_group-5] [INFO] [1739960144.188104235] [move_group]: Try loading adapter 'default_planning_request_adapters/CheckStartStateBounds'
[move_group-5] [INFO] [1739960144.188137850] [move_group]: Loaded adapter 'default_planning_request_adapters/CheckStartStateBounds'
[move_group-5] [INFO] [1739960144.188145372] [move_group]: Try loading adapter 'default_planning_request_adapters/CheckStartStateCollision'
[move_group-5] [INFO] [1739960144.188161126] [move_group]: Loaded adapter 'default_planning_request_adapters/CheckStartStateCollision'
[move_group-5] [INFO] [1739960144.188891119] [move_group]: Try loading adapter 'default_planning_response_adapters/ValidateSolution'
[move_group-5] [INFO] [1739960144.189765795] [move_group]: Loaded adapter 'default_planning_response_adapters/ValidateSolution'
[move_group-5] [INFO] [1739960144.189783968] [move_group]: Try loading adapter 'default_planning_response_adapters/DisplayMotionPath'
[move_group-5] [INFO] [1739960144.190126847] [move_group]: Loaded adapter 'default_planning_response_adapters/DisplayMotionPath'
[move_group-5] [INFO] [1739960144.193497762] [move_group.moveit.moveit.ros.planning_pipeline]: Successfully loaded planner 'STOMP'
[move_group-5] [INFO] [1739960144.194241982] [move_group]: Try loading adapter 'default_planning_request_adapters/ResolveConstraintFrames'
[move_group-5] [INFO] [1739960144.194308343] [move_group]: Loaded adapter 'default_planning_request_adapters/ResolveConstraintFrames'
[move_group-5] [INFO] [1739960144.194317176] [move_group]: Try loading adapter 'default_planning_request_adapters/ValidateWorkspaceBounds'
[move_group-5] [INFO] [1739960144.194488097] [move_group]: Loaded adapter 'default_planning_request_adapters/ValidateWorkspaceBounds'
[move_group-5] [INFO] [1739960144.194499463] [move_group]: Try loading adapter 'default_planning_request_adapters/CheckStartStateBounds'
[move_group-5] [INFO] [1739960144.194523711] [move_group]: Loaded adapter 'default_planning_request_adapters/CheckStartStateBounds'
[move_group-5] [INFO] [1739960144.194530949] [move_group]: Try loading adapter 'default_planning_request_adapters/CheckStartStateCollision'
[move_group-5] [INFO] [1739960144.194546345] [move_group]: Loaded adapter 'default_planning_request_adapters/CheckStartStateCollision'
[move_group-5] [INFO] [1739960144.195236753] [move_group]: Try loading adapter 'default_planning_response_adapters/AddTimeOptimalParameterization'
[move_group-5] [INFO] [1739960144.195684529] [move_group]: Loaded adapter 'default_planning_response_adapters/AddTimeOptimalParameterization'
[move_group-5] [INFO] [1739960144.195698556] [move_group]: Try loading adapter 'default_planning_response_adapters/ValidateSolution'
[move_group-5] [INFO] [1739960144.196090350] [move_group]: Loaded adapter 'default_planning_response_adapters/ValidateSolution'
[move_group-5] [INFO] [1739960144.196104971] [move_group]: Try loading adapter 'default_planning_response_adapters/DisplayMotionPath'
[move_group-5] [INFO] [1739960144.196457129] [move_group]: Loaded adapter 'default_planning_response_adapters/DisplayMotionPath'
[rviz2-6] [INFO] [1739960144.226531828] [rviz2]: Stereo is NOT SUPPORTED
[rviz2-6] [INFO] [1739960144.226588931] [rviz2]: OpenGl version: 4.6 (GLSL 4.6)
[move_group-5] [INFO] [1739960144.234266885] [move_group.moveit.moveit.plugins.simple_controller_manager]: Added FollowJointTrajectory controller for maci_controller
[move_group-5] [INFO] [1739960144.235390735] [move_group.moveit.moveit.plugins.simple_controller_manager]: Added FollowJointTrajectory controller for gripper_controller
[move_group-5] [INFO] [1739960144.235533568] [move_group.moveit.moveit.plugins.simple_controller_manager]: Returned 2 controllers in list
[move_group-5] [INFO] [1739960144.235558360] [move_group.moveit.moveit.plugins.simple_controller_manager]: Returned 2 controllers in list
[move_group-5] [INFO] [1739960144.235785744] [move_group.moveit.moveit.ros.trajectory_execution_manager]: Trajectory execution is managing controllers
[move_group-5] [INFO] [1739960144.235801714] [move_group]: MoveGroup debug mode is ON
[rviz2-6] [INFO] [1739960144.246830220] [rviz2]: Stereo is NOT SUPPORTED
[move_group-5] [INFO] [1739960144.251812064] [move_group.moveit.moveit.planners.pilz.move_group_sequence_action]: initialize move group sequence action
[move_group-5] [INFO] [1739960144.254896327] [move_group.moveit.moveit.planners.pilz.joint_limits_aggregator]: Reading limits from namespace robot_description_planning
[move_group-5] [INFO] [1739960144.255225218] [move_group.moveit.moveit.planners.pilz.joint_limits_aggregator]: Reading limits from namespace robot_description_planning
[move_group-5] [INFO] [1739960144.256112466] [move_group.moveit.moveit.ros.move_group.executable]: 
[move_group-5] 
[move_group-5] ********************************************************
[move_group-5] * MoveGroup using: 
[move_group-5] *     - apply_planning_scene_service
[move_group-5] *     - clear_octomap_service
[move_group-5] *     - get_group_urdf
[move_group-5] *     - load_geometry_from_file
[move_group-5] *     - CartesianPathService
[move_group-5] *     - execute_trajectory_action
[move_group-5] *     - get_planning_scene_service
[move_group-5] *     - kinematics_service
[move_group-5] *     - move_action
[move_group-5] *     - motion_plan_service
[move_group-5] *     - query_planners_service
[move_group-5] *     - state_validation_service
[move_group-5] *     - save_geometry_to_file
[move_group-5] *     - SequenceAction
[move_group-5] *     - SequenceService
[move_group-5] ********************************************************
[move_group-5] 
[move_group-5] [INFO] [1739960144.256175878] [move_group.moveit.moveit.ros.move_group.context]: MoveGroup context using pipeline ompl
[move_group-5] [INFO] [1739960144.256191078] [move_group.moveit.moveit.ros.move_group.context]: MoveGroup context initialization complete
[move_group-5] Loading 'move_group/ApplyPlanningSceneService'...
[move_group-5] Loading 'move_group/ClearOctomapService'...
[move_group-5] Loading 'move_group/GetUrdfService'...
[move_group-5] Loading 'move_group/LoadGeometryFromFileService'...
[move_group-5] Loading 'move_group/MoveGroupCartesianPathService'...
[move_group-5] Loading 'move_group/MoveGroupExecuteTrajectoryAction'...
[move_group-5] Loading 'move_group/MoveGroupGetPlanningSceneService'...
[move_group-5] Loading 'move_group/MoveGroupKinematicsService'...
[move_group-5] Loading 'move_group/MoveGroupMoveAction'...
[move_group-5] Loading 'move_group/MoveGroupPlanService'...
[move_group-5] Loading 'move_group/MoveGroupQueryPlannersService'...
[move_group-5] Loading 'move_group/MoveGroupStateValidationService'...
[move_group-5] Loading 'move_group/SaveGeometryToFileService'...
[move_group-5] Loading 'pilz_industrial_motion_planner/MoveGroupSequenceAction'...
[move_group-5] Loading 'pilz_industrial_motion_planner/MoveGroupSequenceService'...
[move_group-5] 
[move_group-5] You can start planning now!
[move_group-5] 
[rviz2-6] Warning: class_loader.impl: SEVERE WARNING!!! A namespace collision has occurred with plugin factory for class rviz_default_plugins::displays::InteractiveMarkerDisplay. New factory will OVERWRITE existing one. This situation occurs when libraries containing plugins are directly linked against an executable (the one running right now generating this message). Please separate plugins out into their own library or just don't link against the library and use either class_loader::ClassLoader/MultiLibraryClassLoader to open.
[rviz2-6]          at line 321 in /opt/ros/jazzy/include/class_loader/class_loader/class_loader_core.hpp
[create-4] [INFO] [1739960144.620896563] [spawn_robot]: Waiting messages on topic [robot_description].
[create-4] [INFO] [1739960144.720125850] [spawn_robot]: Entity creation successfull.
[INFO] [create-4]: process has finished cleanly [pid 1010293]
[move_group-5] [WARN] [1739960145.386693006] [tf2_buffer]: Detected time source change. Clearing TF buffer.
[move_group-5] [WARN] [1739960145.386749199] [tf2_buffer]: Detected time source change. Clearing TF buffer.
[INFO] [ros2-7]: process has finished cleanly [pid 1010297]
[gazebo-1] [INFO] [1739960146.463203487] [gz_ros_control]: [gz_ros2_control] Fixed joint [realsense_joint] (Entity=62)] is skipped
[gazebo-1] [INFO] [1739960146.463270472] [gz_ros_control]: [gz_ros2_control] Fixed joint [ur5_base_joint] (Entity=63)] is skipped
[gazebo-1] [INFO] [1739960146.466751298] [gz_ros_control]: Loading controller_manager
[gazebo-1] [INFO] [1739960146.478315892] [controller_manager]: Subscribing to '/robot_description' topic for robot description.
[gazebo-1] [WARN] [1739960146.478491295] [gz_ros_control]: Waiting RM to load and initialize hardware...
[gazebo-1] [INFO] [1739960147.005010747] [controller_manager]: Received robot description from topic.
[gazebo-1] [INFO] [1739960147.011538758] [gz_ros_control]: The position_proportional_gain has been set to: 0.1
[gazebo-1] [INFO] [1739960147.011630987] [gz_ros_control]: Loading joint: ur5_shoulder_pan_joint
[gazebo-1] [INFO] [1739960147.011637175] [gz_ros_control]:      State:
[gazebo-1] [INFO] [1739960147.011642238] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011670995] [gz_ros_control]:                       found initial value: 0.000000
[gazebo-1] [INFO] [1739960147.011679296] [gz_ros_control]:               velocity
[gazebo-1] [INFO] [1739960147.011687611] [gz_ros_control]:      Command:
[gazebo-1] [INFO] [1739960147.011691559] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011709542] [gz_ros_control]: Loading joint: ur5_shoulder_lift_joint
[gazebo-1] [INFO] [1739960147.011713573] [gz_ros_control]:      State:
[gazebo-1] [INFO] [1739960147.011717367] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011722363] [gz_ros_control]:                       found initial value: 0.000000
[gazebo-1] [INFO] [1739960147.011727120] [gz_ros_control]:               velocity
[gazebo-1] [INFO] [1739960147.011731014] [gz_ros_control]:      Command:
[gazebo-1] [INFO] [1739960147.011734194] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011746393] [gz_ros_control]: Loading joint: ur5_elbow_joint
[gazebo-1] [INFO] [1739960147.011750301] [gz_ros_control]:      State:
[gazebo-1] [INFO] [1739960147.011757079] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011762114] [gz_ros_control]:                       found initial value: 0.000000
[gazebo-1] [INFO] [1739960147.011766485] [gz_ros_control]:               velocity
[gazebo-1] [INFO] [1739960147.011770289] [gz_ros_control]:      Command:
[gazebo-1] [INFO] [1739960147.011773444] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011785177] [gz_ros_control]: Loading joint: ur5_wrist_1_joint
[gazebo-1] [INFO] [1739960147.011788879] [gz_ros_control]:      State:
[gazebo-1] [INFO] [1739960147.011792475] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011796468] [gz_ros_control]:                       found initial value: 0.000000
[gazebo-1] [INFO] [1739960147.011800431] [gz_ros_control]:               velocity
[gazebo-1] [INFO] [1739960147.011804171] [gz_ros_control]:      Command:
[gazebo-1] [INFO] [1739960147.011807364] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011818061] [gz_ros_control]: Loading joint: ur5_wrist_2_joint
[gazebo-1] [INFO] [1739960147.011822051] [gz_ros_control]:      State:
[gazebo-1] [INFO] [1739960147.011825629] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011831423] [gz_ros_control]:                       found initial value: 0.000000
[gazebo-1] [INFO] [1739960147.011835539] [gz_ros_control]:               velocity
[gazebo-1] [INFO] [1739960147.011839170] [gz_ros_control]:      Command:
[gazebo-1] [INFO] [1739960147.011842643] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011854039] [gz_ros_control]: Loading joint: ur5_wrist_3_joint
[gazebo-1] [INFO] [1739960147.011857857] [gz_ros_control]:      State:
[gazebo-1] [INFO] [1739960147.011861306] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011865134] [gz_ros_control]:                       found initial value: 0.000000
[gazebo-1] [INFO] [1739960147.011869163] [gz_ros_control]:               velocity
[gazebo-1] [INFO] [1739960147.011872664] [gz_ros_control]:      Command:
[gazebo-1] [INFO] [1739960147.011875893] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011885983] [gz_ros_control]: Loading joint: finger_joint
[gazebo-1] [INFO] [1739960147.011889709] [gz_ros_control]:      State:
[gazebo-1] [INFO] [1739960147.011893370] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011897441] [gz_ros_control]:                       found initial value: 0.000000
[gazebo-1] [INFO] [1739960147.011901358] [gz_ros_control]:               velocity
[gazebo-1] [INFO] [1739960147.011904833] [gz_ros_control]:      Command:
[gazebo-1] [INFO] [1739960147.011908085] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011918033] [gz_ros_control]: Loading joint: left_inner_finger_joint
[gazebo-1] [INFO] [1739960147.011924075] [gz_ros_control]:      State:
[gazebo-1] [INFO] [1739960147.011927811] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011966759] [gz_ros_control]:                       found initial value: 0.000000
[gazebo-1] [INFO] [1739960147.011972698] [gz_ros_control]:               velocity
[gazebo-1] [INFO] [1739960147.011976530] [gz_ros_control]:      Command:
[gazebo-1] [INFO] [1739960147.011979850] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.011991450] [gz_ros_control]: Loading joint: right_outer_knuckle_joint
[gazebo-1] [INFO] [1739960147.011995193] [gz_ros_control]:      State:
[gazebo-1] [INFO] [1739960147.011998868] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.012005759] [gz_ros_control]:                       found initial value: 0.000000
[gazebo-1] [INFO] [1739960147.012010163] [gz_ros_control]:               velocity
[gazebo-1] [INFO] [1739960147.012013873] [gz_ros_control]:      Command:
[gazebo-1] [INFO] [1739960147.012017127] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.012031059] [gz_ros_control]: Loading joint: right_inner_finger_joint
[gazebo-1] [INFO] [1739960147.012034881] [gz_ros_control]:      State:
[gazebo-1] [INFO] [1739960147.012038389] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.012042309] [gz_ros_control]:                       found initial value: 0.000000
[gazebo-1] [INFO] [1739960147.012046427] [gz_ros_control]:               velocity
[gazebo-1] [INFO] [1739960147.012050030] [gz_ros_control]:      Command:
[gazebo-1] [INFO] [1739960147.012053278] [gz_ros_control]:               position
[gazebo-1] [INFO] [1739960147.012156638] [gz_ros_control.resource_manager]: Initialize hardware 'ur5_' 
[gazebo-1] [INFO] [1739960147.012284207] [gz_ros_control.resource_manager]: Successful initialization of hardware 'ur5_'
[gazebo-1] [INFO] [1739960147.012384599] [resource_manager]: 'configure' hardware 'ur5_' 
[gazebo-1] [INFO] [1739960147.012390002] [gz_ros_control]: System Successfully configured!
[gazebo-1] [INFO] [1739960147.012396601] [resource_manager]: Successful 'configure' of hardware 'ur5_'
[gazebo-1] [INFO] [1739960147.012407221] [resource_manager]: 'activate' hardware 'ur5_' 
[gazebo-1] [INFO] [1739960147.012410699] [resource_manager]: Successful 'activate' of hardware 'ur5_'
[gazebo-1] [INFO] [1739960147.012425242] [controller_manager]: Resource Manager has been successfully initialized. Starting Controller Manager services...
[rviz2-6] [ERROR] [1739960147.365883716] [moveit_1723663066.moveit.ros.motion_planning_frame]: Action server: /recognize_objects not available
[rviz2-6] [INFO] [1739960147.385318043] [moveit_1723663066.moveit.ros.motion_planning_frame]: MoveGroup namespace changed: / -> . Reloading params.
[rviz2-6] [INFO] [1739960147.485158829] [moveit_1723663066.moveit.ros.rdf_loader]: Loaded robot model in 0.0468254 seconds
[rviz2-6] [INFO] [1739960147.485213482] [moveit_1723663066.moveit.core.robot_model]: Loading robot model 'maci'...
[rviz2-6] [INFO] [1739960147.496450379] [moveit_1723663066.moveit.kinematics.kdl_kinematics_plugin]: Joint weights for group 'ur5': 1 1 1 1 1 1
[rviz2-6] [ERROR] [1739960147.496705792] [moveit_1723663066.moveit.kinematics.kdl_kinematics_plugin]: Group 'gripper' is not a chain
[rviz2-6] [ERROR] [1739960147.496725776] [moveit_1723663066.moveit.ros.kinematics_plugin_loader]: Kinematics solver of type 'kdl_kinematics_plugin/KDLKinematicsPlugin' could not be initialized for group 'gripper'
[rviz2-6] [ERROR] [1739960147.496742939] [moveit_1723663066.moveit.ros.robot_model_loader]: Kinematics solver could not be instantiated for joint group gripper.
[rviz2-6] [INFO] [1739960147.549791611] [moveit_1723663066.moveit.ros.planning_scene_monitor]: Starting planning scene monitor
[rviz2-6] [INFO] [1739960147.550721105] [moveit_1723663066.moveit.ros.planning_scene_monitor]: Listening to '/monitored_planning_scene'
[INFO] [ros2-8]: process has finished cleanly [pid 1010298]
[rviz2-6] [INFO] [1739960148.010442514] [interactive_marker_display_107011310135008]: Connected on namespace: /rviz_moveit_motion_planning_display/robot_interaction_interactive_marker_topic
[rviz2-6] [INFO] [1739960148.013012129] [moveit_1723663066.moveit.ros.robot_interaction]: No active joints or end effectors found for group 'gripper'. Make sure that kinematics.yaml is loaded in this node's namespace.
[rviz2-6] [INFO] [1739960148.013460910] [moveit_1723663066.moveit.ros.robot_interaction]: No active joints or end effectors found for group 'gripper'. Make sure that kinematics.yaml is loaded in this node's namespace.
[rviz2-6] [INFO] [1739960148.017224477] [moveit_1723663066.moveit.ros.motion_planning_frame]: group gripper
[rviz2-6] [INFO] [1739960148.017251147] [moveit_1723663066.moveit.ros.motion_planning_frame]: Constructing new MoveGroup connection for group 'gripper' in namespace ''
[rviz2-6] [INFO] [1739960148.023762787] [interactive_marker_display_107011310135008]: Sending request for interactive markers
[rviz2-6] [INFO] [1739960148.024396871] [moveit_1723663066.moveit.ros.move_group_interface]: Ready to take commands for planning group gripper.
[rviz2-6] [INFO] [1739960148.024897270] [moveit_1723663066.moveit.ros.motion_planning_frame]: group gripper
[rviz2-6] [INFO] [1739960148.057970545] [interactive_marker_display_107011310135008]: Service response received for initialization
[gazebo-1] [WARN] [1739960148.514565029] [gz_ros_control]:  Desired controller update period (0.01 s) is slower than the gazebo simulation period (0.001 s).
[INFO] [spawner-9]: process started with pid [1010935]
[move_group-5] [WARN] [1739960154.205041230] []: Invalid frame ID "ur5_wrist_1_link" passed to canTransform argument source_frame - frame does not exist
[gazebo-1] [INFO] [1739960154.390319060] [controller_manager]: Loading controller : 'maci_joint_state_broadcaster' of type 'joint_state_broadcaster/JointStateBroadcaster'
[gazebo-1] [INFO] [1739960154.390378886] [controller_manager]: Loading controller 'maci_joint_state_broadcaster'
[gazebo-1] [INFO] [1739960154.394863381] [controller_manager]: Controller 'maci_joint_state_broadcaster' node arguments: --ros-args --params-file /home/mhered/bar_ws/install/share/maci/config/ros2_control.yaml --param use_sim_time:=true 
[spawner-9] [INFO] [1739960154.439993141] [spawner_maci_joint_state_broadcaster]: Loaded maci_joint_state_broadcaster
[gazebo-1] [INFO] [1739960154.441697790] [controller_manager]: Configuring controller: 'maci_joint_state_broadcaster'
[gazebo-1] [INFO] [1739960154.441956927] [maci_joint_state_broadcaster]: 'joints' or 'interfaces' parameter is empty. All available state interfaces will be published
[gazebo-1] [INFO] [1739960154.468886058] [controller_manager]: Activating controllers: [ maci_joint_state_broadcaster ]
[spawner-9] [INFO] [1739960154.502055439] [spawner_maci_joint_state_broadcaster]: Configured and activated maci_joint_state_broadcaster
[gazebo-1] [INFO] [1739960154.503319276] [controller_manager]: Loading controller : 'maci_controller' of type 'joint_trajectory_controller/JointTrajectoryController'
[gazebo-1] [INFO] [1739960154.503411633] [controller_manager]: Loading controller 'maci_controller'
[gazebo-1] [INFO] [1739960154.509345885] [controller_manager]: Controller 'maci_controller' node arguments: --ros-args --params-file /home/mhered/bar_ws/install/share/maci/config/ros2_control.yaml --param use_sim_time:=true 
[spawner-9] [INFO] [1739960154.541710213] [spawner_maci_joint_state_broadcaster]: Loaded maci_controller
[gazebo-1] [INFO] [1739960154.542130313] [controller_manager]: Configuring controller: 'maci_controller'
[gazebo-1] [INFO] [1739960154.542352167] [maci_controller]: No specific joint names are used for command interfaces. Using 'joints' parameter.
[gazebo-1] [INFO] [1739960154.542385831] [maci_controller]: Command interfaces are [position] and state interfaces are [position velocity].
[gazebo-1] [INFO] [1739960154.542418076] [maci_controller]: Using 'splines' interpolation method.
[gazebo-1] [INFO] [1739960154.544507195] [maci_controller]: Action status changes will be monitored at 20.00 Hz.
[gazebo-1] [INFO] [1739960154.573732561] [controller_manager]: Activating controllers: [ maci_controller ]
[spawner-9] [INFO] [1739960154.624684578] [spawner_maci_joint_state_broadcaster]: Configured and activated maci_controller
[gazebo-1] [INFO] [1739960154.625534422] [controller_manager]: Loading controller : 'gripper_controller' of type 'joint_trajectory_controller/JointTrajectoryController'
[gazebo-1] [INFO] [1739960154.625636788] [controller_manager]: Loading controller 'gripper_controller'
[gazebo-1] [INFO] [1739960154.626026382] [controller_manager]: Controller 'gripper_controller' node arguments: --ros-args --params-file /home/mhered/bar_ws/install/share/maci/config/ros2_control.yaml --param use_sim_time:=true 
[spawner-9] [INFO] [1739960154.658856576] [spawner_maci_joint_state_broadcaster]: Loaded gripper_controller
[gazebo-1] [INFO] [1739960154.659192635] [controller_manager]: Configuring controller: 'gripper_controller'
[gazebo-1] [INFO] [1739960154.659363546] [gripper_controller]: No specific joint names are used for command interfaces. Using 'joints' parameter.
[gazebo-1] [INFO] [1739960154.659388453] [gripper_controller]: Command interfaces are [position] and state interfaces are [position velocity].
[gazebo-1] [INFO] [1739960154.659401864] [gripper_controller]: Using 'splines' interpolation method.
[gazebo-1] [INFO] [1739960154.660895238] [gripper_controller]: Action status changes will be monitored at 20.00 Hz.
[gazebo-1] [INFO] [1739960154.679366077] [controller_manager]: Activating controllers: [ gripper_controller ]
[spawner-9] [INFO] [1739960154.729779047] [spawner_maci_joint_state_broadcaster]: Configured and activated gripper_controller
[INFO] [spawner-9]: process has finished cleanly [pid 1010935]
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

