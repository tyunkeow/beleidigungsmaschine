#!/bin/bash

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
echo "This script is located at $SCRIPTPATH"

stop.sh

echo "Starting docker containers..."
# start syslog daemon container
docker run -d --privileged --name syslog -v /tmp/syslogdev:/dev syslog
docker run -d --privileged --name brickd tinkerforge-brickd
docker run -d --privileged --name insultr --link brickd:brickd -v "${SCRIPTPATH}/insult_db/:/insulter/insult_db" insultr
docker ps -a

echo "The following files were bound to the host:"
docker inspect -f {{.Volumes}} syslog
docker inspect -f {{.Volumes}} insultr

echo "done."
