FROM resin/rpi-raspbian
RUN apt-get update -q
RUN apt-get install -y --no-install-recommends \
	rsyslog
CMD rsyslogd -n
VOLUME /dev
VOLUME /var/log