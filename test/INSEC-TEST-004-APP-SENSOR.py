
import json
import requests

appsensor_urlqa = 'http://localhost:3000/api/threats'
data={
    "event":{
        "detectionSystemId":"webApp-1",
        "user":{"username":"usuario_sospechoso"},
        "timestamp":"2025-09-27:34T12:00:00Z",
        "detectionPount":{"category":"Input validation","label":"IE1"},
        "action":"BloquearUsuario",
        "description":"El usuario ha sido bloqueado por actividad sospechosa.",
        "severity":"high"

    }
}

response = requests.post(appsensor_urlqa, json=data)

if response.status_code == 200:
    print("Actividad sospechosa registrada exitosamente.")
else:
    print(f"Error al registrar la actividad sospechosa: {response.status_code}")
    print(response.text)
