## Rviz Tools for python 

Some useful tools for using ROS2 Rviz with python. 

Currently this package contains some functions that make it easy to publish Rviz Markers in a pythonic way.

Python code by **Luis Cruz**.

Based on David Butterworth Python library(ROS1) [rviz_tools_py](https://github.com/DavidB-CMU/rviz_tools_py) 

&

Based on PickNikRobotics C++ library [RvizVisualTools](https://github.com/PickNikRobotics/rviz_visual_tools)

This package been tested on Ubuntu 24.04 with ROS Jazzy.


**Usage examples:**

The normal way to publish an Rviz Marker is by setting its properties using ROS message types:
```
P = Pose(position=Point(x=0,y=0,z=0),orientation=Quaternion(x=0,y=0,z=0,w=1))
scale = Vector3(x=0.2,y=0.2,z=0.2)
markers.publishCube(P, 'red', scale)
```

**Demo:**

To run the example code:  
```
$ ros2 run rviz_tools_package demo
```

![rviz_tools_package](https://github.com/user-attachments/assets/8f8ed4f4-96ec-45fd-ae3f-a5204ac1cd17)

