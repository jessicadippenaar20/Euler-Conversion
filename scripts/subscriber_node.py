#!/usr/bin/env python

import rospy 
from std_msgs.msg import String
from euler_to_quarternion.msg import quarternion_conversion

def callback(data):
    rospy.loginfo("%s X: %f Y: %f Z: %f, W: %f", data.message, data.x, data.y, data.z, data.w)

def listener():
    rospy.init_node('subsciber_node', anonymous=True)
    rospy.Subscriber('output', quarternion_conversion, callback)
    rospy.spin()
    


if __name__ == '__main__': 
    try: 
        listener()
    except rospy.ROSInterruptException:
        pass