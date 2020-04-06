FROM debian:latest

RUN apk add --no-cache openssh
RUN apk update
RUN apk upgrade
