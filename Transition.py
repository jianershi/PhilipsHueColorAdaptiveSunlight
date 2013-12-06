from colorChange import *
from time import sleep
from config import myUrl, steps
import json
import requests

class Transition:
	"""
	this class handles the color transition
	"""

	def __init__(self):
		self.myColorChange = ColorTemperatureChange()
		self.previousMode = 'hi'

	def sendOnePayload(self, ct):
		"""
		This method actually send out control message

        :type ct: int
        :param ct: color temperature

		"""
		payload = {'colormode': 'ct', 'ct': ct}
		try:
			response=requests.put(myUrl,data=json.dumps(payload))
			print response
		except:
			print ("connection error")

	def determineState(self):
		"""
		
		This method is called to send a control message, 
		it will determine whether color transtion is needed.
		If so, it initiate the color transtion method.
		It not, it will still send out control message

		"""
		whichMode = self.myColorChange.setHueMode()
		if whichMode != self.previousMode:
			self.startTransition(steps,self.previousMode,whichMode)
			self.previousMode = whichMode
		else:
			#still needs to transit, because light may be turned on at that point.
			final_ct = self.myColorChange.getColorTemperature(whichMode)
			self.sendOnePayload(final_ct)
			print ("Final CT: {}").format(final_ct)

	def startTransition(self,steps,initialMode,finalMode):
		"""
		Handle the actual transition sequence

		:type steps: int
		:param steps: how many steps will the transtion take. Each step = 2 sec
		:type initialMode: str
		:param initialMode: 'hi' or 'low'
		:type finalMode: str
		:param finalMode: 'hi' or 'low'
		
		"""

		#Calculate steps
		ct_init = self.myColorChange.getColorTemperature(initialMode);
		ct_final = self.myColorChange.getColorTemperature(finalMode);

		print ("Transit from {} to {}").format(ct_init,ct_final);

		#break transition down to steps
		perStep = 1.0 * (ct_final - ct_init) / steps; #1.0 is to convert the whole thing from integer to double
		ct_list = []
		for i in range(0,int(steps)-1):
			ct_list.append(int(ct_init+perStep*i))

		print (ct_list) #debug

		#issue transition command
		for i in range(0,int(steps)-1):
			self.sendOnePayload(ct_list[i]);
			print ("Current CT: {}").format(ct_list[i]);
			sleep(2)

		#transition complete