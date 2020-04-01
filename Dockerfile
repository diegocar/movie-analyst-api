FROM centos/nodejs-10-centos7

RUN yum install -y --no-cache openssh
RUN yum update -y