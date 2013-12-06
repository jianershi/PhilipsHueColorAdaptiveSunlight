#Philips Hue Color Adaptive Sunlight

Philips Hue light will change color temperature at sunrise and sunset. Same as [f.lux](http://justgetflux.com) did.

I used the [Philips Hue Remote API](https://github.com/jarvisinc/PhilipsHueRemoteAPI) for development so I don't have to limit the server on local network. Official API should work as well with little change.

I used [Weather Underground API](http://www.wunderground.com/weather/api/) to get the sunrise and sunset time so you need its API key. Provide your location ZIP code and it should determine the sunrise and sunset time automatically.

##Setup
configure ```config.py``` using ```config.py.sample``` as an example
You will need [Weather Underground API](http://www.wunderground.com/weather/api/) to get it working.

##Run
Setup up Virtual Environment

```
virtualenv ev
source ev/bin/activate
```

Install Dependencies

```
pip install -r requirements.txt
```

Run :)

```
python main.py
```

Enjoy ~

##Documentation
For up to date documentation, refer to the docs/_build folder

##Story
[http://blog.paulshi.me/technical/2013/12/05/Philips-Hue-Color-Adaptive-Sunlight.html](http://blog.paulshi.me/technical/2013/12/05/Philips-Hue-Color-Adaptive-Sunlight.html)

##License
```
The MIT License (MIT)

Copyright (c) 2013 Jianer Shi (hipaulshi@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

```

[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/paulshi/philipshuecoloradaptivesunlight/trend.png)](https://bitdeli.com/free "Bitdeli Badge")