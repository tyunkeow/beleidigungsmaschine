#!/bin/bash

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
echo "This script is located at $SCRIPTPATH"

echo "Stopping existing docker containers..."
docker stop insulter
docker stop brickd
docker stop syslog

echo "Removing existing docker containers..."
docker rm insulter
docker rm brickd
docker rm syslog

echo "Starting docker containers..."
# start syslog daemon container
docker run -d --privileged --name syslog -v /tmp/syslogdev:/dev syslog
docker run -d --privileged --name brickd tinkerforge_brickd
docker run -d --privileged --name insulter --link brickd:brickd -v "${SCRIPTPATH}/insulter/audio_db:/insulter/audio_db" insulter
docker ps -a

echo "The following files were bound to the host:"
docker inspect -f {{.Volumes}} syslog
docker inspect -f {{.Volumes}} insulter

echo "done."
