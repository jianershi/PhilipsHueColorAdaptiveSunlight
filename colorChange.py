from flask import Flask
import requests
import datetime
from config import *

app = Flask(__name__)

@app.route("/")
def hello():
    return setMode()



def getSunInfo():
	url = "http://api.wunderground.com/api/"+weatherUnderGroundAPIKey+"/astronomy/q/"+zipCode+".json"
	print url
	r = requests.get(url)
	print r.status_code
	print r.text
	rjson = r.json()
	sunrise_h = rjson['sun_phase']['sunrise']['hour']
	sunrise_m = rjson['sun_phase']['sunrise']['minute']
	sunset_h = rjson['sun_phase']['sunset']['hour']
	sunset_m = rjson['sun_phase']['sunset']['minute']
	print "sunrise at {}:{}".format(sunrise_h,sunrise_m)
	print "sunrset at {}:{}".format(sunset_h,sunset_m)
	print "recontruct time"
	currenttime = datetime.datetime.now();
	# currenttime=currenttime.replace(day=7)
	# print currenttime
	# currenttime.hour = sunrise_h
	# currenttime.minute = sunrise_m
	# print "sunrise time {}".format(currenttime)
	# sunrise = datetime.time(int(sunrise_h),int(sunrise_m))

	#this makes sure that the time frame is always constructed form today's date
	reconstructed_sunrise_time = datetime.datetime(currenttime.year, currenttime.month, currenttime.day, int(sunrise_h), int(sunrise_m))
	reconstructed_sunset_time = datetime.datetime(currenttime.year, currenttime.month, currenttime.day, int(sunset_h), int(sunset_m))
	# testime = datetime.datetime(currenttime.year, currenttime.month, 7, 0, 0)
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

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)