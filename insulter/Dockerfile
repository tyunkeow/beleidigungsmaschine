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

RUN mv /usr/share/alsa/alsa.conf /usr/share/alsa/alsa.orig

RUN sed s/defaults.ctl.card\ 0/defaults.ctl.card\ 1/ /usr/share/alsa/alsa.orig | sed s/defaults.pcm.card\ 0/defaults.pcm.card\ 1/ > /usr/share/alsa/alsa.conf

#CMD ["python", "tinkerforge_stack.py"]
CMD ["./run_insultr.sh"]
