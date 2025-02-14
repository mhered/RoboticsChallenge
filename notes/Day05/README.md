# Day05 - Self Driving Robot? How To Make A Robot Autonomous

launch Krytn Navigation task

set goal pose and away it goes!

to understand what happens under the hood: add global and local costs maps > for each position we assign a cost for the robot to be in this position then add global and local path. (Difference between local and global?) Calculates path minimum cost. 

* Local costmap `/local_costmap/costmap` Color Scheme: `map`

* Global costmap `/global_costmap/costmap` Color Scheme: `costmap`

* Local path: `/plan` Line Style: Billboards Line Width: 0.05 , Color: green 
  can fiddle with the 
* Global path: `/transformed_global_plan` Line Style: Billboards Line Width: 0.05 , Color: blue 

## inspecting the `navigation.launch.py`

`gazebo_and_mapping` opens rviz with different config `nav.rviz`

`navigation` launches `nav2_bringup.launch.py` with `navigation.yaml` config file

reuse the `twist_stamper`

## inspecting `navigation.yaml`

in `local_map` or in `global_map` we can reduce the `robot_radius` or the `inflation radius` so it gets closer to the wall
