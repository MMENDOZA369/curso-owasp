# Use the official Ubuntu base image
FROM ubuntu:latest

# Establecer el directorio de trabajo
WORKDIR /app

# Install necessary dependencies (incluyendo Java y unzip)
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

# Set JAVA_HOME (requerido para dependency-check)
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH=$JAVA_HOME/bin:$PATH

# Copy the Angular project into the container
COPY ./Myproyect/testing20265 /app
# Copy the report directory into the container
COPY ./Myproyect/report /app/report
# Copy the OWASP Dependency Check script into the container
COPY ./Myproyect/guard/INSEC-TEST-001-CHECK-INIT.sh /app/INSEC-TEST-001-CHECK-INIT.sh
# COPY ./INSEC-TEXT-002-THREATS-MODEL.py /app/INSEC-TEXT-002-THREATS-MODEL.py/

# Make the scripts executable
RUN chmod +x /app/INSEC-TEST-001-CHECK-INIT.sh
# RUN chmod +x /app/INSEC-TEXT-002-THREATS-MODEL.py/

# Install Angular CLI globally
RUN npm install -g @angular/cli

# Install project dependencies
RUN npm install

# Copy the .env file into the container
COPY .env /app/.env

# Export the APIKEY environment variable from the .env file
RUN export $(grep -v '^#' /app/.env | xargs)
# Run the OWASP Dependency Check script
RUN /app/INSEC-TEST-001-CHECK-INIT.sh

# Expose the default Angular development server port
EXPOSE 4200

# Command to run the Angular project
CMD ["ng", "serve", "--host", "127.0.0.1"]