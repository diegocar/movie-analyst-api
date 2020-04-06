FROM debian:latest

RUN apt-get install qemu-user-static devscripts cowbuilder dpkg-dev
RUN apk add --no-cache openssh
RUN apk update
RUN apk upgrade
