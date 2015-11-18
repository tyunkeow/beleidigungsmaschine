#!/bin/bash

echo "Stopping existing docker containers..."
docker stop syslog
docker stop insulter
docker stop brickd

echo "Removing existing docker containers..."
docker rm syslog
docker rm brickd
docker rm insulter

echo "Starting docker containers..."
docker run --name syslog -d -v /tmp/syslogdev:/dev syslog
docker run -d --privileged --name brickd tinkerforge_brickd
docker run -d --privileged --name insulter --link brickd:brickd insulter
docker ps -a

echo "done."
