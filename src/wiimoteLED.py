#!/usr/bin/env python

from wiimote.msg import State
from std_msgs.msg import String
import rospy
pub = rospy.Publisher('rocket_command',String)

def control_rocket(command):
	#print command
	pub.publish(command)


def callback(msg):
	#print '>>> ',msg.ir_tracking
	#print msg.nunchuk_joystick_zeroed# UP = 0,1 DOWN = 0,-1 LEFT = 1,0 Right = -1,0
	#print msg.nunchuk_joystick_raw
	#print msg.MSG_BTN_UP
	#print msg.MSG_CLASSIC_BTN_UP
	
	x,y = msg.nunchuk_joystick_zeroed

	if msg.buttons[6] or y > 0:
		control_rocket('up')
	elif msg.buttons[7] or y < 0:
		control_rocket('down')
	elif msg.buttons[8] or x > 0:
		control_rocket('left')
	elif msg.buttons[9] or x < 0:
		control_rocket('right')
	elif msg.buttons[5] or msg.nunchuk_buttons[0]:
		control_rocket('fire')
	else:
		control_rocket('stop') 
	

def wii_control():
	rospy.init_node('wii_listener', anonymous=True)
	rospy.Subscriber("/wiimote/state",State,callback);	
	rospy.spin()

if __name__ == '__main__':
	wii_control()



'''
State.INVALID                         State.MSG_BTN_UP                      State.MSG_CLASSIC_BTN_Y               State.linear_acceleration_zeroed
State.INVALID_FLOAT                   State.MSG_BTN_Z                       State.MSG_CLASSIC_BTN_ZL              State.mro
State.LEDs                            State.MSG_CLASSIC_BTN_A               State.MSG_CLASSIC_BTN_ZR              State.nunchuk_acceleration_raw
State.MSG_BTN_1                       State.MSG_CLASSIC_BTN_B               State.angular_velocity_covariance     State.nunchuk_acceleration_zeroed
State.MSG_BTN_2                       State.MSG_CLASSIC_BTN_DOWN            State.angular_velocity_raw            State.nunchuk_buttons
State.MSG_BTN_A                       State.MSG_CLASSIC_BTN_HOME            State.angular_velocity_zeroed         State.nunchuk_joystick_raw
State.MSG_BTN_B                       State.MSG_CLASSIC_BTN_L               State.buttons                         State.nunchuk_joystick_zeroed
State.MSG_BTN_C                       State.MSG_CLASSIC_BTN_LEFT            State.deserialize                     State.percent_battery
State.MSG_BTN_DOWN                    State.MSG_CLASSIC_BTN_MINUS           State.deserialize_numpy               State.raw_battery
State.MSG_BTN_HOME                    State.MSG_CLASSIC_BTN_PLUS            State.errors                          State.rumble
State.MSG_BTN_LEFT                    State.MSG_CLASSIC_BTN_R               State.header                          State.serialize
State.MSG_BTN_MINUS                   State.MSG_CLASSIC_BTN_RIGHT           State.ir_tracking                     State.serialize_numpy
State.MSG_BTN_PLUS                    State.MSG_CLASSIC_BTN_UP              State.linear_acceleration_covariance  State.zeroing_time
State.MSG_BTN_RIGHT                   State.MSG_CLASSIC_BTN_X               State.linear_acceleration_raw         
'''
