import os
import json

# Microservicio para gestionar clientes
def crear_cliente(nombre, datos):
    """Crea un archivo JSON para un cliente nuevo"""
    if not os.path.exists(f"{nombre}.json"):
        with open(f"{nombre}.json", "w") as archivo:
            json.dump(datos, archivo)
        print(f"Cliente '{nombre}' creado.")
    else:
        print("El cliente ya existe.")

def actualizar_cliente(nombre, nuevo_servicio):
    """Actualiza el archivo de un cliente existente con un nuevo servicio"""
    try:
        with open(f"{nombre}.json", "r") as archivo:
            datos = json.load(archivo)
        datos['servicios'].append(nuevo_servicio)
        with open(f"{nombre}.json", "w") as archivo:
            json.dump(datos, archivo)
        print(f"Cliente '{nombre}' actualizado con nuevo servicio.")
    except FileNotFoundError:
        print("El cliente no existe.")

# Microservicio para consultar clientes
def listar_clientes():
    """Lista todos los archivos de clientes"""
    clientes = [archivo.replace('.json', '') for archivo in os.listdir() if archivo.endswith('.json')]
    print("Clientes registrados:", clientes)

def buscar_cliente(nombre):
    """Busca y muestra la información de un cliente"""
    try:
        with open(f"{nombre}.json", "r") as archivo:
            datos = json.load(archivo)
        print(f"Datos del cliente '{nombre}':", datos)
    except FileNotFoundError:
        print("El cliente no existe.")

# Ejemplo de uso
if __name__ == "__main__":
    print("1: Crear cliente")
    print("2: Actualizar cliente")
    print("3: Listar clientes")
    print("4: Buscar cliente")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        nombre = input("Nombre del cliente: ")
        datos = {
            "nombre": nombre,
            "servicios": [input("Descripción del servicio inicial: ")]
        }
        crear_cliente(nombre, datos)
    elif opcion == "2":
        nombre = input("Nombre del cliente: ")
        nuevo_servicio = input("Descripción del nuevo servicio: ")
        actualizar_cliente(nombre, nuevo_servicio)
    elif opcion == "3":
        listar_clientes()
    elif opcion == "4":
        nombre = input("Nombre del cliente: ")
        buscar_cliente(nombre)
    else:
        print("Opción no válida.")
