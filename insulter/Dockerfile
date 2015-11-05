FROM hypriot/rpi-python

MAINTAINER Jan Harms <mail@jan-harms.com>

USER root

ENV AUDIO /data/audio/

ENV HOME /insulter/

ADD ./data/audio/m/* ${AUDIO}/m/

ADD ./data/audio/f/* ${AUDIO}/f/

ADD *.py $HOME

RUN apt-get update && apt-get install -y \
    alsa \
    sox

RUN pip install tinkerforge

WORKDIR ${HOME}

RUN ["python", "tinkerforge_stack.py"]
