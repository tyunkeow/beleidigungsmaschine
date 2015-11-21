FROM hypriot/rpi-python

MAINTAINER Jan Harms <mail@jan-harms.com>

USER root

RUN apt-get update && apt-get install -y \
    alsa \
    sox

RUN pip install tinkerforge

ENV HOME /insulter/

VOLUME /insulter/insult_db/

ENV AUDIO_DB_DIR /insulter/insult_db/

ADD *.py $HOME

ADD *.sh $HOME

ADD *.json $HOME

WORKDIR ${HOME}

#CMD ["python", "tinkerforge_stack.py"]
CMD ["./run_insulter.sh"]
