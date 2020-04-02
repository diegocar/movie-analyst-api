FROM centos/nodejs-10-centos7:20200331-1f30af0

RUN yum install curl sudo
RUN sudo yum install epel-release
RUN curl -sL https://rpm.nodesource.com/setup_10.x | sudo bash -
RUN yum install nodejs