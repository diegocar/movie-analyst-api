FROM node:10-alpine

RUN apk add --no-cache openssh
RUN apk update
RUN apk install