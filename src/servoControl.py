#!/usr/bin/env python

import serial
import rospy
from geometry_msgs.msg import Point

port = serial.Serial("/dev/ttyACM0", 9600)
servo0 = 1500.0
servo5 = 1500.0
inc = 30

print port

def servo_test(channel):
	while True:

		n = input('Enter the number: ')
		target = n * 4
		print 'Target = ',target

		inst = [0] * 4
		inst[0] = 0x84  
		inst[1] = channel
		inst[2] = target & 0x7F
		inst[3] = (target >> 7) & 0x7F

		print 'Instructions = ',inst

		#instchr = map(chr,inst)
		#print 'Instructions CHR = ',instchr
		#msn = ''.join(instchr) 
		#print 'Serial MSN = ',msn
		#port.write(msn)

		port.write(''.join(map(chr,inst)))
	
		raw_input('Press a key to continue')
		print '------------------------------\n'
	
def move_servo(channel,n):
	target = n * 4

	inst = [0] * 4
	inst[0] = 0x84  
	inst[1] = channel
	inst[2] = target & 0x7F
	inst[3] = (target >> 7) & 0x7F
	port.write(''.join(map(chr,inst)))

def clamp(x):
	if x > 2000:
		return 2000 
	elif x < 992:
		return 992
	else:
		return x


def adjustCamera(x,y):
	global servo0,servo5,inc

	kp = 0.3

	servo0 = clamp(servo0 + kp * x)
	servo5 = clamp(servo5 - kp * y)

	move_servo(0,int(servo0))
	move_servo(5,int(servo5))
	'''if x > 0:
		servo0 = clamp(servo0 + inc)
		move_servo(0,servo0)
	if x < 0:
		servo0 = clamp(servo0 - inc)
		move_servo(0,servo0)
	if y > 0:
		servo5 = clamp(servo5 - inc)
		move_servo(5,servo5)
	if y < 0:
		servo5 = clamp(servo5 + inc)
		move_servo(5,servo5)'''

def callback(p):
	#print p
	x = p.x - 640/2
	y = p.y - 480/2
	adjustCamera(x,y)

def servoCore():
	rospy.init_node('listener2', anonymous=True)
	rospy.Subscriber("/ball_center",Point,callback);	
	rospy.spin()

if __name__ == '__main__':
	servoCore()
	
