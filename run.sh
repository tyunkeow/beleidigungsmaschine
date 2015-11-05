#!/bin/bash

docker run -d --privileged tinkerforge_brickd
docker run -d --privileged insulter
docker ps -a

echo "done."
