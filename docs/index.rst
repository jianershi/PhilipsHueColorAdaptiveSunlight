Philips Hue Color Adaptive Sunlight Documentation
===============================================================

Philips Hue light will change color temperature at sunrise and sunset. Same as f.lux did.

I used the Philips Hue Remote API for development so I don't have to limit the server on local network. Official API should work as well with little change.

I used Weather Underground API to get the sunrise and sunset time so you need its API key. Provide your location ZIP code and it should determine the sunrise and sunset time automatically.

The current version will change color instantaneously. I probably should add the functioanlity of changing gradually in the future.

.. toctree::
   :maxdepth: 2

.. automodule:: colorChange
   :members:
   :undoc-members:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
