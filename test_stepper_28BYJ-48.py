# Test the 28BYJ-48 stepper

import time
import stepper_28BYJ48

# Create the stepper object
stepper = stepper_28BYJ48.Stepper(10, 11, 12, 13)

# Move forwards and backwards
numSteps = 100
stepper.forward(numSteps)
stepper.backward(numSteps)
stepper.halfStepForward(numSteps)
stepper.halfStepBackward(numSteps)
