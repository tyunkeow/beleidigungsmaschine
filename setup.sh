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

# install pip
curl https://bootstrap.pypa.io/get-pip.py > /tmp/build-insultr/get-pip.py
python /tmp/build-insultr/get-pip.py

# install tinkerforge
pip install tinkerforge

#install brickd
setup-brickd.sh

# install shairport
setup-shairport.sh