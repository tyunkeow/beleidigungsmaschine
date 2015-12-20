#!/bin/bash

apt-get update -q

apt-get update && apt-get install -y \
	apt-utils \
    alsa-base \
	alsa-utils \
	libasound2-dev \
    libasound2-plugin-equal \
    sox \
    vim

apt-get install -y --no-install-recommends \
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

curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
python get-pip.py

pip install tinkerforge

mkdir /root/.ssh/
ssh-keyscan github.com >> /root/.ssh/known_hosts

git clone https://github.com/mikebrady/shairport-sync.git && \
    cd shairport-sync && \
    autoreconf -i -f && \
    ./configure --with-alsa --with-avahi --with-ssl=openssl --with-systemd && \
    make && \
    make install 

