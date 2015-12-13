FROM rpi-sound-base

RUN pip install tinkerforge

ENV HOME /insultr/

VOLUME /insultr/insult_db/

ENV AUDIO_DB_DIR /insultr/insult_db/

WORKDIR ${HOME}

CMD ["./run_insultr.sh"]

ADD *.sh $HOME

ADD *.py $HOME
