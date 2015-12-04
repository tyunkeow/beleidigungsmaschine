FROM resin/rpi-raspbian:jessie

MAINTAINER Jan Harms <mail@jan-harms.com>

USER root

RUN apt-get update -q
RUN apt-get install -y --no-install-recommends \
	alsa-base \
	alsa-utils \
	apt-utils \
	autoconf \
	automake \
	autotools-dev \
	avahi-daemon \
	avahi-utils \
	build-essential \
	ca-certificates \
	dbus \
	git-core \
	libasound2-dev \
	libavahi-client-dev \
	libconfig-dev \
	libdaemon-dev \
	libgpg-error0 \
	libnss-mdns \
	libpopt-dev \
	libssl-dev \ 
	ssh \
	supervisor

RUN mkdir /root/.ssh/
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

RUN git clone https://github.com/mikebrady/shairport-sync.git && \
    cd shairport-sync && \
    autoreconf -i -f && \
    ./configure --with-alsa --with-avahi --with-ssl=openssl --with-systemd && \
    make && \
    make install 

#RUN mv /usr/share/alsa/alsa.conf /usr/share/alsa/alsa.orig
#RUN sed s/defaults.ctl.card\ 0/defaults.ctl.card\ 1/ /usr/share/alsa/alsa.orig | sed s/defaults.pcm.card\ 0/defaults.pcm.card\ 1/ > /usr/share/alsa/alsa.conf

ADD asound.conf /etc/asound.conf

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENTRYPOINT ["/usr/bin/supervisord"]
