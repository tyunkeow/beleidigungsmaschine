#!/bin/bash

echo "Removing existing docker containers..."
docker rm brickd
docker rm insulter

echo "Starting docker containers..."
docker run -d --privileged --name brickd tinkerforge_brickd
docker run -d --privileged --name insulter --link brickd:brickd insulter
docker ps -a

echo "done."
