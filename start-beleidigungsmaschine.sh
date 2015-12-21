#!/bin/bash

# Absolute path to this script, e.g. /home/user/bin/foo.sh
SCRIPT=$(readlink -f "$0")
SCRIPTPATH=$(dirname "$SCRIPT")
echo "This script is located at $SCRIPTPATH"

$SCRIPTPATH/stop-beleidigungsmaschine.sh

echo "Starting brickd..."
/etc/init.d/brickd.sh start

echo "Starting dbus"
service dbus start

echo "Starting avahi-daemon"
avahi-daemon --no-drop-root

echo "Starting shairport-sync"
(shairport-sync 2>&1 > /var/log/shairport.log) &

echo "Starting Insultr..."
rm /var/log/insultr.log
python insulter/tinkerforge_stack.py &
