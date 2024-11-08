import os

# Diccionario hash para almacenar archivos de clientes
clientes = {}

# Función para crear un archivo para un nuevo cliente
def crear_cliente(nombre, servicio):
    if nombre in clientes:
        print(f"El cliente '{nombre}' ya existe.")
    else:
        with open(f"{nombre}.txt", "w") as f:
            f.write(f"Nombre: {nombre}\nServicio: {servicio}\n")
        clientes[nombre] = f"{nombre}.txt"
        print(f"Archivo para '{nombre}' creado exitosamente.")

# Función para leer el archivo de un cliente existente
def leer_cliente(nombre):
    if nombre in clientes:
        with open(clientes[nombre], "r") as f:
            print(f"Contenido del archivo de {nombre}:\n{f.read()}")
    else:
        print(f"No se encontró el archivo para el cliente '{nombre}'.")

# Función para modificar la información de un cliente existente
def modificar_cliente(nombre, nuevo_servicio):
    if nombre in clientes:
        with open(clientes[nombre], "a") as f:
            f.write(f"Nuevo servicio: {nuevo_servicio}\n")
        print(f"Archivo de '{nombre}' actualizado con el nuevo servicio.")
    else:
        print(f"No se encontró el archivo para el cliente '{nombre}'.")

# Función para borrar el archivo de un cliente
def borrar_cliente(nombre):
    if nombre in clientes:
        os.remove(clientes[nombre])
        del clientes[nombre]
        print(f"Archivo de '{nombre}' eliminado exitosamente.")
    else:
        print(f"No se encontró el archivo para el cliente '{nombre}'.")

# Menú de opciones para interactuar con el programa
def menu():
    while True:
        print("\n--- Gestión de Clientes ---")
        print("1. Crear un nuevo cliente")
        print("2. Leer archivo de cliente")
        print("3. Modificar cliente existente")
        print("4. Borrar archivo de cliente")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            servicio = input("Ingrese el servicio solicitado: ")
            crear_cliente(nombre, servicio)
        elif opcion == "2":
            nombre = input("Ingrese el nombre del cliente: ")
            leer_cliente(nombre)
        elif opcion == "3":
            nombre = input("Ingrese el nombre del cliente: ")
            nuevo_servicio = input("Ingrese el nuevo servicio solicitado: ")
            modificar_cliente(nombre, nuevo_servicio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del cliente: ")
            borrar_cliente(nombre)
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, intente de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()
