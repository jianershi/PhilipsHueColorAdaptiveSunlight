from colorChange import *
from time import sleep
from config import myUrl
import json
import requests

myColorChange = ColorTemperatureChange();

while (1):

	whichMode = myColorChange.setHueMode()
	ct = myColorChange.getColorTemperature(whichMode)

	payload = {'colormode': 'ct', 'ct': ct}
	response=requests.post(myUrl,data=json.dumps(payload))

	print response
	sleep(60)


