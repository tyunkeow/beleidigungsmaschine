FROM hypriot/rpi-python

MAINTAINER Jan Harms <mail@jan-harms.com>

USER root

RUN apt-get update && apt-get install -y \
	apt-utils \
    alsa-base \
	alsa-utils \  
	libasound2-dev \
    libasound2-plugin-equal \
    sox

ADD asound.conf /etc/asound.conf
