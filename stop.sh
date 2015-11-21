#!/bin/bash
# stop.sh

echo "Stopping existing docker containers..."
docker stop insultr
docker stop brickd
docker stop syslog

docker ps -a

echo "Removing existing docker containers..."
docker rm insultr
docker rm brickd
docker rm syslog
