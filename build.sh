#!/bin/bash

docker build -t syslog syslog
docker build -t insultr insulter
docker build -t tinkerforge-brickd tinkerforge-brickd

echo "done."
