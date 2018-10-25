FROM debian:jessie
MAINTAINER Alex Wilson a.wilson@alumni.warwick.ac.uk

ENV JAVA_HOME /opt/java
ENV PATH /opt/flume/bin:/opt/java/bin:/opt/nsq/bin:$PATH
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -qq \ 
    && apt-get install -q -y --no-install-recommends wget \
    && mkdir /opt/java \ 
    && wget --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" -qO- \
          http://download.oracle.com/otn-pub/java/jdk/8u181-b13/96a7b8442fe848ef90c96a2fad6ed6d1/jre-8u181-linux-x64.tar.gz \
          | tar zxvf - -C /opt/java --strip 1 \
    && mkdir /opt/flume \ 
    && wget -qO- http://archive.apache.org/dist/flume/1.8.0/apache-flume-1.8.0-bin.tar.gz \
          | tar zxvf - -C /opt/flume --strip 1 \
    && mkdir /opt/nsq \
    && wget -qO- http://s3.amazonaws.com/bitly-downloads/nsq/nsq-1.0.0-compat.linux-amd64.go1.8.tar.gz \
          | tar zxvf - -C /opt/nsq --strip 1 \
    && mkdir /opt/hadoop \
    && wget -qO- http://www.eu.apache.org/dist/hadoop/core/hadoop-3.1.1/hadoop-3.1.1.tar.gz \
          | tar zxvf - -C /opt/hadoop --strip 1

ADD start-flume.sh /opt/flume/bin/start-flume

ENTRYPOINT [ "start-flume" ]
