```bash
ubuntu@9fabe9a532fc:/workspace$ ros2 topic list
/attached_collision_object
/clock
/collision_object
/diagnostics
/display_contacts
/display_planned_path
/dynamic_joint_states
/filtered_cloud
/gripper_controller/controller_state
/gripper_controller/joint_trajectory
/gripper_controller/transition_event
/joint_states
/maci_controller/controller_state
/maci_controller/joint_trajectory
/maci_controller/transition_event
/maci_joint_state_broadcaster/transition_event
/monitored_planning_scene
/parameter_events
/pipeline_state
/planning_scene
/planning_scene_world
/realsense/depth
/realsense/image
/realsense/points
/recognized_object_array
/robot_description
/robot_description_semantic
/rosout
/rviz_moveit_motion_planning_display/robot_interaction_interactive_marker_topic/feedback
/rviz_moveit_motion_planning_display/robot_interaction_interactive_marker_topic/update
/tf
/tf_static
/trajectory_execution_event
ubuntu@9fabe9a532fc:/workspace$ ros2 node list
/controller_manager
/gripper_controller
/gz_ros_control
/interactive_marker_display_94583645297888
/maci_controller
/maci_joint_state_broadcaster
/move_group
/move_group/moveit
/move_group_private_94754016111376
/moveit_1654599941
/moveit_48773058
/moveit_simple_controller_manager
/robot_state_publisher
/ros_gz_bridge
/rviz
/rviz_private_140034658915632
/transform_listener_impl_5605f836fb60
/transform_listener_impl_5605f83987a0
/transform_listener_impl_562da37d1f90
/transform_listener_impl_562da398bea0
/transform_listener_impl_7f5c5c052fb0
ubuntu@9fabe9a532fc:/workspace$ ros2 action list
/execute_trajectory
/gripper_controller/follow_joint_trajectory
/maci_controller/follow_joint_trajectory
/move_action
/sequence_move_group
ubuntu@9fabe9a532fc:/workspace$ ros2 service list
/apply_planning_scene
/check_state_validity
/clear_octomap
/compute_cartesian_path
/compute_fk
/compute_ik
/controller_manager/configure_controller
/controller_manager/describe_parameters
/controller_manager/get_logger_levels
/controller_manager/get_parameter_types
/controller_manager/get_parameters
/controller_manager/get_type_description
/controller_manager/list_controller_types
/controller_manager/list_controllers
/controller_manager/list_hardware_components
/controller_manager/list_hardware_interfaces
/controller_manager/list_parameters
/controller_manager/load_controller
/controller_manager/reload_controller_libraries
/controller_manager/set_hardware_component_state
/controller_manager/set_logger_levels
/controller_manager/set_parameters
/controller_manager/set_parameters_atomically
/controller_manager/switch_controller
/controller_manager/unload_controller
/get_planner_params
/get_planning_scene
/get_urdf
/gripper_controller/describe_parameters
/gripper_controller/get_logger_levels
/gripper_controller/get_parameter_types
/gripper_controller/get_parameters
/gripper_controller/get_type_description
/gripper_controller/list_parameters
/gripper_controller/query_state
/gripper_controller/set_logger_levels
/gripper_controller/set_parameters
/gripper_controller/set_parameters_atomically
/gz_ros_control/describe_parameters
/gz_ros_control/get_parameter_types
/gz_ros_control/get_parameters
/gz_ros_control/get_type_description
/gz_ros_control/list_parameters
/gz_ros_control/set_parameters
/gz_ros_control/set_parameters_atomically
/interactive_marker_display_94583645297888/describe_parameters
/interactive_marker_display_94583645297888/get_parameter_types
/interactive_marker_display_94583645297888/get_parameters
/interactive_marker_display_94583645297888/get_type_description
/interactive_marker_display_94583645297888/list_parameters
/interactive_marker_display_94583645297888/set_parameters
/interactive_marker_display_94583645297888/set_parameters_atomically
/load_geometry_from_file
/load_map
/maci_controller/describe_parameters
/maci_controller/get_logger_levels
/maci_controller/get_parameter_types
/maci_controller/get_parameters
/maci_controller/get_type_description
/maci_controller/list_parameters
/maci_controller/query_state
/maci_controller/set_logger_levels
/maci_controller/set_parameters
/maci_controller/set_parameters_atomically
/maci_joint_state_broadcaster/describe_parameters
/maci_joint_state_broadcaster/get_logger_levels
/maci_joint_state_broadcaster/get_parameter_types
/maci_joint_state_broadcaster/get_parameters
/maci_joint_state_broadcaster/get_type_description
/maci_joint_state_broadcaster/list_parameters
/maci_joint_state_broadcaster/set_logger_levels
/maci_joint_state_broadcaster/set_parameters
/maci_joint_state_broadcaster/set_parameters_atomically
/move_group/describe_parameters
/move_group/get_parameter_types
/move_group/get_parameters
/move_group/get_type_description
/move_group/list_parameters
/move_group/moveit/describe_parameters
/move_group/moveit/get_parameter_types
/move_group/moveit/get_parameters
/move_group/moveit/get_type_description
/move_group/moveit/list_parameters
/move_group/moveit/set_parameters
/move_group/moveit/set_parameters_atomically
/move_group/set_parameters
/move_group/set_parameters_atomically
/move_group_private_94754016111376/describe_parameters
/move_group_private_94754016111376/get_parameter_types
/move_group_private_94754016111376/get_parameters
/move_group_private_94754016111376/get_type_description
/move_group_private_94754016111376/list_parameters
/move_group_private_94754016111376/set_parameters
/move_group_private_94754016111376/set_parameters_atomically
/moveit_1654599941/describe_parameters
/moveit_1654599941/get_parameter_types
/moveit_1654599941/get_parameters
/moveit_1654599941/get_type_description
/moveit_1654599941/list_parameters
/moveit_1654599941/set_parameters
/moveit_1654599941/set_parameters_atomically
/moveit_48773058/describe_parameters
/moveit_48773058/get_parameter_types
/moveit_48773058/get_parameters
/moveit_48773058/get_type_description
/moveit_48773058/list_parameters
/moveit_48773058/set_parameters
/moveit_48773058/set_parameters_atomically
/moveit_simple_controller_manager/describe_parameters
/moveit_simple_controller_manager/get_parameter_types
/moveit_simple_controller_manager/get_parameters
/moveit_simple_controller_manager/get_type_description
/moveit_simple_controller_manager/list_parameters
/moveit_simple_controller_manager/set_parameters
/moveit_simple_controller_manager/set_parameters_atomically
/plan_kinematic_path
/plan_sequence_path
/query_planner_interface
/robot_state_publisher/describe_parameters
/robot_state_publisher/get_parameter_types
/robot_state_publisher/get_parameters
/robot_state_publisher/get_type_description
/robot_state_publisher/list_parameters
/robot_state_publisher/set_parameters
/robot_state_publisher/set_parameters_atomically
/ros_gz_bridge/describe_parameters
/ros_gz_bridge/get_parameter_types
/ros_gz_bridge/get_parameters
/ros_gz_bridge/get_type_description
/ros_gz_bridge/list_parameters
/ros_gz_bridge/set_parameters
/ros_gz_bridge/set_parameters_atomically
/rviz/describe_parameters
/rviz/get_parameter_types
/rviz/get_parameters
/rviz/get_type_description
/rviz/list_parameters
/rviz/reset_time
/rviz/set_parameters
/rviz/set_parameters_atomically
/rviz_moveit_motion_planning_display/robot_interaction_interactive_marker_topic/get_interactive_markers
/rviz_private_140034658915632/describe_parameters
/rviz_private_140034658915632/get_parameter_types
/rviz_private_140034658915632/get_parameters
/rviz_private_140034658915632/get_type_description
/rviz_private_140034658915632/list_parameters
/rviz_private_140034658915632/set_parameters
/rviz_private_140034658915632/set_parameters_atomically
/save_geometry_to_file
/save_map
/set_planner_params
/transform_listener_impl_5605f836fb60/get_type_description
/transform_listener_impl_5605f83987a0/get_type_description
/transform_listener_impl_562da37d1f90/get_type_description
/transform_listener_impl_562da398bea0/get_type_description
/transform_listener_impl_7f5c5c052fb0/get_type_description
ubuntu@9fabe9a532fc:/workspace$ ros2 doctor
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: twist_stamper has been updated to a new version. local: 0.0.3 < latest: 0.0.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: tf2_bullet has been updated to a new version. local: 0.36.7 < latest: 0.36.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_cmake_vendor has been updated to a new version. local: 0.0.8 < latest: 0.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: tf2_eigen has been updated to a new version. local: 0.36.7 < latest: 0.36.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: tf2 has been updated to a new version. local: 0.36.7 < latest: 0.36.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: tf2_kdl has been updated to a new version. local: 0.36.7 < latest: 0.36.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: rviz_default_plugins has been updated to a new version. local: 14.1.6 < latest: 14.1.7
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: rviz2 has been updated to a new version. local: 14.1.6 < latest: 14.1.7
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: tf2_ros_py has been updated to a new version. local: 0.36.7 < latest: 0.36.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_utils_vendor has been updated to a new version. local: 0.0.4 < latest: 0.0.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: message_filters has been updated to a new version. local: 4.11.3 < latest: 4.11.4
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: tf2_tools has been updated to a new version. local: 0.36.7 < latest: 0.36.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: tf2_eigen_kdl has been updated to a new version. local: 0.36.7 < latest: 0.36.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: tf2_ros has been updated to a new version. local: 0.36.7 < latest: 0.36.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: tf2_geometry_msgs has been updated to a new version. local: 0.36.7 < latest: 0.36.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: tf2_sensor_msgs has been updated to a new version. local: 0.36.7 < latest: 0.36.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: rqt_plot has been updated to a new version. local: 1.4.0 < latest: 1.4.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_math_vendor has been updated to a new version. local: 0.0.7 < latest: 0.0.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: tf2_py has been updated to a new version. local: 0.36.7 < latest: 0.36.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: rviz_assimp_vendor has been updated to a new version. local: 14.1.6 < latest: 14.1.7
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: rviz_common has been updated to a new version. local: 14.1.6 < latest: 14.1.7
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: rviz_rendering has been updated to a new version. local: 14.1.6 < latest: 14.1.7
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: rviz_ogre_vendor has been updated to a new version. local: 14.1.6 < latest: 14.1.7
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: geometry2 has been updated to a new version. local: 0.36.7 < latest: 0.36.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: tf2_msgs has been updated to a new version. local: 0.36.7 < latest: 0.36.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros_gz_sim has been updated to a new version. local: 1.0.7 < latest: 1.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: navigation2 has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: admittance_controller has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: control_toolbox has been updated to a new version. local: 3.4.0 < latest: 4.0.1
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_setup_assistant has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gpio_controllers has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_planners_chomp has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: forward_command_controller has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_velocity_smoother has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_mppi_controller has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_bringup has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: controller_manager_msgs has been updated to a new version. local: 4.21.0 < latest: 4.26.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_graceful_controller has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_setup_controllers has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ackermann_steering_controller has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: pilz_industrial_motion_planner has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: dwb_core has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_rendering_vendor has been updated to a new version. local: 0.0.5 < latest: 0.0.6
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: imu_sensor_broadcaster has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: geometric_shapes has been updated to a new version. local: 2.3.1 < latest: 2.3.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_setup_srdf_plugins has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_controller has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_constrained_smoother has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_dwb_controller has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_warehouse has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros2controlcli has been updated to a new version. local: 4.21.0 < latest: 4.26.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_common has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: dwb_msgs has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_theta_star_planner has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: range_sensor_broadcaster has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_simple_controller_manager has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: mecanum_drive_controller has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_waypoint_follower has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: eigen_stl_containers has been updated to a new version. local: 1.0.0 < latest: 1.1.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: srdfdom has been updated to a new version. local: 2.0.5 < latest: 2.0.7
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: dwb_plugins has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: controller_manager has been updated to a new version. local: 4.21.0 < latest: 4.26.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_move_group has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ur_description has been updated to a new version. local: 3.0.0 < latest: 3.0.1
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_simple_commander has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: position_controllers has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_sensors_vendor has been updated to a new version. local: 0.0.5 < latest: 0.0.6
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_sim_vendor has been updated to a new version. local: 0.0.6 < latest: 0.0.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: dwb_critics has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_common_vendor has been updated to a new version. local: 0.0.7 < latest: 0.0.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: pose_broadcaster has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros2_controllers has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: zstd_image_transport has been updated to a new version. local: 4.0.3 < latest: 4.0.4
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: parameter_traits has been updated to a new version. local: 0.3.9 < latest: 0.4.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: compressed_image_transport has been updated to a new version. local: 4.0.3 < latest: 4.0.4
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: bondcpp has been updated to a new version. local: 4.1.0 < latest: 4.1.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: theora_image_transport has been updated to a new version. local: 4.0.3 < latest: 4.0.4
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_behavior_tree has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: tricycle_controller has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros_gz_bridge has been updated to a new version. local: 1.0.7 < latest: 1.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: compressed_depth_image_transport has been updated to a new version. local: 4.0.3 < latest: 4.0.4
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_amcl has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: generate_parameter_library_py has been updated to a new version. local: 0.3.9 < latest: 0.4.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: steering_controllers_library has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_behaviors has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: hardware_interface has been updated to a new version. local: 4.21.0 < latest: 4.26.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_fuel_tools_vendor has been updated to a new version. local: 0.0.5 < latest: 0.0.6
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_voxel_grid has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: realtime_tools has been updated to a new version. local: 3.0.0 < latest: 3.4.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: opennav_docking has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros_gz_sim_demos has been updated to a new version. local: 1.0.7 < latest: 1.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: sdformat_vendor has been updated to a new version. local: 0.0.8 < latest: 0.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: smclib has been updated to a new version. local: 4.1.0 < latest: 4.1.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_gui_vendor has been updated to a new version. local: 0.0.4 < latest: 0.0.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav_2d_msgs has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_plugin_vendor has been updated to a new version. local: 0.0.4 < latest: 0.0.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_transport_vendor has been updated to a new version. local: 0.0.5 < latest: 0.0.6
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: pid_controller has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: costmap_queue has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: force_torque_sensor_broadcaster has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_msgs_vendor has been updated to a new version. local: 0.0.5 < latest: 0.0.6
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_setup_app_plugins has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: velocity_controllers has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_smoother has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros_gz has been updated to a new version. local: 1.0.7 < latest: 1.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_setup_framework has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_smac_planner has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav_2d_utils has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_planning_interface has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_planning has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_msgs has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: controller_interface has been updated to a new version. local: 4.21.0 < latest: 4.26.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: chomp_motion_planner has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: diagnostic_updater has been updated to a new version. local: 4.2.1 < latest: 4.2.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_setup_core_plugins has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: parallel_gripper_controller has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_occupancy_map_monitor has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_rviz_plugins has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_core has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: joint_state_broadcaster has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: bicycle_steering_controller has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_configs_utils has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_map_server has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_rotation_shim_controller has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: tricycle_steering_controller has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_perception has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gripper_controllers has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: opennav_docking_bt has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: diff_drive_controller has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: joint_limits has been updated to a new version. local: 4.21.0 < latest: 4.26.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: joint_trajectory_controller has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_tools_vendor has been updated to a new version. local: 0.0.5 < latest: 0.0.6
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_physics_vendor has been updated to a new version. local: 0.0.5 < latest: 0.0.6
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: opennav_docking_core has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_visualization has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_regulated_pure_pursuit_controller has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_planner has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_util has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros_gz_image has been updated to a new version. local: 1.0.7 < latest: 1.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_collision_monitor has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_bt_navigator has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_planners_stomp has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros2_control_test_assets has been updated to a new version. local: 4.21.0 < latest: 4.26.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_robot_interaction has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: generate_parameter_library has been updated to a new version. local: 0.3.9 < latest: 0.4.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_planners_ompl has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_common has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: bond has been updated to a new version. local: 4.1.0 < latest: 4.1.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_navfn_planner has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros_gz_interfaces has been updated to a new version. local: 1.0.7 < latest: 1.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: image_transport_plugins has been updated to a new version. local: 4.0.3 < latest: 4.0.4
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_core has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_lifecycle_manager has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: effort_controllers has been updated to a new version. local: 4.18.0 < latest: 4.20.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_kinematics has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_costmap_2d has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 130: UserWarning: Cannot find the latest versions of packages: maci_moveit my_first_robot magni_description maci pymoveit2 krytn threading_examples gamecity [...]. Use `ros2 doctor --report` to see full list.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 45: UserWarning: Subscriber without publisher detected on /collision_object.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /diagnostics.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /display_contacts.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /dynamic_joint_states.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /filtered_cloud.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /gripper_controller/controller_state.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 45: UserWarning: Subscriber without publisher detected on /gripper_controller/joint_trajectory.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /gripper_controller/transition_event.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /maci_controller/controller_state.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 45: UserWarning: Subscriber without publisher detected on /maci_controller/joint_trajectory.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /maci_controller/transition_event.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /maci_joint_state_broadcaster/transition_event.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /pipeline_state.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /realsense/depth.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /realsense/image.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 45: UserWarning: Subscriber without publisher detected on /recognized_object_array.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /robot_description_semantic.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /sequence_move_group/_action/feedback.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /sequence_move_group/_action/status.

All 5 checks passed

ubuntu@9fabe9a532fc:/workspace$ 
```

