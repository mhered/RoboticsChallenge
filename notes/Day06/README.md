# Day06 - How To Control An Autonomous Robot With Code Instead of A GUI

launch the Navigation Task (already there should be map)

```bash
$ ros2 topic echo /goal_pose
```

Goal Pose sends `PoseStamped`messages in topic `/goal_pose`: made of header, position x,y,z and orientation (quaternion) x,y,z,w 

## inspect Node `bar_examples/krytn/move_krytn_topic.py`

* creates a node named `krytn_mover`

* creates a publisher for `PoseStamped` messages
* creates a clock for the timestamps
* creates a logger to publish through the logging system
* builds the message: coordinates x,y, frame_id and timestamp
* publishes
* logs a message
* waits 1s 
* shuts down

Can be run with:

```bash
$ source install/setup.bash
$ ros2 run krytn move_krytn_topic.py
```

## Task

edit the node to send the robot to a desired location

later we will do an action server, but the topic is the easiest to automate.

For the fun I decided to make a valet service: a Node that takes Krytn to a docking station.

So I wanted to define two waypoints, an "Approach position" so the robot can rotate safely away from the docking station and then reverse the last stretch towards the "Docked position" 

Apparently, easier said than done.

```python
ApproachPose = PoseStamped()
ApproachPose.pose.position.x = 0.0
ApproachPose.pose.position.y = 0.0
ApproachPose.pose.orientation.z = 0.9
ApproachPose.pose.orientation.w = -0.4

DockedPose = PoseStamped()
DockedPose.pose.position.x = 0.259
DockedPose.pose.position.y = 0.542
DockedPose.pose.orientation.z = 0.9
DockedPose.pose.orientation.w = -0.4
```



Need a subscriber to the current pose, and a trigger to define when I reach the first waypoint

The idea was good but:

Started with `/pose` but it only publishes while the robot is moving, my bot got stuck waiting for `current_pose` to initialize

`/odom` publishes continuously but the coordinates are affected by drift, so they are not comparable with the goal pose

ChatGPT suggested something complicated using `/tf` and I need to investigate the frame of reference because it does not seem to be the same as for `/global_pose`

So still getting there...

--

Eventually I gave up, see result [dock_krytn.py](./dock_krytn.py)
