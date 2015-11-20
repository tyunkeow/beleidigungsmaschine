#!/bin/bash

echo "Stopping existing docker containers..."
docker stop brickd
docker stop insulter
docker stop syslog

echo "Removing existing docker containers..."
docker rm brickd
docker rm insulter
docker rm syslog

echo "Starting docker containers..."
# start syslog daemon container
docker run -d --privileged --name syslog -v /tmp/syslogdev:/dev syslog
docker run -d --privileged --name insulter --link brickd:brickd insulter
docker run -d --privileged --name brickd tinkerforge_brickd
docker ps -a

echo "The following files were bound to the host:"
docker inspect -f {{.Volumes}} syslog

echo "done."
