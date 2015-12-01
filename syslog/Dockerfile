FROM resin/rpi-raspbian

MAINTAINER Jan Harms <mail@jan-harms.com>

USER root

RUN apt-get update -q
RUN apt-get install -y --no-install-recommends \
	rsyslog

CMD rsyslogd -n

VOLUME /dev

VOLUME /var/log

ADD rsyslog-insultr.conf /etc/rsyslog.conf