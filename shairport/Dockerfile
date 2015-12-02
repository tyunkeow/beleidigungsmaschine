FROM resin/rpi-raspbian

MAINTAINER Jan Harms <mail@jan-harms.com>

USER root

RUN apt-get update -q
RUN apt-get install -y --no-install-recommends \
	avahi-utils \
	libssl-dev \
	libao-dev \
	libpulse-dev \ 
	libasound2-dev

RUN git clone https://github.com/abrasive/shairport.git
RUN cd shairport
RUN ./configure
RUN make
RUN sudo make install
RUN cd scripts/debian/
RUN sudo cp -r * /etc/