# ! /bin/bash

# Instalar Dependency-Check si no esta instalado
if ! command -v dependency-check &> /dev/null then
    echo "Instalando OWASP Dependency-Check..."
    curl -sSfL https://raw.githubusercontent.com/jeremylong/dependency-check-bin/master/install.sh -o dependency-check.zip
    unzip dependency-check.zip -d dependency-check

fi
# Ejecutar Dependency-Check
echo "Ejecutando OWASP Dependency-Check en node..."
./dependency-check/bin/dependency-check.sh --project "Proyecto1212" --scan . --format HTML --out ./report
echo "Reporte generado en ./report"