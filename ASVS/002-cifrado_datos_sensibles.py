from cryptography.fernet import Fernet

def generate_key():
    clave = Fernet.generate_key()
    with open("clave.key", "wb") as clave_file:
        clave_file.write(clave)
def cargar_clave():
    return open("clave.key", "rb").read()

def cifrar_datos(datos):
    clave = cargar_clave()
    fernet = Fernet(clave)
    return fernet.encrypt(datos.encode())

def descifrar_datos(datos_cifrados):
    clave = cargar_clave()
    fernet = Fernet(clave)
    return fernet.decrypt(datos_cifrados).decode()

if __name__ == "__main__":
    generate_key()
    datos_sensibles = "Pepegrillo 123, Calle de la Luz, Madrid"
    datos_cifrados = cifrar_datos(datos_sensibles)
    print(f"Datos cifrados: {datos_cifrados}")
    print(f"Datos descifrados: {descifrar_datos(datos_cifrados)}")
