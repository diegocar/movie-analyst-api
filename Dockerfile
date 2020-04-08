FROM node:10-buster

RUN apt install openssh-client
RUN apt-get intall alien
RUN apt-get upgrade -y