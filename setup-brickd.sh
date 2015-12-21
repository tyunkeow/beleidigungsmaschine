#!/bin/bash

mkdir -p /tmp/build-insultr

# install brickd 
curl -SL "http://download.tinkerforge.com/tools/brickd/linux/brickd-latest_armhf.deb" -o /tmp/build-insultr/brickd.deb
dpkg -i /tmp/build-insultr/brickd.deb
rm /tmp/build-insultr/brickd.deb
cp brickd.sh /etc/init.d/

sudo update-rc.d brickd.sh defaults
sudo /etc/init.d/brickd.sh start