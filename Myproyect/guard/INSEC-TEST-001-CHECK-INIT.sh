#!/bin/bash

# Ruta del proyecto
PROJECT_PATH="."
# Cargar variables de entorno desde el archivo .env
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi
# Verificar si el archivo .env contiene la variable APIKEY
if [ -z "$APIKEY" ]; then
    echo "❌ La variable APIKEY no está configurada en el archivo .env"
    exit 1
fi
APIKEY="${APIKEY}"
# Color naranja ANSI 256 (código 208)
ORANGE='\033[38;5;208m'
RESET='\033[0m'

echo "${ORANGE}"
echo "╔═════════════════════════════╗"
echo "║                             ║"
echo "║        ██╗  ██╗██╗ ®        ║"
echo "║        ██║ ██╔╝██║          ║"
echo "║        █████╔╝ ██║          ║"
echo "║        ██╔═██╗ ██║          ║"
echo "║        ██║  ██╗██║          ║"
echo "║        ╚═╝  ╚═╝╚═╝    test  ║"
echo "║                             ║"
echo "╚═════════════════════════════╝"
echo "${RESET}"

echo "Descargando OWASP Dependency-Check..."
curl -L "https://github.com/dependency-check/DependencyCheck/releases/download/v12.1.1/dependency-check-12.1.1-release.zip" -o dependency-check.zip

unzip dependency-check.zip -d dependency-check
chmod +x dependency-check/dependency-check.sh
rm dependency-check.zip

echo "Configurando OWASP Dependency-Check..."
echo "Actualizar dependency-check............."
./dependency-check/dependency-check/bin/dependency-check.sh --updateonly --nvdApiKey "${APIKEY}" 
echo "✅ Actualización de OWASP Dependency-Check completada."

echo "Ejecutando Análisis de dependencias de seguridad..."
./dependency-check/dependency-check/bin/dependency-check.sh --project "demo" --scan "." --format "HTML" --out ./report

echo "✅ Análisis de dependencias completado."
echo "📄 Reporte generado en ./report/dependency-check-report.html"

