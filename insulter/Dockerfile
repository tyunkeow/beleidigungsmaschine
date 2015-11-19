FROM hypriot/rpi-python

MAINTAINER Jan Harms <mail@jan-harms.com>

USER root

RUN apt-get update && apt-get install -y \
    alsa \
    sox

RUN pip install tinkerforge


ENV HOME /insulter/

ENV AUDIO_DB /insulter/audio_db/

ADD ./audio_db/* ${AUDIO}/

#ADD ./data/audio/f/* ${AUDIO}/f/
#ADD ./data/audio/hello.aiff ${AUDIO}/hello.aiff

ADD *.py $HOME

ADD *.sh $HOME

ADD *.json $HOME

WORKDIR ${HOME}

#CMD ["python", "tinkerforge_stack.py"]
CMD ["./run_insulter.sh"]
