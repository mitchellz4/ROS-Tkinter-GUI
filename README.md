# Smart_AG GUI

This GUI was developed for our Bramblebee robot, it is a Husky base from Clear Path Robotics with a custom built platform on top of it that has a full computer, ZED 2I, Realsense Camera, Velodyne Lidar, PixyPro 180 Degree Camera, and a GPS Antenna. 

The GUI was coded in Python3 and the Tkinter GUI Package was used as well.

## Dependencies

Ubuntu 18.04 

ROS Melodic 

Tkinter (GUI)

```
sudo apt install -y python3-pip
apt-get install python-tk
```
XdoTool
```

sudo apt-get update -y
sudo apt-get install -y xdotool

```

## Downloading GUI

```
cd ~/(CATKIN_WS)/src
git clone ----
cd ..
catkin_make
#####This Git was meant to be used with our robot so there are other packages related to the husky robot, and the other sensors/cameras
 ```
 
# How to change the code and use on your own robot
