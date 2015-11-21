FROM hypriot/rpi-python

MAINTAINER Jan Harms <mail@jan-harms.com>

USER root

RUN apt-get update && apt-get install -y \
    alsa \
    sox

RUN pip install tinkerforge

ENV HOME /insultr/

VOLUME /insultr/insult_db/

ENV AUDIO_DB_DIR /insultr/insult_db/

ADD *.py $HOME

ADD *.sh $HOME

WORKDIR ${HOME}

#CMD ["python", "tinkerforge_stack.py"]
CMD ["./run_insultr.sh"]
