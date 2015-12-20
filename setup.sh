#!/bin/bash

apt-get update -q

#build tools
apt-get install -y --no-install-recommends \
	autoconf \
	automake \
	autotools-dev \
	avahi-daemon \
	avahi-utils \
	build-essential \
	ca-certificates \
	curl \
	dbus \
	git-core \
	libavahi-client-dev \
	libconfig-dev \
	libdaemon-dev \
	libgpg-error0 \
	libnss-mdns \
	libpopt-dev \
	libssl-dev \
	libusb-1.0-0 \
	libudev0 \
	pm-utils \
	ssh \
	supervisor

#sound
apt-get install -y --no-install-recommends \
	apt-utils \
    alsa-base \
	alsa-utils \
	libasound2-dev \
    libasound2-plugin-equal \
    sox \
    vim

mkdir -p /tmp/build-insultr
cd /tmp/build-insultr

# install pip
curl https://bootstrap.pypa.io/get-pip.py > get-pip.py
python get-pip.py

# install tinkerforge
pip install tinkerforge

# install brickd 
curl -SL "http://download.tinkerforge.com/tools/brickd/linux/brickd-2.2.2_armhf.deb" -o brickd.deb
dpkg -i brickd.deb
rm brickd.deb
cp brickd /etc/init.d/

# install shairport
mkdir -p /root/.ssh/
ssh-keyscan github.com >> /root/.ssh/known_hosts

git clone https://github.com/mikebrady/shairport-sync.git

cd /tmp/build-insultr/shairport-sync && \
    autoreconf -i -f && \
    ./configure --with-alsa --with-avahi --with-ssl=openssl --with-systemd && \
    make && \
    make install 

