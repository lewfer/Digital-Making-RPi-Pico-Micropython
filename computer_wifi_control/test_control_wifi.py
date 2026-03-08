# Template code to control a RPi Pico robot over a Wifi network 

import network
import time

# Specify the IP address of your robot
HOST = "192.168.178.50" 

# Specify the port number to send messages on
PORT = 5000

# Create a network object
net = network.Network()

# Set up a message sender
net.createSender(HOST, PORT)

# Send messages to drive the robot forward for 2 seconds then stop
net.sendMessage("on")
time.sleep(2)
net.sendMessage("off")
