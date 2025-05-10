#! /bin/bash
# Desplegar Threat Dragon en un contenedor Docker
# Descargar y ejecutar la imagen de Threat Dragon

echo "Descargando la imagen de OWASP Threat Dragon..."
docker pull owasp/threat-dragon:stable
echo "Ejecutando la imagen de OWASP Threat Dragon en http://localhost:3000 ...."
docker run -d -p 3000:3000 owasp/threat-dragon:stable && tail -f /dev/null
echo "OWASP Threat Dragon se está ejecutando en http://localhost:3000"
