import requests

# Url de la API para generar el reporte
url = "http://localhost:3000/api/threatmodels/report"

#Solicitar el informe

response = requests.get(url)

if response.status_code == 200:
    with open("reporte_amenazas.html", "wb") as file:
        file.write(response.content)
    print("El informe de amenazas se ha generado correctamente y se ha guardado como 'reporte_amenazas.html'.")
else:
    print(f"Error al generar el informe de amenazas: {response.status_code}")
    print(response.text)
# Este script genera un informe de amenazas en formato HTML utilizando la API de Threat Dragon.
# Asegúrate de que la API de Threat Dragon esté en funcionamiento antes de ejecutar este script.
# Puedes abrir el archivo 'reporte_amenazas.html' en un navegador web para ver el informe.