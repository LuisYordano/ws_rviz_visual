#!/usr/bin/env python

"""
This is a demo of Rviz Tools for python which tests all of the
available functions by publishing lots of Markers in Rviz.
"""

# Python includes
import numpy as np
import threading

# ROS includes
import rclpy
from geometry_msgs.msg import Pose, Point, Quaternion, Vector3, Polygon
from rviz_tools_package.rviz_tools_node import RvizMarkers

# Initialize the ROS2 Node
rclpy.init()
node = rclpy.create_node('rviz_tools_demo')

markers = RvizMarkers('/world', 'rviz_tools_demo')

thread = threading.Thread(target=rclpy.spin, args=(node, ), daemon=True)
thread.start()
rate = node.create_rate(1.0)

try:
    while rclpy.ok():

        # Axis:
        # Publish an axis using a ROS Pose Msg
        P = Pose(position=Point(x=0,y=0,z=0),orientation=Quaternion(x=0,y=0,z=0,w=1))
        axis_length = 0.4
        axis_radius = 0.05
        markers.publishAxis(P, axis_length, axis_radius, 5.0) # pose, axis length, radius, lifetime

        # Line:
        # Publish a line between two ROS Point Msgs
        point1 = Point(x=-2.0,y=1.0)
        point2 = Point(x=2.0,y=1.0) 
        width = 0.05
        markers.publishLine(point1, point2, 'random', width, 5.0) # point1, point2, color, width, lifetime

        # Path:
        # Publish a path using a list of ROS Point Msgs
        path = []
        path.append( Point(x=0.0,y=-0.5,z=0.0) )
        path.append( Point(x=1.0,y=-0.5,z=0.0) )
        path.append( Point(x=1.5,y=-0.2,z=0.0) )
        path.append( Point(x=2.0,y=-0.5,z=0.0) )
        path.append( Point(x=2.5,y=-0.2,z=0.0) )
        path.append( Point(x=3.0,y=-0.5,z=0.0) )
        path.append( Point(x=4.0,y=-0.5,z=0.0) )
        width = 0.02
        markers.publishPath(path, 'random', width, 5.0) # path, color, width, lifetime

        # Polygon:

        # Publish a polygon using a ROS Polygon Msg
        polygon = Polygon()
        polygon.points.append( Point(x=0.0,y=-1.0,z=0.0) )
        polygon.points.append( Point(x=0.0,y=-2.0,z=0.0) )
        polygon.points.append( Point(x=-1.0,y=-2.0,z=0.0) )
        polygon.points.append( Point(x=-1.0,y=-1.0,z=0.0) )
        markers.publishPolygon(polygon, 'random', 0.02, 5.0) # path, color, width, lifetime

        # Text:

        # Publish some text using a ROS Pose Msg
        P = Pose(position=Point(x=3.0,y=-1.0,z=1.5))
        scale = Vector3(x=0.2,y=0.2,z=0.2)
        markers.publishText(P, 'RViz Tool Python ROS2', 'random', scale, 5.0) # pose, text, color, scale, lifetime

        # Arrow:    
        # Publish an arrow using a ROS Pose Msg       
        P = Pose(position=Point(x=1.0, y=-2.0))
        arrow_length = 2.0  # single value for length (height is relative)        
        markers.publishArrow(P, 'random', arrow_length, 5.0)

        # Cube / Cuboid:       
        # Publish a cube using a ROS Pose Msg
        P = Pose(position=Point(x=-2.0,y=0.0,z=0.0))
        cube_width = 0.6
        markers.publishCube(P, 'random', cube_width, 5.0) # pose, color, cube_width, lifetime
        
        # Sphere:       
        # Publish a sphere using a ROS Pose
        P = Pose(position=Point(x=-2.0,y=-1.0,z=0.0))
        scale = Vector3(x=0.6,y=0.6,z=0.6) # diameter        
        markers.publishSphere(P, 'random', scale, 5.0) # pose, color, scale, lifetime
        
        # Cylinder: 
        # Publish a cylinder using a ROS Pose
        P = Pose(position=Point(x=-2.0,y=-2.0,z=0.0))
        markers.publishCylinder(P, 'random', 1.0, 0.5, 5.0) # pose, color, height, radius, lifetime
      
        # Model mesh:
        # Publish STL mesh of box, colored green
        P = Pose(position=Point(x=3.0,y=1.0,z=0.0))
        scale = Vector3(x=1.5,y=1.5,z=1.5)
        mesh_file1 = "package://rviz_tools_package/meshes/box_mesh.stl"
        markers.publishMesh(P, mesh_file1, 'random', scale, 5.0) # pose, mesh_file_name, color, mesh_scale, lifetime

        # Display STL mesh of bottle, re-scaled to smaller size
        P = Pose(position=Point(x=4.0,y=1.0,z=0.0))
        scale = Vector3(x=0.6,y=0.6,z=0.6)
        mesh_file2 = "package://rviz_tools_package/meshes/fuze_bottle_collision.stl"
        markers.publishMesh(P, mesh_file2, 'random', scale, 5.0) # pose, mesh_file_name, color, mesh_scale, lifetime

        # Display collada model with original texture (no coloring)
        P = Pose(position=Point(x=4.0,y=-1.5,z=0.0))
        mesh_file3 = "package://rviz_tools_package/meshes/fuze_bottle_visual.dae"
        mesh_scale = 4.0
        markers.publishMesh(P, mesh_file3, None, mesh_scale, 5.0) # pose, mesh_file_name, color, mesh_scale, lifetime

        rate.sleep()

except KeyboardInterrupt:
    pass
