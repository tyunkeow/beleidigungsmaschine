#!/bin/bash

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
echo "This script is located at $SCRIPTPATH"

./stop.sh

echo "Starting docker containers..."
# start syslog daemon container
docker run -d --privileged --name syslog -v /tmp/syslogdev:/dev -v /tmp/syslogvarlog:/var/log syslog
docker run -d --privileged -p 4223:4223 --name brickd tinkerforge-brickd
docker run -d --privileged --name insultr -v /tmp/syslogdev/log:/dev/log --link brickd:brickd -v "${SCRIPTPATH}/insult_db:/insultr/insult_db" insultr
docker run --name shairport -v /dev/snd:/dev/snd:rw --net="host" --privileged -d shairport
docker ps -a

echo "The following files were bound to the host:"
docker inspect -f {{.Mounts}} syslog
docker inspect -f {{.Mounts}} insultr

echo "done."
