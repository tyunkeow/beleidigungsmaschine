FROM resin/rpi-raspbian

MAINTAINER Jan Harms <mail@jan-harms.com>

ENV BRICKD_VERSION 2.2.2

ENV BRICKD_PORT 4223

RUN apt-get update && apt-get install -y --no-install-recommends \
	curl \
	libusb-1.0-0 \
	libudev0 \
	pm-utils \
	supervisor

RUN curl -SL "http://download.tinkerforge.com/tools/brickd/linux/brickd-${BRICKD_VERSION}_armhf.deb" -o brickd.deb

RUN dpkg -i brickd.deb

RUN rm brickd.deb

COPY brickd /etc/init.d/
#COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#WORKDIR /usr/src/brickdaemon_${BRICKD_VERSION}/src

# Port vom Brick Daemon für andere Container bekannt machen
EXPOSE $BRICKD_PORT

# Brick Daemon starten
ENTRYPOINT ["/etc/init.d/brickd"]
CMD ["start"]
#CMD ["/usr/bin/supervisord"]
