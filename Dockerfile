FROM node:10-buster-slim

RUN apt install openssh-client
RUN apt-get upgrade -y