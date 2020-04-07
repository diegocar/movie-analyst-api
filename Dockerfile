FROM node:10-buster

RUN apt-get install qemu-user-static devscripts cowbuilder dpkg-dev
RUN apt install openssh-client
RUN apt-get upgrade -y