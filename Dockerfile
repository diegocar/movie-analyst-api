FROM centos/nodejs-10-centos7

RUN yum –y install openssh-server openssh-clients
RUN yum update -y