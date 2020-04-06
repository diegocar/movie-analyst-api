FROM debian:latest

RUN apt-get install sudo
RUN sudo apt install curl
RUN curl -sL https://deb.nodesource.com/setup_13.x | sudo -E bash -
RUN sudo apt-get install -y nodejs