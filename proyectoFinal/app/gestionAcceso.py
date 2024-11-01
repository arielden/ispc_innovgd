import pickle
import os
from datetime import datetime

class Acceso:
    def __init__(self, id, fecha_ingreso, fecha_salida, usuario_logueado):
        self.__id = id
        self.__fecha_ingreso = fecha_ingreso
        self.__fecha_salida = fecha_salida
        self.__usuario_logueado = usuario_logueado

    @property
    def id(self):
        return self.__id

    @property
    def fecha_ingreso(self):
        return self.__fecha_ingreso

    @property
    def fecha_salida(self):
        return self.__fecha_salida

    @fecha_salida.setter
    def fecha_salida(self, value):
        self.__fecha_salida = value

    @property
    def usuario_logueado(self):
        return self.__usuario_logueado

    def __str__(self):
        ingreso = self.__fecha_ingreso.strftime('%Y-%m-%d %H:%M:%S') if self.__fecha_ingreso else "N/A"
        salida = self.__fecha_salida.strftime('%Y-%m-%d %H:%M:%S') if self.__fecha_salida else "N/A"
        return f"Acceso ID: {self.id}, Usuario: {self.usuario_logueado}, Ingreso: {ingreso}, Salida: {salida}"

def registrar_acceso_exitoso(usuario, archivo="accesos.ispc"):
    """Registra un acceso exitoso del usuario en el archivo binario accesos.ispc."""
    acceso = Acceso(
        id=usuario.id,
        fecha_ingreso=datetime.now(),
        fecha_salida=None, 
        usuario_logueado=usuario.username
    )

    accesos = cargar_accesos(archivo)
    accesos.append(acceso)
    guardar_acceso(accesos, archivo)
    print(f"Acceso exitoso registrado para el usuario {usuario.username}.")

def actualizar_fecha_salida(usuario, archivo="accesos.ispc"):
    """Actualiza la fecha de salida del último acceso del usuario."""
    accesos = cargar_accesos(archivo)
    
    for acceso in reversed(accesos):
        if acceso.usuario_logueado == usuario.username and acceso.fecha_salida is None:
            acceso.fecha_salida = datetime.now()
            break
        
    guardar_acceso(accesos, archivo)
    print("Fecha de salida registrada para el usuario.")

def registrar_intento_fallido(username, password, archivo="logs.txt"):
    """Registra un intento fallido de inicio de sesión en logs.txt."""
    with open(archivo, "a") as log_file:
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write(f"[{fecha_hora}] Intento fallido de login: Username: {username}, Password: {password}\n")
    print("Intento fallido registrado en logs.txt.")

def guardar_acceso(accesos, archivo="accesos.ispc"):
    """Guarda la lista de accesos en un archivo binario."""
    with open(archivo, "wb") as file:
        pickle.dump(accesos, file)

def cargar_accesos(archivo="accesos.ispc"):
    """Carga la lista de accesos desde un archivo binario."""
    if os.path.exists(archivo):
        with open(archivo, "rb") as file:
            return pickle.load(file)
    return [] 

def mostrar_accesos(archivo="accesos.ispc"):
    """Muestra los registros de accesos desde el archivo accesos.ispc."""
    accesos = cargar_accesos(archivo)
    if accesos:
        for acceso in accesos:
            print(acceso)
    else:
        print("No hay registros de accesos disponibles.")

def mostrar_logs_intentos_fallidos(archivo="logs.txt"):
    """Muestra los registros de intentos fallidos de inicio de sesión desde logs.txt."""
    if os.path.exists(archivo):
        with open(archivo, "r") as log_file:
            logs = log_file.readlines()
            if logs:
                for log in logs:
                    print(log.strip())
            else:
                print("No hay registros de intentos fallidos.")
    else:
        print("El archivo de logs no existe.")
