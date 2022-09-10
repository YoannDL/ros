#!/usr/bin/env python3

import roslib; roslib.load_manifest('visualization_marker_tutorials')
from visualization_msgs.msg import Marker
from visualization_msgs.msg import MarkerArray
from geometry_msgs.msg import PoseStamped, Pose, Point
import rospy
import std_msgs.msg
import math



rospy.init_node('rviz_pose')
# create PoseStamped
pose = PoseStamped()
pub = rospy.Publisher("/visualization_walk", PoseStamped, queue_size = 2)
pose.header = std_msgs.msg.Header()
pose.header.stamp = rospy.Time.now()
pose.header.frame_id = "map" 
pose.pose = Pose()
pose.pose.position.x = 2 #  kinect Z value, [2], is X in TF of camera_link
pose.pose.position.y = 2 # kinect X value, [0], is -Y in TF of camera_link
pose.pose.position.z = 0  # kinect Y value, [1], is -Z in TF of camera_link

pose.pose.orientation.x = 0
pose.pose.orientation.y = 0
pose.pose.orientation.z = 0
pose.pose.orientation.w = 1
    # send PoseStamped
    

while not rospy.is_shutdown():



   # Publish the MarkerArray
  pub.publish(pose)

   

  rospy.sleep(0.01)
