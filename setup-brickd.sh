#!/bin/bash

# install brickd 
curl -SL "http://download.tinkerforge.com/tools/brickd/linux/brickd-latest_armhf.deb" -o /tmp/build-insultr/brickd.deb
dpkg -i /tmp/build-insultr/brickd.deb
rm /tmp/build-insultr/brickd.deb
cp brickd.sh /etc/init.d/
