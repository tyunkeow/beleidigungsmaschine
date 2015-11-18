FROM hypriot/rpi-python

MAINTAINER Jan Harms <mail@jan-harms.com>

USER root

ENV AUDIO /data/audio/

ENV HOME /insulter/

ADD ./data/audio/m/* ${AUDIO}/m/

ADD ./data/audio/f/* ${AUDIO}/f/

ADD ./data/audio/hello.aiff ${AUDIO}/hello.aiff

RUN apt-get update && apt-get install -y \
    alsa \
    sox

RUN pip install tinkerforge

ADD *.py $HOME

ADD *.sh $HOME

ADD *.json $HOME

WORKDIR ${HOME}

#CMD ["python", "tinkerforge_stack.py"]
CMD ["./run_insulter.sh"]
