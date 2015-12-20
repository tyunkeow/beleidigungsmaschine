#!/bin/sh
### BEGIN INIT INFO
# Provides:          brickd
# Required-Start:    $remote_fs $syslog $network
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: brickd
# Description:       Brick Daemon
### END INIT INFO

# brickd (Brick Daemon)
# Copyright (C) 2011-2012 Olaf Lüke <olaf@tinkerforge.com>
# Copyright (C) 2013-2015 Matthias Bolte <matthias@tinkerforge.com>
#
# based on skeleton from Debian GNU/Linux
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place - Suite 330,
# Boston, MA 02111-1307, USA.

PATH=/bin:/usr/bin:/sbin:/usr/sbin
DAEMON=/usr/bin/brickd
#OPTIONS=--daemon
PIDFILE=/var/run/brickd.pid

test -x $DAEMON || exit 0

. /lib/lsb/init-functions

case "$1" in
  start)
	log_daemon_msg "Starting Brick Daemon" "brickd"
	start_daemon -p $PIDFILE $DAEMON $OPTIONS
	log_end_msg $?
	;;
  stop)
	log_daemon_msg "Stopping Brick Daemon" "brickd"
	killproc -p $PIDFILE $DAEMON
	log_end_msg $?
	;;
  restart|force-reload)
	$0 stop
	sleep 1
	$0 start
	;;
  status)
	status_of_proc -p $PIDFILE $DAEMON "brickd" && exit 0 || exit $?
	;;
  *)
	echo "Usage: /etc/init.d/brickd {start|stop|restart|force-reload|status}" >&2
	exit 1
	;;
esac

exit 0
