FROM centos/nodejs-10-centos7

RUN sudo yum –y install openssh-server openssh-clients
RUN yum update -y