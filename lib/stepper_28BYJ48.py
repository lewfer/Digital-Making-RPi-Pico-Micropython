# Class to drive the 28BYJ-48 stepper
# When making full steps, there are 2048 steps in a full 360 degree turn
# When making half steps, there are 4096 steps in a full 360 degree turn


import machine
import time

# Encode the step sequences (i.e. which pins fire)

full_step_sequence = [
    [1,1,0,0],
    [0,1,1,0],
    [0,0,1,1],
    [1,0,0,1]
]

half_step_sequence = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]

# Stepper class
# Provide the GPIO pin numbers in1, in2, in3, in4
class Stepper:
    def __init__(self, in1, in2, in3, in4):

        self.pins = [
            machine.Pin(10, machine.Pin.OUT),
            machine.Pin(11, machine.Pin.OUT),
            machine.Pin(12, machine.Pin.OUT),
            machine.Pin(13, machine.Pin.OUT)]

    def forward(self, numSteps):
        for i in range(numSteps):
            for step in full_step_sequence:
                for i in range(len(self.pins)):
                    self.pins[i].value(step[i])
                    time.sleep(0.001)

    def backward(self, numSteps):
        for i in range(numSteps):
            for step in reversed(full_step_sequence):
                for i in range(len(self.pins)):
                    self.pins[i].value(step[i])
                    time.sleep(0.001)         

    def halfStepForward(self, numSteps):
        for i in range(numSteps):
            for step in half_step_sequence:
                for i in range(len(self.pins)):
                    self.pins[i].value(step[i])
                    time.sleep(0.001)

    def halfStepBackward(self, numSteps):
        for i in range(numSteps):
            for step in reversed(half_step_sequence):
                for i in range(len(self.pins)):
                    self.pins[i].value(step[i])
                    time.sleep(0.001)        

