import requests

# URL de la API de Threat Dragon
api_url = '<http://localhost:3000/api/threatmodel>'

# Datos del modelo de amenazas
data = {
    "summary": "Modelo de amenazas de APP WEB",
    "description":"Modelo generado automaticamente",
    "thereats":[
        {
            "id":"T1",
            "title":"Inyección SQL",
            "description":"Inyeccion SQL en formularios web.",
            "migration":"Usar consultas preparadas y valdiar entradas."
        },
        {
            "id":"T2",
            "title":"Cross-Site Scripting (XSS)",
            "description":"Inyeccion de scripts maliciosos en el navegador del usuario.",
            "migration":"Escapar caracteres especiales y validar entradas."
        },
        {
            "id":"T3",
            "title":"Cross-Site Request Forgery (CSRF)",
            "description":"Ataques que engañan a los usuarios para que realicen acciones no deseadas.",
            "migration":"Usar tokens CSRF y verificar la autenticidad de las solicitudes."
        }
    ]
}

#Solicitar la creación del modelo de amenazas
response = requests.post(api_url, json=data)
if response.status_code == 201:
    print("Modelo de amenazas creado con éxito.")
else:
    print(f"Error al crear el modelo de amenazas: {response.status_code}")
    print(response.text)
# Solicitar la lista de modelos de amenazas
