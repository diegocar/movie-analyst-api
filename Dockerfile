FROM node:10-buster-slim

RUN apk add --no-cache openssh
RUN apk update
