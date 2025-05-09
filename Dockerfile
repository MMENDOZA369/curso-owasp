FROM ubuntu:latest

WORKDIR /app

RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    unzip \
    nodejs \
    npm \
    python3 \
    python3-pip \
    openjdk-17-jdk \
    && apt-get clean

ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

COPY ./Myproyect/testing20265 /app/testing20265
COPY ./Myproyect/report /app/report
COPY ./Myproyect/guard/INSEC-TEST-001-CHECK-INIT.sh /app/
COPY .env /app/.env

RUN chmod +x /app/INSEC-TEST-001-CHECK-INIT.sh
RUN npm install -g @angular/cli
RUN cd /app/testing20265 && npm install