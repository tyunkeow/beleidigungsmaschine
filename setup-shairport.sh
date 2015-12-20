#!/bin/bash

mkdir -p /tmp/build-insultr

# install shairport
mkdir -p /root/.ssh/
ssh-keyscan github.com >> /root/.ssh/known_hosts

git clone https://github.com/mikebrady/shairport-sync.git /tmp/build-insultr/shairport-sync

cd /tmp/build-insultr/shairport-sync && \
    autoreconf -i -f && \
    ./configure --with-alsa --with-avahi --with-ssl=openssl --with-systemd && \
    make && \
    make install 

