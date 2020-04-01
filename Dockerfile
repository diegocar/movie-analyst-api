FROM centos/nodejs-10-centos7

RUN curl -sL https://rpm.nodesource.com/setup_10.x | bash -
RUN yum install nodejs