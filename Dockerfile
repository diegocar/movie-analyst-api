FROM centos/nodejs-10-centos7

RUN apk add --no-cache openssh
RUN apk update