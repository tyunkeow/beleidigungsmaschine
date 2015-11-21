FROM hypriot/rpi-python

MAINTAINER Jan Harms <mail@jan-harms.com>

USER root

RUN apt-get update && apt-get install -y \
    alsa \
    sox

RUN pip install tinkerforge

ENV HOME /insulter/

VOLUME /insulter/audio_db/

ENV AUDIO_DB_DIR /insulter/audio_db/

#ADD ./audio_db/* ${AUDIO_DB_DIR}/

ADD *.py $HOME

ADD *.sh $HOME

ADD *.json $HOME

WORKDIR ${HOME}

#CMD ["python", "tinkerforge_stack.py"]
CMD ["./run_insulter.sh"]
