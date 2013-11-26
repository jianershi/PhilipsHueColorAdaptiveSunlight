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
	try:
		response=requests.post(myUrl,data=json.dumps(payload))
		print response
	except:
		print ("connection error")
		
	sleep(60)


