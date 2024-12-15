#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import PoseStamped
from nav_msgs.msg import Odometry
from tf.transformations import quaternion_from_euler

def pose_callback(msg):
    # 从PoseStamped消息中获取位姿数据
    position = msg.pose.position#!/usr/bin/env python3

import rospy
import tf
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Pose, Twist
from tf2_msgs.msg import TFMessage

def tf_callback(msg, odom_pub):
    # 假设 msg 是订阅到的 TF 消息，直接处理
    for transform in msg.transforms:
        if transform.child_frame_id == "/camera_link":
            # 获取位置和旋转信息
            position = transform.transform.translation
            rotation = transform.transform.rotation

            # 创建 Odometry 消息
            odom = Odometry()
            odom.header.stamp = rospy.Time.now()
            odom.header.frame_id = 'base_link'  # 使用 base_link 作为参考坐标系

            # 填充位姿信息
            odom.pose.pose.position.x = position.x
            odom.pose.pose.position.y = position.y
            odom.pose.pose.position.z = position.z
            odom.pose.pose.orientation = rotation

            # 可选：根据需要填充速度信息
            odom.twist.twist = Twist()  # 如果有速度数据，可以在此填充

            # 发布 Odometry 消息
            odom_pub.publish(odom)

def publish_odometry_from_tf():
    rospy.init_node('camera_odometry_publisher', anonymous=True)
    
    # 发布 Odometry 消息
    odom_pub = rospy.Publisher('/odom', Odometry, queue_size=10)
    
    # 订阅 /tf 话题
    tf_sub = rospy.Subscriber('/tf', TFMessage, tf_callback, odom_pub)
    
    rospy.spin()

if __name__ == "__main__":
    try:
        publish_odometry_from_tf()
    except rospy.ROSInterruptException:
        pass

    orientation = msg.pose.orientation
    
    # 将四元数转换为欧拉角（如果需要）
    # roll, pitch, yaw = euler_from_quaternion([orientation.x, orientation.y, orientation.z, orientation.w])
    
    # 创建一个里程计消息
    odom = Odometry()
    
    # 设置里程计的header
    odom.header.stamp = rospy.Time.now()
    odom.header.frame_id = "odom"  # 参考坐标系可以设置为odom
    
    # 设置里程计的位置信息
    odom.pose.pose.position = position
    odom.pose.pose.orientation = orientation
    
    # 设置里程计的速度信息（根据实际需求更新速度，这里设置为零）
    odom.twist.twist.linear.x = 0.0
    odom.twist.twist.linear.y = 0.0
    odom.twist.twist.linear.z = 0.0
    odom.twist.twist.angular.x = 0.0
    odom.twist.twist.angular.y = 0.0
    odom.twist.twist.angular.z = 0.0

    # 发布里程计消息
    odom_pub.publish(odom)

def main():
    rospy.init_node('camera_to_odometry', anonymous=True)

    # 订阅位姿消息
    rospy.Subscriber('/camera_link/pose', PoseStamped, pose_callback)

    # 创建里程计发布者
    global odom_pub
    odom_pub = rospy.Publisher('/camera_odom', Odometry, queue_size=10)

    rospy.loginfo("Camera to Odometry node started.")
    
    # 循环处理回调
    rospy.spin()

if __name__ == '__main__':
    main()
