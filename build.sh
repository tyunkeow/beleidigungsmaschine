#!/bin/bash

docker build -t rpi-sound-base rpi-sound-base
docker build -t syslog syslog
docker build -t insultr insulter
docker build -t tinkerforge-brickd tinkerforge-brickd
docker build -t shairport shairport

echo "done."
