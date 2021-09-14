FROM ubuntu:18.04
COPY ./config.txt /app
RUN apt-get update && \
apt-get -y install sudo && \
apt-get install -y openssh-client && \
apt-get install -y openssh-server
EXPOSE 22
EXPOSE 80
ENTRYPOINT service ssh restart && sudo adduser codestrike < /app/config.txt && bash
