#!/bin/bash

docker build -t syslog syslog
docker build -t tinkerforge-brickd tinkerforge-brickd
docker build -t insulter insulter

echo "done."
