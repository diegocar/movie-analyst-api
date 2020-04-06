FROM node:10-buster-slim

RUN apt-get update
RUN apt-get install openssh
