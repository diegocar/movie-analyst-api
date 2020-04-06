FROM node:10-alpine

RUN apk add --no-cache openssh
RUN apk update
RUN apk upgrade
RUN apt-get install qemu-user-static devscripts cowbuilder dpkg-dev
