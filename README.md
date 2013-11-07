#Philips Hue Color Adaptive Sunlight

This is an attempt to get the philips hue light change color temperature when the sunrise and sunset. Same as [f.lux](http://justgetflux.com)

It should work with the official API but I used the [Philips Hue Remote API](https://github.com/jarvisinc/PhilipsHueRemoteAPI) for development so I don't have to limit the server on local network.

It uses weather underground API to get the sunrise and sunset time so you need their API key. Provide your location ZIP code and it should determine the sunrise and sunset time automatically.

##Developing Progress
Main functioanlity is pretty much done. Now need to write the main python file to spin up two threads