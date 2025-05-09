

![alt text](image.png)



Uso tipico de SAMM, comienza con una evaluación de la situación actual de las practicas de seguridad de una 
organización.

Paso 1: Situación Actual de la organización.

* Realizar entrevistas 
* Cuesttionarios.
* Análisis de procesos.
* Definición de objetivos de madurez, para una mejora en las practicas de seguridad.

Paso 2:Definicion de mejoras e iteraciones.

Las actividades se deben definir como una mejora continua en donde la organización,
debe priorizar y dar fases en conjunto con sus plazos conversados.

Tambien deben existir de ambos contexto todos los ambientes disponibles para su preventivo análisis y asi 
implementar mejoras progresivas en areas de seguridad.

La Herramienta SAMM(framework), permite realizar un seguimiento al proyecto y generar informes de madurez alcansados.

En un ciclo de vida real se pueden automtaizar ciertas actividades.


INSEC-TEST 001- Análisis inicial de dependencias.

Scrip dedicado a realizar un análisis inicial de depenendencias, con owasp dependency check, se realiza un 
una automatización la revision de vulnerabilidades, en "Dependencias" y "Bibliotecas", utilizadas en el proyecto



# # Crear un ambiente virtual llamado "testing"
  apt install python3.12-venv
# python3 -m venv testing

# # Activar el ambiente virtual
# source testing/bin/activate  # En Linux/Mac
# # .\testing\Scripts\activate  # En Windows

# # Instalar dependencias necesarias
# pip install -r requirements.txt
# # desactivar el ambiente virtual
# deactivate
