import pickle
import os
from datetime import datetime

class Acceso:
    def __init__(self, id, fecha_ingreso, fecha_salida, usuario_logueado):
        self.__id = id
        self.__fecha_ingreso = fecha_ingreso
        self.__fecha_salida = fecha_salida
        self.__usuario_logueado = usuario_logueado

    # Métodos para acceder y modificar los atributos
    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value

    def get_fecha_ingreso(self):
        return self.__fecha_ingreso

    def set_fecha_ingreso(self, value):
        self.__fecha_ingreso = value

    def get_fecha_salida(self):
        return self.__fecha_salida

    def set_fecha_salida(self, value):
        self.__fecha_salida = value

    def get_usuario_logueado(self):
        return self.__usuario_logueado

    def set_usuario_logueado(self, value):
        self.__usuario_logueado = value

    def __str__(self):
        ingreso = self.__fecha_ingreso.strftime('%Y-%m-%d %H:%M:%S') if self.__fecha_ingreso else "N/A"
        salida = self.__fecha_salida.strftime('%Y-%m-%d %H:%M:%S') if self.__fecha_salida else "N/A"
        return f"Acceso ID: {self.get_id()}, Usuario: {self.get_usuario_logueado()}, Ingreso: {ingreso}, Salida: {salida}"


def registrar_acceso_exitoso(usuario, archivo="accesos.ispc"):
    """Registra un acceso exitoso del usuario en el archivo binario accesos.ispc."""
    acceso = Acceso(
        id=usuario.get_id(),
        fecha_ingreso=datetime.now(),
        fecha_salida=None, 
        usuario_logueado=usuario.get_username()
    )

    accesos = cargar_accesos(archivo)
    accesos.append(acceso)
    guardar_acceso(accesos, archivo)
    print(f"Acceso exitoso registrado para el usuario {usuario.get_username()}.")

def actualizar_fecha_salida(usuario, archivo="accesos.ispc"):
    """Actualiza la fecha de salida del último acceso del usuario."""
    accesos = cargar_accesos(archivo)
    
    for acceso in reversed(accesos):
        if acceso.get_usuario_logueado() == usuario.get_username() and acceso.get_fecha_salida() is None:
            acceso.set_fecha_salida(datetime.now())
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