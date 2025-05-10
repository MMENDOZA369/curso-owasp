import re 

def validar_entrada(user_input):
    # Permitir solo caracteres alfanuméricos:
    if re.match(r'^[a-zA-Z0-9]+$', user_input):
        print("Entrada válida.")
    else:
        print("Entrada inválida. Se ha detectado una posible inyección SQL.")

enrada_usuario = input("Introduce un valor: ")
validar_entrada(enrada_usuario)
