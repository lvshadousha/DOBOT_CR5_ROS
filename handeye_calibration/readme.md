这个启动文件控制英特尔 RealSense 相机和 DOBOT CR5 机器人手臂。

启动标定程序：

1. 参考 TCP-IP-ROS-6AXis 中的 README，添加 dobot_control 面板到 RViz 界面并启用机器人。由于机器人的振动，将 RRT 的最长有效步长修改为 0.0005 或更小。

2. 启动标定程序：
   ```bash
   roslaunch /your_path/src/easy_handeye/docs/example_launch/cr5_realsense_calibration.launch
   ```

3. 启动 DOBOT：
   ```bash
   roslaunch dobot_bringup bringup.launch robot_ip:=192.168.5.1
   ```

4. 启动 MoveIt：
   ```bash
   roslaunch dobot_moveit moveit.launch
   ```

5. 启动 RealSense 相机：
   ```bash
   roslaunch realsense2_camera rs_camera.launch
   ```

发布标定结果（一个 tf）：

1. 在 publish.launch 文件中将标定结果的路径更改为保存标定结果的路径。
   ```bash
   roslaunch /home/lvdousha/catkin_ws/src/easy_handeye/easy_handeye/launch/publish.launch
   ```
```
