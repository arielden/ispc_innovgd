import pickle
import os
from datetime import datetime

class Acceso:
    """En esta clase representamos los accesos del usuario al sistema"""
    def __init__(self, id, fecha_ingreso, usuario_logueado):
        self.id = id
        self.fecha_ingreso = fecha_ingreso
        self.usuario_logueado = usuario_logueado

    def __str__(self):
        return f"ID Acceso: {self.id}, Usuario: {self.usuario_logueado}, Fecha de Ingreso: {self.fecha_ingreso}"

def guardar_acceso(accesos, archivo="accesos.ispc"):
    """Acá se guarda la lista de accesos en un archivo binario."""
    with open(archivo, "wb") as file:
        pickle.dump(accesos, file)

def cargar_accesos(archivo="accesos.ispc"):
    """Cargamos la lista de accesos desde un archivo binario."""
    if os.path.exists(archivo):
        with open(archivo, "rb") as file:
            return pickle.load(file)
    return []  # Si no tenemos el archivo le ponemos una lista vacía.

def registrar_intento_fallido(usuario, clave, archivo="logs.txt"):
    """Registramos un intento fallido de acceso en un archivo de texto."""
    with open(archivo, "a") as file:
        file.write(f"Intento fallido - Fecha: {datetime.now()}, Usuario: {usuario}, Clave: {clave}\n")

def ingresar_sistema(usuarios, accesos):
    """Función para ingreso al sistema con validación de usuario y contraseña."""
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    if username in usuarios and usuarios[username].password == password:
        print(f"Bienvenido a PlayHouse {username}!")
        nuevo_acceso = Acceso(len(accesos) + 1, datetime.now(), username)
        accesos.append(nuevo_acceso)
        guardar_acceso(accesos)
        while True:
            print("\n1. Volver al menú principal")
            print("2. Salir de la aplicación")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                return
            elif opcion == "2":
                print("Saliendo del sistema...")
                exit()
            else:
                print("Opción no válida. Intente nuevamente.")
    else:
        print("Credenciales incorrectas. Intente nuevamente.")
        registrar_intento_fallido(username, password)
