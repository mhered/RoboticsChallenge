# 3D-Scanning And Importing Real Scenes Into Gazebo

Main source is this [tutorial](https://www.youtube.com/watch?v=DgUkGKIJ4wQ). 

1. I used [Scaniverse](https://scaniverse.com/) to quickly generate a 3D scan of a real scene using a smartphone.
2. Export as FDX
3. Import FDX in Blender and clean the file as explained in the tutorial. Removed floor, ceiling, and errors in the windows, and closed a couple of big holes. Note: I did not use the smooth brush because it opened holes. This [tutorial](https://www.youtube.com/watch?v=_pzTK-LBm3o) is even better for how to repair a 3D scan in Blender
4. Export as OBJ
5. Import in [Instant Meshes](https://github.com/wjakob/instant-meshes?tab=readme-ov-file) to make a smooth regular low poly mesh. Note: I did not use it because the mesh was already quite good, only 4k vertices, and the software opened holes in it.
6. Export as OBJ and reimport into Blender
7. Bake the texture in the low poly mesh as explained in the tutorial. Not needed for me as I did not modify the mesh.
8. Export as DAE 