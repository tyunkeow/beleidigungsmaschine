FROM rpi-sound-base

MAINTAINER Jan Harms <mail@jan-harms.com>

USER root

RUN apt-get update -q
RUN apt-get install -y --no-install-recommends \
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

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

ENTRYPOINT ["/usr/bin/supervisord"]
