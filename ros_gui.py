#!/usr/bin/env python2



import subprocess
import time
from tkinter import *

import rospy
from std_msgs.msg import Int16
from geometry_msgs.msg import Twist



# Used in the subprocess call as stdout, output stream value which is nothing in this case.
windowid1 = ''


# This will launch the base, imu, and teleop controls
# Change Roslaunch to what your launch file is

def ControllerCommand():
	global windowid1
    # Subprocess is used to run new processes such as in this opening a terminal window and launching file
	subprocess.call(["xdotool", "windowfocus", windowid1])
	time.sleep(.1)
	subprocess.call(["xdotool", "key", "alt+1"])
	time.sleep(.1)
	subprocess.check_output(["xdotool", "type", "roslaunch hardwarelaunch controller.launch" + "\n"])

# This launches the GPS
def GPSCommand():
	global windowid1
	subprocess.call(["xdotool", "windowfocus", windowid1])
	time.sleep(.1)
	subprocess.call(["xdotool", "key", "alt+2"])
	time.sleep(.1)	
	subprocess.check_output(["xdotool", "type", "roslaunch hardwarelaunch gps.launch" + "\n"])

# THis launches the Realsense
def RealsenseCommand():
	global windowid1
	subprocess.call(["xdotool", "windowfocus", windowid1])
	time.sleep(.1)
	subprocess.call(["xdotool", "key", "alt+3"])
	time.sleep(.1)	
	subprocess.check_output(["xdotool", "type", "roslaunch realsense2_camera rs_camera.launch tf_prefix:=realsense" + "\n"])

# Will launch a rosbag that records all data, change this to where you want the file to go
def RosbagCommand():
	global windowid1
	subprocess.call(["xdotool", "windowfocus", windowid1])
	time.sleep(.1)
	subprocess.call(["xdotool", "key", "alt+4"])
	time.sleep(.1)	
	subprocess.check_output(["xdotool", "type", "rosbag record --split 20024 -o /media/bramblebee/smartag/2022-Data/WVU_Organic_Farm_Trip2_2022-07-22/ -a" + "\n"])


def callback_cmd_vel(msg):
	global cmd_vel_speed
	cmd_vel_speed.set(msg.linear.x)

rospy.Subscriber("/husky_velocity_controller/cmd_vel", Twist, callback_cmd_vel)

# IMU Sub
def callback_imu(data):
	global imu_status
	imu_status.set(data.data)

rospy.Subscriber("/zed2i/zed_node/imu/data", Int16, callback_imu)



## Plans to add RVIZ, IMU Subscriber, Realsense image view, ZED Image View ## -----------------------------------------------



#Create the GUI window

# Initializing the interpreter and root window
root = Tk()
# Makes the GUI window the maximum size of the screen
width = root.winfo_screenwidth()
height = root.winfo_screenwidth()
root.geometry("%dx%d" % (width, height))
# Title of the window when opening, can be changed to whatever you want
root.title('Bramblebee GUI')
# Allows the angle and speed value to be put on the main window
cmd_vel_angle = DoubleVar()
cmd_vel_speed = DoubleVar()
callback_imu = IntVar()
# The main frame
frame = Frame(root)
frame.pack()

# Build subframes into the main GUI frame

# This frame is used for the Launch Command Buttons
frame0 = Frame(frame)
# This frame is used for the cmd vel windows
frame01 = Frame(frame,borderwidth=2,relief=RAISED)


# Indicate where you want the frames to be oriented
frame0.pack(side = TOP)
frame01.pack(side = TOP)


# Create buttons
b1 = Button(frame0, text="Start Controller", command=ControllerCommand)
b1.pack(side=BOTTOM)
b2 = Button(frame0, text="GPS Controller",command=GPSCommand)
b2.pack(side=LEFT)
b3 = Button(frame0, text="Realsense Camera",command=RealsenseCommand)
b3.pack(side=LEFT)
b4 = Button(frame0, text="Rosbag",command=RosbagCommand)
b4.pack(side=LEFT)

# Create text windows for cmd values
frameE5 = Frame(frame01)
frameE6 = Frame(frame01)
frameE7 = Frame(frame01)
frameE5.pack(side = LEFT)
frameE6.pack(side = LEFT)
frameE7.pack(side = LEFT)

# Labels for the the cmd boxes
label5 = Label(frameE5,text="cmd_speed")
label6 = Label(frameE6,text="cmd_angle")
label7 = Label(frameE7,text="IMU" )
label5.pack(side=TOP)

label7.pack(side=TOP)

# Values for the cmd labels
e5 = Label(frameE5, textvariable=cmd_vel_speed, width = 10,justify=RIGHT)
e5.pack(side=RIGHT)

e7 = Label(frameE7, textvariable=callback_imu, width = 10, justify=RIGHT)
e7.pack(side=RIGHT)

# Opens 4 Terminal windows, with a .1 second delay in between each of them
subprocess.call(["xdotool", "windowmove", "20", "20"])
time.sleep(.1)

# This is what file path each terminal will open in, change this based on your system
working_directory1 = "--working-directory=/home/mitchell"

# Calls the first terminal with gnome-terminal command, and the geometry is the size of the terminal window, working directory is the path each terminal will be in
subprocess.call(["xdotool", "exec", "gnome-terminal", "--geometry=600x600+450+20", working_directory1])
time.sleep(.5)
# 1st Terminal - alt+1
subprocess.call(["xdotool", "key", "ctrl+shift+t"])
time.sleep(.1)
# 2nd Terminal - alt+2
subprocess.call(["xdotool", "key", "ctrl+shift+t"])
time.sleep(.1)
# 3rd Terminal - alt+3
subprocess.call(["xdotool", "key", "ctrl+shift+t"])
time.sleep(.1)  
windowid1 = subprocess.check_output(["xdotool", "getactivewindow"])
print("windowid1", windowid1.decode(), windowid1)
subprocess.call(["xdotool", "windowmove", windowid1.decode(), "50", "575"]) 
time.sleep(.1)


root.mainloop()



