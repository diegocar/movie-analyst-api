FROM node:10-buster

RUN apt-get update -y
RUN apt install openssh-client
RUN apt-get install alien -y
RUN apt-get upgrade -y