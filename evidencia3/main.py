import pickle
import os
from accesos import cargar_accesos, ingresar_sistema
from validacion import validar_email, validar_clave, validar_usuario
from ordenamiento import ordenar_por_burbuja, ordenar_por_python, buscar_usuario_binaria, buscar_usuario_secuencial
from registros_pluviales import menu_principal_registro_pluvial

class Usuario:
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    def __str__(self):
        return f"ID: {self.id}, Usuario: {self.username}, Email: {self.email}"

def guardar_usuarios(usuarios, archivo="usuarios.ispc"):
    """Guardar el diccionario de usuarios en un archivo binario."""
    with open(archivo, "wb") as file:
        pickle.dump(usuarios, file)

def cargar_usuarios(archivo="usuarios.ispc"):
    """Cargar el diccionario de usuarios desde un archivo binario."""
    if os.path.exists(archivo):
        with open(archivo, "rb") as file:
            return pickle.load(file)
    return {}  # Retorna un diccionario vacío si el archivo no existe

def agregar_usuario(usuarios):
    """Agregar un nuevo usuario al sistema."""
    id = input("Ingrese ID: ")

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

    nuevo_usuario = Usuario(id, username, password, email)
    usuarios[username] = nuevo_usuario
    guardar_usuarios(usuarios)
    print("¡Usuario agregado exitosamente!")

def modificar_usuario(usuarios):
    """Modificar un usuario existente."""
    username = input("Ingrese el nombre de usuario a modificar: ")
    if username in usuarios:
        print("Usuario encontrado. Ingrese los nuevos datos:")
        id = input("Ingrese el nuevo ID: ")
        
        while True:
            password = input("Ingrese la nueva contraseña: ")
            if validar_clave(password):
                break

        while True:
            email = input("Ingrese el nuevo correo electrónico: ")
            if validar_email(email):
                break

        usuarios[username] = Usuario(id, username, password, email)
        guardar_usuarios(usuarios)
        print("¡Usuario modificado exitosamente!")
    else:
        print("El usuario no existe.")

def eliminar_usuario(usuarios):
    """Eliminar un usuario dado su nombre de usuario o correo."""
    identificador = input("Ingrese el nombre de usuario o correo electrónico a eliminar: ")
    usuario_eliminar = None

    for username, usuario in usuarios.items():
        if usuario.username == identificador or usuario.email == identificador:
            usuario_eliminar = username
            break

    if usuario_eliminar:
        del usuarios[usuario_eliminar]
        guardar_usuarios(usuarios)
        print(f"Usuario {identificador} eliminado exitosamente.")
    else:
        print(f"No se encontró ningún usuario con ese username: {identificador}")

def mostrar_todos_los_usuarios(usuarios):
    """Muestra todos los usuarios registrados."""
    if usuarios:
        for usuario in usuarios.values():
            print(usuario)
    else:
        print("No hay usuarios disponibles.")

# Menú Principal
def menu_principal():
    """Función principal para el menú del sistema."""
    usuarios = cargar_usuarios()
    accesos = cargar_accesos()
    usuarios_ordenados = None  # Variable para saber si los usuarios están ordenados

    while True:
        print("\n--- Menú Principal ---")
        print("1. Agregar Usuario")
        print("2. Modificar Usuario")
        print("3. Eliminar Usuario")
        print("4. Buscar Usuario")
        print("5. Mostrar Todos los Usuarios")
        print("6. Ordenar Usuarios")
        print("7. Ingresar al Sistema")
        print("8. Registros Pluviales")
        print("9. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_usuario(usuarios)
        elif opcion == "2":
            modificar_usuario(usuarios)
        elif opcion == "3":
            eliminar_usuario(usuarios)
        elif opcion == "4":
            if usuarios_ordenados:
                buscar_usuario_binaria(usuarios_ordenados)
            else:
                buscar_usuario_secuencial(usuarios)
        elif opcion == "5":
            mostrar_todos_los_usuarios(usuarios)
        elif opcion == "6":
            print("\nOpciones de Ordenamiento:")
            print("1. Ordenar por Burbuja (Técnica Propia)")
            print("2. Ordenar por Python (sort())")
            opcion_ordenar = input("Seleccione una opción: ")

            if opcion_ordenar == "1":
                usuarios_ordenados = ordenar_por_burbuja(usuarios)
                usuarios = usuarios_ordenados
                guardar_usuarios(usuarios_ordenados)

            elif opcion_ordenar == "2":
                usuarios_ordenados = ordenar_por_python(usuarios)
                usuarios = usuarios_ordenados
                guardar_usuarios(usuarios_ordenados)

            else:
                print("Opción no válida. Intente nuevamente.")
        elif opcion == "7":
            ingresar_sistema(usuarios, accesos)
        elif opcion == "8":
            menu_principal_registro_pluvial()
        elif opcion == "9":
            print("Saliendo de la aplicación.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu_principal()
