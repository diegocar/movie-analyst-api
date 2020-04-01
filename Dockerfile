FROM centos/nodejs-10-centos7

RUN yum install -y openssh
RUN yum update -y