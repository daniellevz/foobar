#######################
# Based on Ubuntu Image
#######################

# Set the base image to use to Ubuntu
FROM ubuntu

# Set the file maintainer (your name - the file's author)
MAINTAINER Danielle

# Update the default application repository sources list
#RUN echo "deb http://archive.ubuntu.com/ubuntu/ $(lsb_release -sc) main universe" >> /etc/apt/sources.list

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils

# install python
RUN apt-get install -y python3
RUN apt-get install -y python3-dev
RUN apt-get install -y python-distribute
RUN apt-get install -y python3-pip

#ADD /var/log/foobar /var/log/foobar

ADD requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
ADD . /foobar
WORKDIR /foobar
# Port to expose (foobar uses 80)
EXPOSE 80

# default command executed after creation
CMD python3 -m foobar
