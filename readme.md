
What is this?
=============

This is the source code for an "insulting"-machine. 
The machine is based on a raspberry pi and additional hardware by [tinkerforge](http://www.tinkerforge.de).
By pressing a button you can trigger a random sound file. The pre-generated sound files which are included in 
the source are german insults.
The source includes a python script which can generate sound files from a JSON-List of words using the speech
synthesis tools on a mac. This can be used to generate your own insults. 

Hardware
========

* Raspberry Pi
* SD Card
* https://www.tinkerforge.com/de/shop/bricks/master-brick.html
* https://www.tinkerforge.com/de/shop/bricklets/io4-bricklet.html
* https://www.tinkerforge.com/de/shop/power-supplies/step-down-power-supply.html
* https://www.tinkerforge.com/de/shop/bricklets/human-input/rotary-poti-bricklet.html (2x)
* https://www.tinkerforge.com/de/shop/bricklets/human-input/motion-detector-bricklet.html  
* Power Supply 5V
* Speaker
 

Installation
============

* Download Hypriot SD card image for Raspberry Pi. Contains Raspbian with Docker pre-installed. http://blog.hypriot.com/downloads/
* Flash SD Card. http://blog.hypriot.com/getting-started-with-docker-on-your-arm-device/
* Start Pi with the SD card and login as root
* `git clone https://github.com/tyunkeow/beleidigungsmaschine.git`
* `cd beleidigungsmaschine`
* `./build.sh`
* `./run.sh`
 

