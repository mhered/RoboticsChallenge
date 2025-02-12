# Day03 - Robot Eyes Why You Need To See Through Them

* made a small investment to improve the quality of the videos: bought a dedicated microphone and webcam
* lots of fiddling with docker. My VNC failed to start, took me a while to realise the container was stopped
* keep getting the error  `Failed to activate container`  when launching Krytn Teleop, even though I added the 3s timer to the `joint_state_broadcaster` spawner in `gazebo.launch.py` as suggested by Danial Othman
* I eventually managed launching it together with Navigation then stopping Navigation. Now I get `Failed to configure controller` error but at least it works...Awkward...

