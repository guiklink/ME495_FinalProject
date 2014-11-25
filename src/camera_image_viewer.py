#!/usr/bin/env python
import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from geometry_msgs.msg import Point


class Vision_Node:
	def __init__(self):
		self.bridge = CvBridge()
		self.cv_window_name = 'OpenCV Image'

	def callback(self,raw_image):
		tmp	= self.bridge.imgmsg_to_cv2(raw_image, desired_encoding="bgr8")
		cv2.imshow(self.cv_window_name,tmp)

	def listener(self):
		rospy.init_node('visionTest', anonymous=True)
		rospy.Subscriber("/camera_node/image_raw",Image,self.callback);
		rospy.sleep(100)
		rospy.spin()

if __name__ == '__main__':
	vision = Vision_Node()
	vision.listener() 
