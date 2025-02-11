import os
import shutil

# Define the number of days
num_days = 28

# Base directory
base_dir = os.getcwd()

# Path to the existing thumbnail image
source_thumbnail = os.path.join(base_dir, "assets", "thumbnail.jpg")

# Check if the source thumbnail exists
if not os.path.exists(source_thumbnail):
    print("Error: The source thumbnail image does not exist in ./assets/thumbnail.jpg.")
    exit(1)

# Titles for each day based on the provided index
titles = [
    "3 Ways To Get You Computer Setup With Robotics - The easy way, the hard way and the dangerous way.",
    "The Right Way And The Wrong Way To Drive A Robot",
    "How Robotic Systems Communicate And How You Can Listen",
    "Robot Eyes Why You Need To See Through Them",
    "Don't Let Your Robot Become Lost - How To Give It A Map",
    "Self Driving Robot? How To Make A Robot Autonomous",
    "How To Control An Autonomous Robot With Code Instead of A GUI",
    "How To Use CAD To Create Custom Robot Links",
    "How To Add Your Custom Link To Your Robot",
    "3 Steps To Finding Problems To Solve With Wheeled Robots & How To Choose When You Have Too Many",
    "How To Control A Robot Arm - The Easy Way",
    "7 Useful Commands That Will Let You Interrogate Any ROS 2 System",
    "3 Steps To Designing A Simple Gripper In CAD",
    "How To Install A Gripper On Your Robot Arm In Simulation",
    "How To Setup The ROS2 Standard For Joint Control And How To Control Joints With Code",
    "The Easy Way To Setup Your Robot Arm - Configuring MoveIT 2",
    "How To Control A Full Robot Arm With Code",
    "How To Create A Gazebo World - Adding Something To Pickup",
    "How To Stop Your Robot Arm From Hitting Things - Adding Collision Avoidance Sensors To Your Robot Arm",
    "How To Find Problems That Robot Arms Can Solve And How To Choose One",
    "A Starter Template For Designing Wheel Robots In CAD For ROS",
    "3 Things To Consider When Choosing Your Robot Project",
    "How To Use Photos To Quickly Create Realistic Robot Models In CAD",
    "Exporting Your Robot From FreeCAD And Configuring ROS 2 Control So You Can Teleoperate It",
    "3 Tips To Create a compelling an environment for your robot",
    "2 Important Sensors To Consider Adding To Your Robot",
    "How To Iterate On A Robot Simulation To Make It More Realistic",
    "How To Configure Mapping & Navigation So Your Custom Robot Can Drive Itself",
    "How To Control Your Custom Robot With Code To Make It Really Autonomous"
]

# Loop to create directories and files
for day in range(num_days + 1):  # Including Day 0
    day_str = f"Day{day:02d}"
    day_path = os.path.join(base_dir, day_str)
    
    # Create the main directory for the day
    os.makedirs(day_path, exist_ok=True)
    
    # Create assets folder
    assets_path = os.path.join(day_path, "assets")
    os.makedirs(assets_path, exist_ok=True)

    # Copy the existing thumbnail image
    destination_thumbnail = os.path.join(assets_path, "thumbnail.jpg")
    shutil.copy(source_thumbnail, destination_thumbnail)

    # Create README.md with the corresponding title
    readme_path = os.path.join(day_path, "README.md")
    with open(readme_path, "w") as readme_file:
        readme_file.write(f"# {day_str} - {titles[day]}\n\nContent coming soon...\n")

print("Folders and files generated successfully.")

