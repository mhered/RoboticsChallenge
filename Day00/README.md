# Day00 - 3 Ways To Get You Computer Setup With Robotics - The easy way, the hard way and the dangerous way.

### Highlights

Day 0: Setting things up. The challenge's repo provides a containerized environment very easy to setup. Leveraging WLS, docker and the Dev Containers VS Code extension eliminates the need to fiddle with dual boot, ubuntu or ROS installs version compatibility, or dependencies. 

### Sources

[Course](https://course.becomearoboticist.com/)

[Discord channel](https://discord.gg/WpUGZYqXQN)

### First install

1. Download  [Visual Studio Code](https://code.visualstudio.com/Download) and install it
2. Download [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/) and install it - loong!
3. In Power Shell install WSL - long, and seems to require admin permissions:

```shell
> wsl --install
```

4. Restart the PC for changes to take effect

5. Run Docker (status should show: Engine running)

6. Launch an Ubuntu shell, clone the repo and open VS Code inside the folder

```bash
> ubuntu
$ cd ~
$ git clone https://github.com/johnny555/bar_ws.git
$ cd bar_ws
$ code . 
```

7. Install the Dev Containers VS Code extension
8. Open `bar_ws` folder in dev container. Ctrl+Caps + P > **Dev Containers: Open Folder in Container**... The first time it takes a very looong time to set up 20Gb of virtual machine
9. Ctrl+Caps + P > **Run Task** > **Test Gazebo**
10. In browser, open the GUI: `http://localhost:6080/` and play with Gazebo

### Relaunch

Run Docker  (status should show: Engine running)

Launch VS Code inside the `bar_ws` folder. e.g Open terminal typing `wsl` in the Search bar:

```bash
$ cd bar_ws
$ code .
```

**Reopen** the folder in container (or Ctrl+Caps + P > **Dev Containers: Open Folder in Container**... select `/home/mhered/bar_ws`  )

Ctrl+Caps + P > **Run Task** > **Test Gazebo**

In browser, open: `http://localhost:6080/`

Took actually a couple of days, played a bit with OBS Studio and made a video

## Kick Off meeting

Works for Nexus

Krytn & MACI Coffee robot

Read "Atomic Habits" James Clear - sprint to change self perception

"show your work" - a record, as a way to appreciate what we learn and get noticed

tag john vial

roughly 1 hour per day then write and share what I learnt for 28 consecutive days

Days 0-9 - Krytn Coffee Robot - standard ROS navigation stack then extend it using FreeCAD (add a tray)

10-19 MACI robot arm - adding collision avoidance. Controlling a robot arm is complicated. Extend it with our own gripper then pick up a can from a tray

20-28 build your own robot - find something relevant to you and simulate it! Will provide templates.

Additional Bonus videos to extend: real robots, frameworks and templates, AI...

Join Discord!

7 daily tasks each week (do the task and post about it)

Play with github copilot can help get unstuck

Copilot

Pearce - Engineering degree. Did robotics without ROS (was extracurricular). Doing PM in navy

11 pax in the cohort

## 
