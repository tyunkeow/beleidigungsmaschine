FROM resin/rpi-raspbian

MAINTAINER Jan Harms <mail@jan-harms.com>

USER root

RUN apt-get update -q
RUN apt-get install -y --no-install-recommends \
	alsa-base \
	alsa-utils \
	autoconf \
	avahi-daemon \
	avahi-utils \
	build-essential \
	ca-certificates \
	dbus \
	git-core \
	libasound2-dev \
	libavahi-client-dev \
	libdaemon-dev \
	libgpg-error0 \
	libpopt-dev \
	libssl-dev \ 
	ssh \
	supervisor

RUN mkdir /root/.ssh/
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts

RUN apt-get install -y --no-install-recommends \
	autotools-dev \
	automake

RUN git clone https://github.com/mikebrady/shairport-sync.git && \
    cd shairport-sync && \
    autoreconf -i -f && \
    ./configure --with-alsa --with-avahi --with-ssl=openssl && \
    make && \
    make install 

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENTRYPOINT ["/usr/bin/supervisord"]
