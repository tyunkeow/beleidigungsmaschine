FROM resin/rpi-raspbian
RUN apt-get update -q
RUN apt-get install rsyslog
CMD rsyslogd -n
VOLUME /dev
VOLUME /var/log