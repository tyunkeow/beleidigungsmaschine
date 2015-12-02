FROM resin/rpi-raspbian

MAINTAINER Jan Harms <mail@jan-harms.com>

USER root

RUN apt-get update -q
RUN apt-get install -y --no-install-recommends \
	avahi-utils \
	build-essential \
	ca-certificates \
	git-core \
	libssl-dev \
	libao-dev \
	libpulse-dev \ 
	libasound2-dev \
	ssh

RUN mkdir /root/.ssh/
RUN ssh-keyscan github.com >> /root/.ssh/known_hosts
RUN git clone https://github.com/abrasive/shairport.git && \
    cd shairport && \
    ./configure && \
    make && make install 

COPY airplay.sh /usr/bin/
#RUN cd scripts/debian/
#RUN sudo cp -r * /etc/

ADD shairport /etc/default/

ENTRYPOINT ["/usr/bin/airplay.sh"]