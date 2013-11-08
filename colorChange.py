import requests
import datetime
from config import *

def getColorTemperature(mode):
	# max range of philip hue color temperature setting
	maxRangeVal = 153.0
	minRangeVal = 500.0
	# which corresponds to
	maxRange = 6500.0 #K
	minRange = 2000.0 #K
	# My Setting 
	morningRange = 6500.0 #K
	nightRange = 3400.0 #K

	perKValueChnage = (abs(maxRangeVal -  minRangeVal) / abs(maxRange - minRange))
	myMorningVal = maxRangeVal + perKValueChnage*(maxRange - morningRange)
	myNightVal =  minRangeVal + perKValueChnage*(minRange - nightRange)

	# print int(myMorningVal)
	# print int(myNightVal)

	if mode == "hi":
		return int(myMorningVal)
	elif mode == "low":
		return int(myNightVal)
	else:
		return -1

def getSunInfo():
	url = "http://api.wunderground.com/api/"+weatherUnderGroundAPIKey+"/astronomy/q/"+zipCode+".json"
	# print url
	r = requests.get(url)
	# print r.status_code
	# print r.text
	rjson = r.json()
	sunrise_h = rjson['sun_phase']['sunrise']['hour']
	sunrise_m = rjson['sun_phase']['sunrise']['minute']
	sunset_h = rjson['sun_phase']['sunset']['hour']
	sunset_m = rjson['sun_phase']['sunset']['minute']
	currenttime = datetime.datetime.now();

	#this makes sure that the time frame is always constructed form today's date
	reconstructed_sunrise_time = datetime.datetime(currenttime.year, currenttime.month, currenttime.day, int(sunrise_h), int(sunrise_m))
	reconstructed_sunset_time = datetime.datetime(currenttime.year, currenttime.month, currenttime.day, int(sunset_h), int(sunset_m))
	print "sunrise time: {}".format(reconstructed_sunrise_time)
	print "sunset time: {}".format(reconstructed_sunset_time)
	print "current time: {}".format(currenttime)

	flagA = currenttime > reconstructed_sunrise_time
	flagB =  currenttime > reconstructed_sunset_time

	if flagA and not flagB:
		return 1
	elif flagA and flagB:
		return 0
	elif not flagA and not flagB:
		return 0
	else:
		return -1
	
def setMode():
	SunInfo = getSunInfo()
	if SunInfo==1:
		return "hi"
	elif SunInfo == 0:
		return "low"
	else:
		return "time logic error!"
