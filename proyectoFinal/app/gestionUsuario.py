import pickle
import os
from validacion import validar_usuario, validar_clave, validar_email
from ordenamiento import ordenar_usuarios_por_username
from main import Usuario

def guardar_usuarios_ordenados_por_dni(usuarios, archivo="usuarios.ispc"):
    """Guarda el diccionario de usuarios en un archivo binario, ordenado por DNI."""
    usuarios_ordenados = dict(sorted(usuarios.items(), key=lambda item: item[1].get_dni()))
    with open(archivo, "wb") as file:
        pickle.dump(usuarios_ordenados, file)
    print("Usuarios guardados en orden por DNI.")

def cargar_usuarios(archivo="usuarios.ispc"):
    """Carga el diccionario de usuarios desde un archivo binario, en orden de DNI."""
    if os.path.exists(archivo):
        with open(archivo, "rb") as file:
            usuarios = pickle.load(file)
            #convierto dni a int
            for usuario in usuarios.values():
                if isinstance(usuario.get_dni(), str):
                    usuario.set_dni(int(usuario.get_dni()))
            return usuarios
    return {}

def agregar_usuario(usuarios):
    """Agrega un nuevo usuario al sistema y guarda el archivo con el ordenamiento por DNI."""
    id = input("Ingrese ID: ")

    # Validación numérica del DNI
    while True:
        dni = input("Ingrese el DNI: ")
        if dni.isdigit():
            dni = int(dni)  # Convertimos a entero para trabajar siempre con un número
            break
        print("DNI no válido. Debe ser un número. Intente nuevamente.")

    while True:
        username = input("Ingrese el nombre de usuario (6-12 caracteres, solo letras y números): ")
        if validar_usuario(username) and username not in usuarios:
            break
        print("Nombre de usuario no válido o ya existente. Intente nuevamente.")

    while True:
        password = input("Ingrese la contraseña: ")
        if validar_clave(password):
            break

    while True:
        email = input("Ingrese el correo electrónico: ")
        if validar_email(email):
            break
        print("Correo electrónico no válido. Intente nuevamente.")

    nuevo_usuario = Usuario(id, username, dni, password, email)
    usuarios[username] = nuevo_usuario
    guardar_usuarios_ordenados_por_dni(usuarios) 
    print("¡Usuario agregado exitosamente!")


def modificar_usuario(usuarios):
    """Modifica un usuario existente en el sistema."""
    username = input("Ingrese el nombre de usuario a modificar: ")
    if username in usuarios:
        print("Usuario encontrado. Ingrese los nuevos datos:")
        id = input("Ingrese el nuevo ID: ")

        # Validación numérica del DNI
        while True:
            dni = input("Ingrese el nuevo DNI: ")
            if dni.isdigit():
                dni = int(dni)
                break
            print("DNI no válido. Debe ser un número. Intente nuevamente.")
        
        while True:
            password = input("Ingrese la nueva contraseña: ")
            if validar_clave(password):
                break

        while True:
            email = input("Ingrese el nuevo correo electrónico: ")
            if validar_email(email):
                break

        usuario = usuarios[username]
        usuario.set_id(id)
        usuario.set_dni(dni)
        usuario.set_password(password)
        usuario.set_email(email)

        guardar_usuarios_ordenados_por_dni(usuarios)  # Guardar en orden por DNI
        print("¡Usuario modificado exitosamente!")
    else:
        print("El usuario no existe.")


def eliminar_usuario(usuarios):
    """Elimina un usuario dado su nombre de usuario o correo electrónico."""
    identificador = input("Ingrese el nombre de usuario o correo electrónico a eliminar: ")
    usuario_eliminar = None

    for username, usuario in usuarios.items():
        if usuario.get_username() == identificador or usuario.get_email() == identificador:
            usuario_eliminar = username
            break

    if usuario_eliminar:
        del usuarios[usuario_eliminar]
        guardar_usuarios_ordenados_por_dni(usuarios)  # Guardar en orden por DNI
        print(f"Usuario {identificador} eliminado exitosamente.")
    else:
        print(f"No se encontró ningún usuario con ese username o email: {identificador}")


def mostrar_usuarios_ordenados(archivo="usuariosOrdenadosPorUsername.ispc"):
    """Muestra los usuarios ordenados desde el archivo especificado."""
    if os.path.exists(archivo):
        with open(archivo, "rb") as file:
            usuarios_ordenados = pickle.load(file)
            for usuario in usuarios_ordenados.values():
                print(usuario)
    else:
        print(f"El archivo {archivo} no existe.")

def mostrar_todos_los_usuarios(archivo="usuarios.ispc"):
    """Muestra todos los usuarios registrados, cargados desde el archivo en orden por DNI."""
    if os.path.exists(archivo):
        with open(archivo, "rb") as file:
            usuarios = pickle.load(file)
            for usuario in usuarios.values():
                print(usuario)
    else:
        print("No hay usuarios disponibles.")


