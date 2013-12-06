from Transition import *
from time import sleep

# Create an instance of ColorTemperatureChange
aTransition = Transition()

while (1):
	aTransition.determineState()
	sleep(1)


