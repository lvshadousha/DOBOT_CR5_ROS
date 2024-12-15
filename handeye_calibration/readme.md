this launch file control the intel realsense camera and dobot cr5 robot arm.

%launch the calibration program.启动标定程序

%Refering the readme in TCP-IP-ROS-6AXis and add dobot_control panel in rviz interface and enable the robot.The longest valid step of RRT should be changed to 0.0005 or less 
because of vibration of the robot.参考TCP-IP-ROS-6AXis中的readme添加dobotcontrol面板,RRT步长修改为0.0005或更小

roslaunch /your_path/src/easy_handeye/docs/example_launch/cr5_realsense_calibration.launch

roslaunch dobot_bringup bringup.launch robot_ip:=192.168.5.1

roslaunch dobot_moveit moveit.launch

roslaunch realsense2_camera rs_camera.launch

Publish the calibration result which is a tf

%Change the path of calibration result in the publish.launch file to path you save the calibration result.

roslaunch /home/lvdousha/catkin_ws/src/easy_handeye/easy_handeye/launch/publish.launch
