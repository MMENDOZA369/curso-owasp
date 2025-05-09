# !/bin/bash
# Iniciar OWASP ZAP en modo damonio
zap-cli start
#Configurar url Objetivo
TARGET_URL="http://localhost:4200" # Cambia esto a la URL de tu aplicación
# Realizar el escaneo activo
zap-cli active-scan "$TARGET_URL"
# Generar el reporte de vulnerabilidades
zap-cli report -o ./reportes/zap_vulnerability_report.html -f html
# Detener OWASP ZAP
zap-cli stop
echo "Escaneo activo completado. Reporte generado en ./reportes/zap_vulnerability_report.html"
# #!/bin/bash
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
echo "║        ╚═╝  ╚═╝╚═╝          ║"
echo "║                             ║"   
echo "╚═════════════════════════════╝"
echo "${RESET}"
