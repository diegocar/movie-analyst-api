FROM node:10-buster

RUN apt install openssh-client
RUN apt-get upgrade -y
