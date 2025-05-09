
import json
import requests

# Fase de Diseño y modelo de amenazas, con threats dragon

urlqa = 'http://localhost:3000/api/threats'
data={
    "summary":"Modelos de amenazas de Seguridad",
    "description":"Diagrama inicial de amenazas de la aplicación", 
    "threats":[
        {"id":"T1","title":"Inyección SQL","description":"Inyección de código SQL malicioso en la base de datos","mitigation":"Validar y sanitizar todas las entrada y usar consultas preparadas."},
        {"id":"T2","title":"Cross-Site Scripting (XSS)","description":"Inyección de scripts maliciosos en la aplicación web","mitigation":"Escapar y validar todas las entradas del usuario."},
        {"id":"T3","title":"Cross-Site Request Forgery (CSRF)","description":"Ataques que engañan a los usuarios para que realicen acciones no deseadas","mitigation":"Usar tokens CSRF y verificar la autenticidad de las solicitudes."},
        {"id":"T4","title":"Fuga de Información Sensible","description":"Exposición de datos sensibles a través de errores o configuraciones incorrectas","mitigation":"Implementar controles de acceso y cifrado de datos."},
        {"id":"T5","title":"Denegación de Servicio (DoS)","description":"Ataques que buscan hacer que un servicio no esté disponible","mitigation":"Implementar límites de tasa y monitoreo de tráfico."},
        {"id":"T6","title":"Autenticación y Gestión de Sesiones Inseguras","description":"Problemas en la gestión de sesiones y autenticación de usuarios","mitigation":"Usar HTTPS, almacenar contraseñas de forma segura y gestionar sesiones correctamente."},
        {"id":"T7","title":"Configuración Incorrecta de Seguridad","description":"Configuraciones inseguras en servidores y aplicaciones","mitigation":"Revisar y asegurar todas las configuraciones de seguridad."},
        {"id":"T8","title":"Uso de Componentes Vulnerables","description":"Uso de bibliotecas o componentes con vulnerabilidades conocidas","mitigation":"Mantener actualizadas todas las dependencias y bibliotecas."},
        {"id":"T9","title":"Control de Acceso Inadecuado","description":"Fallas en la implementación de controles de acceso","mitigation":"Implementar controles de acceso basados en roles y revisar permisos."},
        {"id":"T10","title":"Inyección de Comandos","description":"Ejecución de comandos maliciosos en el servidor","mitigation":"Validar y sanitizar todas las entradas del usuario y permisos."},
        {"id":"T11","title":"Inyección de Código","description":"Ejecución de código malicioso en la aplicación","mitigation":"Validar y sanitizar todas las entradas del usuario."},
        {"id":"T12","title":"Fuga de Información a través de Errores","description":"Exposición de información sensible a través de mensajes de error","mitigation":"Configurar mensajes de error genéricos y no revelar información sensible."},
        {"id":"T13","title":"Inyección de XML (XXE)","description":"Inyección de XML malicioso en la aplicación","mitigation":"Deshabilitar la resolución externa de entidades XML."},
        {"id":"T14","title":"Inyección de LDAP","description":"Inyección de consultas LDAP maliciosas en la aplicación","mitigation":"Validar y sanitizar todas las entradas del usuario."},
        {"id":"T15","title":"Inyección de Comandos del Sistema Operativo","description":"Ejecución de comandos del sistema operativo maliciosos","mitigation":"Validar y sanitizar todas las entradas del usuario."},
    ]
}
response = requests.post(urlqa, json=data)
if response.status_code == 201:
    print("Modelo de amenazas creado exitosamente.")
else:
    print(f"Error al crear el modelo de amenazas: {response.status_code}")
    print(response.text)
# Fase de Diseño y modelo de amenazas, con threats dragon


