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
COPY ./Myproyect/guard/INSEC-TEST-001-CHECK-INIT.sh /app/herramientas/
COPY .env /app/.env

RUN groupadd -r penta-test && \
    useradd -r -m -g penta-test user1 && \
    mkdir -p /app/herramientas && \
    chown -R user1:penta-test /app/herramientas && \
    chown -R user1:penta-test /app/testing20265 && \
    chmod +x /app/herramientas/INSEC-TEST-001-CHECK-INIT.sh && \
    chmod +x /app/herramientas/* && \
    npm install -g @angular/cli && \
    cd /app/testing20265 && npm install

# Ensure npm global directory is owned by user1
RUN mkdir -p /usr/local/lib/node_modules && chown -R user1:penta-test /usr/local/lib/node_modules

USER user1

RUN chmod +x /app/herramientas/INSEC-TEST-001-CHECK-INIT.sh
RUN cd /app/testing20265 && npm install