#!/usr/bin/env python

import rospy 
from std_msgs.msg import String, Float32 
from geometry_msgs.msg import Quaternion
from tf.transformations import *
from euler_to_quarternion.msg import quarternion_conversion

#Define global variables:
roll = pitch = yaw = 0.0



#Define functions called in main here:


def get_rotation():
    global roll, pitch, yaw
    roll = input("Enter first Euler angle: ")
    pitch = input("Enter second Euler angle: ")
    yaw = input("Enter third Euler angle: ")     

def talk_to_me():
    pub = rospy.Publisher('output', quarternion_conversion, queue_size=1)
    rospy.init_node('converter_node', anonymous=True)
    rate = rospy.Rate(1)
    rospy.loginfo("converter_node started, now publishing messages") 
    while not rospy.is_shutdown():
        msg = quarternion_conversion() 
        msg.message = "The converted Quarternion is: "
        msg.x = q[0]
        msg.y = q[1]
        msg.z = q[2]
        msg.w = q[3]
        pub.publish(msg)
        rate.sleep()

#Main Program Here
if __name__ == '__main__': 
    #Call function for user input 
    get_rotation()

    #convert to quaternion
    q = quaternion_from_euler(roll, pitch, yaw)
    #print("The quaternion representation is %2s %s %s %s." % (q[0], q[1], q[2], q[3]))


    try: 
        talk_to_me()
    except rospy.ROSInterruptException:
        pass

#to do: write a publisher that shows the output of the conversion (convert_euler_to_quartonion())
#       create a launch file for both nodes (and roscore)