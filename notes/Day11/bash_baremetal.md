```bash
mhered@Vader:~/bar_ws$ ros2 topic list
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
mhered@Vader:~/bar_ws$ ros2 node list
/controller_manager
/gripper_controller
/gz_ros_control
/interactive_marker_display_107325084867888
/maci_controller
/maci_joint_state_broadcaster
/move_group
/move_group/moveit
/move_group_private_95921480119232
/moveit_3596753669
/moveit_549387618
/moveit_simple_controller_manager
/robot_state_publisher
/ros_gz_bridge
/rviz
/rviz_private_140618238957728
/transform_listener_impl_573d75dff060
/transform_listener_impl_573d766a1bf0
/transform_listener_impl_619c9135f640
/transform_listener_impl_7fe43c381ef0
mhered@Vader:~/bar_ws$ ros2 doctor
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: twist_stamper has been updated to a new version. local: 0.0.3 < latest: 0.0.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: opennav_docking has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: dwb_core has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros2controlcli has been updated to a new version. local: 4.25.0 < latest: 4.26.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: compressed_depth_image_transport has been updated to a new version. local: 4.0.3 < latest: 4.0.4
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_theta_star_planner has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_cmake_vendor has been updated to a new version. local: 0.0.8 < latest: 0.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_smoother has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_visualization has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav_2d_utils has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: dwb_msgs has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_behavior_tree has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_regulated_pure_pursuit_controller has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_dwb_controller has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_core has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: opennav_docking_core has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_rotation_shim_controller has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_util has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros_gz_image has been updated to a new version. local: 1.0.7 < latest: 1.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_navfn_planner has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_setup_controllers has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_costmap_2d has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_transport_vendor has been updated to a new version. local: 0.0.5 < latest: 0.0.6
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: diagnostic_updater has been updated to a new version. local: 4.2.1 < latest: 4.2.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_graceful_controller has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_math_vendor has been updated to a new version. local: 0.0.7 < latest: 0.0.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: costmap_queue has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_controller has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros_gz has been updated to a new version. local: 1.0.7 < latest: 1.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_simple_commander has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_constrained_smoother has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_utils_vendor has been updated to a new version. local: 0.0.4 < latest: 0.0.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_planners_ompl has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_occupancy_map_monitor has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: navigation2 has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: theora_image_transport has been updated to a new version. local: 4.0.3 < latest: 4.0.4
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_robot_interaction has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_simple_controller_manager has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_planners_chomp has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_bt_navigator has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_setup_framework has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_smac_planner has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: control_toolbox has been updated to a new version. local: 4.0.0 < latest: 4.0.1
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: zstd_image_transport has been updated to a new version. local: 4.0.3 < latest: 4.0.4
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: joint_limits has been updated to a new version. local: 4.25.0 < latest: 4.26.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_physics_vendor has been updated to a new version. local: 0.0.5 < latest: 0.0.6
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: controller_manager_msgs has been updated to a new version. local: 4.25.0 < latest: 4.26.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_perception has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_kinematics has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: image_transport_plugins has been updated to a new version. local: 4.0.3 < latest: 4.0.4
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_configs_utils has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_warehouse has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: message_filters has been updated to a new version. local: 4.11.3 < latest: 4.11.4
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_planner has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: dwb_plugins has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_planning has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_fuel_tools_vendor has been updated to a new version. local: 0.0.5 < latest: 0.0.6
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros_gz_sim has been updated to a new version. local: 1.0.7 < latest: 1.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_tools_vendor has been updated to a new version. local: 0.0.5 < latest: 0.0.6
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros_gz_bridge has been updated to a new version. local: 1.0.7 < latest: 1.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_setup_core_plugins has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_ros2_control_demos has been updated to a new version. local: 1.2.10 < latest: 1.2.11
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: chomp_motion_planner has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_behaviors has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_map_server has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_msgs has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: pilz_industrial_motion_planner has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_lifecycle_manager has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: rqt_plot has been updated to a new version. local: 1.4.0 < latest: 1.4.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_collision_monitor has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros_gz_interfaces has been updated to a new version. local: 1.0.7 < latest: 1.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_mppi_controller has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_setup_srdf_plugins has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: realtime_tools has been updated to a new version. local: 3.3.0 < latest: 3.4.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_amcl has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_sim_vendor has been updated to a new version. local: 0.0.7 < latest: 0.0.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: hardware_interface has been updated to a new version. local: 4.25.0 < latest: 4.26.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_bringup has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: controller_manager has been updated to a new version. local: 4.25.0 < latest: 4.26.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_core has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_common has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_sensors_vendor has been updated to a new version. local: 0.0.5 < latest: 0.0.6
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_move_group has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros2_control_test_assets has been updated to a new version. local: 4.25.0 < latest: 4.26.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: compressed_image_transport has been updated to a new version. local: 4.0.3 < latest: 4.0.4
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav_2d_msgs has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_rendering_vendor has been updated to a new version. local: 0.0.5 < latest: 0.0.6
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_msgs_vendor has been updated to a new version. local: 0.0.5 < latest: 0.0.6
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: opennav_docking_bt has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_planners_stomp has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_common_vendor has been updated to a new version. local: 0.0.7 < latest: 0.0.8
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: controller_interface has been updated to a new version. local: 4.25.0 < latest: 4.26.0
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_setup_assistant has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_ros_planning_interface has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: dwb_critics has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_gui_vendor has been updated to a new version. local: 0.0.4 < latest: 0.0.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_ros2_control has been updated to a new version. local: 1.2.10 < latest: 1.2.11
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: ros_gz_sim_demos has been updated to a new version. local: 1.0.7 < latest: 1.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_common has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: gz_plugin_vendor has been updated to a new version. local: 0.0.4 < latest: 0.0.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_waypoint_follower has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_velocity_smoother has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: sdformat_vendor has been updated to a new version. local: 0.0.8 < latest: 0.0.9
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: moveit_setup_app_plugins has been updated to a new version. local: 2.12.1 < latest: 2.12.2
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_rviz_plugins has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 122: UserWarning: nav2_voxel_grid has been updated to a new version. local: 1.3.4 < latest: 1.3.5
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/package.py: 130: UserWarning: Cannot find the latest versions of packages: ros_network_viz krytn_tray gamecity sensors maci_moveit krytn my_room [...]. Use `ros2 doctor --report` to see full list.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 45: UserWarning: Subscriber without publisher detected on /collision_object.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /diagnostics.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /display_contacts.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /display_planned_path.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /dynamic_joint_states.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /execute_trajectory/_action/feedback.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /execute_trajectory/_action/status.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /filtered_cloud.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /gripper_controller/controller_state.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /gripper_controller/transition_event.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /maci_controller/controller_state.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /maci_controller/transition_event.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /maci_joint_state_broadcaster/transition_event.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /monitored_planning_scene.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /move_action/_action/feedback.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /move_action/_action/status.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /pipeline_state.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /realsense/depth.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /realsense/image.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /robot_description.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /robot_description_semantic.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /rviz_moveit_motion_planning_display/robot_interaction_interactive_marker_topic/feedback.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /rviz_moveit_motion_planning_display/robot_interaction_interactive_marker_topic/update.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /sequence_move_group/_action/feedback.
/opt/ros/jazzy/lib/python3.12/site-packages/ros2doctor/api/topic.py: 42: UserWarning: Publisher without subscriber detected on /sequence_move_group/_action/status.

All 5 checks passed

mhered@Vader:~/bar_ws$ ^C
```

