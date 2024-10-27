FROM ubuntu:22.04

# Install Keepalived and HAProxy
RUN apt-get update && apt-get install -y \
    net-tools \
    keepalived \
    haproxy
 
EXPOSE 80
EXPOSE 8444