from ordenamiento import *
from gestionAcceso import *
from gestionUsuario import *
from gestionBaseDatos import *
from registros_pluviales import *
#from validacion import *

class Usuario:
    def __init__(self, id, username, dni, password, email):
        self.__id = id
        self.__username = username
        self.__dni = dni
        self.__password = password
        self.__email = email

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        self.__username = value

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, value):
        self.__dni = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    def __str__(self):
        return f"ID: {self.id}, Usuario: {self.username}, DNI: {self.dni}, Email: {self.email}"

def menu_principal():
    """Main menu function to navigate through the application."""
    usuarios = cargar_usuarios()
    accesos = cargar_accesos()
    usuarios_ordenados = None 

    while True:
        print("\n--- Menú Principal ---")
        print("1. Usuarios y Accesos de la Aplicación")
        print("2. Ingresar al sistema con los datos de usuario")
        print("3. Análisis de datos")
        print("4. Salir de la aplicación")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            menu_usuarios_accesos(usuarios, usuarios_ordenados)
        elif opcion == "2":
            iniciar_sesion_usuario(usuarios)
        elif opcion == "3":
            menu_principal_registro_pluvial()
        elif opcion == "4":
            print("Cerrando la aplicación... Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

def menu_usuarios_accesos(usuarios, usuarios_ordenados):
    """Submenu for user and access management."""
    print("\n--- Usuarios y Accesos de la Aplicación ---")
    print("1. Acceder al CRUD de los Usuarios en POO")
    print("2. Mostrar los datos de Accesos")
    print("3. Ordenamiento y Búsqueda de Usuarios")
    print("4. Volver al Menú Principal")

    subopcion1 = input("Seleccione una opción: ")

    if subopcion1 == "1":
        crud_usuarios(usuarios)
    elif subopcion1 == "2":
        mostrar_datos_accesos()
    elif subopcion1 == "3":
        menu_ordenar_buscar_usuarios(usuarios, usuarios_ordenados)
    elif subopcion1 == "4":
        return 
    else:
        print("Opción no válida.")

def crud_usuarios(usuarios):
    """CRUD operations submenu."""
    print("\n--- CRUD de los Usuarios ---")
    print("1. Agregar un nuevo usuario")
    print("2. Modificar un usuario")
    print("3. Eliminar un usuario")
    print("4. Volver al Menú Principal o al anterior")

    crud_opcion = input("Seleccione una opción: ")

    if crud_opcion == "1":
        agregar_usuario(usuarios)
    elif crud_opcion == "2":
        modificar_usuario(usuarios)
    elif crud_opcion == "3":
        eliminar_usuario(usuarios)
    elif crud_opcion == "4":
        return
    else:
        print("Opción no válida.")

def mostrar_datos_accesos():
    """Shows access and failed login attempts."""
    print("\n--- Mostrar los datos de Accesos ---")
    print("1. Mostrar los Accesos (datos de accesos.ispc)")
    print("2. Mostrar los logs de intentos fallidos (datos de logs.txt)")
    print("3. Volver al Menú Principal o al anterior")

    acceso_opcion = input("Seleccione una opción: ")

    if acceso_opcion == "1":
        mostrar_accesos()
    elif acceso_opcion == "2":
        mostrar_logs_intentos_fallidos()
    elif acceso_opcion == "3":
        return
    else:
        print("Opción no válida.")

def menu_ordenar_buscar_usuarios(usuarios, usuarios_ordenados):
    """Menu for user sorting and searching options."""
    print("\n--- Ordenamiento y Búsqueda de Usuarios ---")
    print("1. Ordenar los Usuarios")
    print("2. Buscar y Mostrar los Usuarios")
    print("3. Mostrar todos los usuarios")
    print("4. Mostrar usuarios ordenados")
    print("5. Volver al Menú Principal o al anterior")

    orden_busqueda_opcion = input("Seleccione una opción: ")

    if orden_busqueda_opcion == "1":
        ordenar_usuarios(usuarios)
    elif orden_busqueda_opcion == "2":
        buscar_y_mostrar_usuarios(usuarios, usuarios_ordenados)
    elif orden_busqueda_opcion == "3":
        mostrar_todos_los_usuarios(usuarios)
    elif orden_busqueda_opcion == "4":
        mostrar_usuarios_ordenados()
    elif orden_busqueda_opcion == "5":
        return
    else:
        print("Opción no válida.")

def ordenar_usuarios(usuarios):
    """Sorts users by username and saves sorted users."""
    print("\n--- Ordenar los Usuarios ---")
    print("1. Burbuja")
    print("2. Selección")
    metodo_opcion = input("Seleccione un método de ordenamiento: ")

    metodos = {"1": "burbuja", "2": "seleccion"}
    metodo = metodos.get(metodo_opcion, "burbuja")
    ordenar_usuarios_por_username(usuarios, metodo=metodo)

def buscar_y_mostrar_usuarios(usuarios, usuarios_ordenados):
    """Provides options to search users by DNI, username, or email."""
    print("\n--- Buscar y Mostrar los Usuarios ---")
    print("1. Búsqueda de Usuarios por DNI")
    print("2. Búsqueda de Usuarios por username")
    print("3. Buscar por email")

    busqueda_opcion = input("Seleccione el tipo de búsqueda: ")

    if busqueda_opcion == "1":
        dni = input("Ingrese el DNI a buscar: ")
        buscar_usuario_por_dni(usuarios, dni)
    elif busqueda_opcion == "2":
        username = input("Ingrese el Username a buscar: ")
        if usuarios_ordenados:
            buscar_usuario_por_username(usuarios_ordenados, username, archivo_ordenado=True)
        else:
            buscar_usuario_por_username(usuarios, username, archivo_ordenado=False)
    elif busqueda_opcion == "3":
        email = input("Ingrese el Email a buscar: ")
        buscar_usuario_por_email(usuarios, email)
    else:
        print("Opción no válida en el submenú de búsqueda.")

def iniciar_sesion_usuario(usuarios):
    """Handles user login and registration of access attempts."""
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    if username in usuarios and usuarios[username].password == password:
        print("Inicio de sesión exitoso.")
        registrar_acceso_exitoso(usuarios[username])
        gestionar_base_datos()
    else:
        print("Credenciales incorrectas.")
        registrar_intento_fallido(username, password)

def submenu_gestion_base_datos():
    """Submenú para ejecutar consultas SQL en la base de datos."""
    while True:
        print("\n--- Gestión de Base de Datos ---")
        print("1. Mostrar todos los datos de usuarios")
        print("2. Mostrar ID, nombre y apellido de usuarios")
        print("3. Mostrar juegos de acción y shooter")
        print("4. Mostrar usuarios con ID entre 9 y 12")
        print("5. Mostrar primeros 3 usuarios con membresía estándar")
        print("6. Crear un nuevo usuario (Crea el usuario Batistuta con membresía plus)")
        print("7. Modificar suscripción del último usuario agregado (modifica la memb. a standard)")
        print("8. Eliminar el último usuario agregado")
        print("9. Mostrar nombre, apellido y tipo de suscripción")
        print("10. Mostrar usuarios con membresía Plus")
        print("11. Mostrar compras por usuario y fecha")
        print("12. Volver al menú principal")

        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                mostrar_todos_los_usuarios()
            elif opcion == "2":
                mostrar_id_nombre_apellido()
            elif opcion == "3":
                mostrar_juegos_accion_shooter()
            elif opcion == "4":
                mostrar_usuarios_id_rango()
            elif opcion == "5":
                mostrar_usuarios_membresia_estandar()
            elif opcion == "6":
                crear_nuevo_usuario()
            elif opcion == "7":
                modificar_suscripcion_ultimo_usuario()
            elif opcion == "8":
                eliminar_ultimo_usuario()
            elif opcion == "9":
                mostrar_nombre_apellido_tipo_suscripcion()
            elif opcion == "10":
                mostrar_usuarios_membresia_plus()
            elif opcion == "11":
                mostrar_compras_por_usuario()
            elif opcion == "12":
                break
            else:
                print("Opción no válida. Intente nuevamente.")
        except Exception as e:
            print(f"Error al ejecutar la consulta: {e}")


def gestionar_base_datos():
    """Dummy function for database management; to be expanded."""
    print("1. Ir a la Gestión de Base de datos")
    print("2. Volver al Menú principal")
    print("3. Salir de la aplicación")

    subopcion2 = input("Seleccione una opción: ")

    if subopcion2 == "1":
        try:
            conexion = conectar()
            if conexion:
                print("Conexión exitosa. Trabajando con la base de datos...")
                submenu_gestion_base_datos()
            else:
                print("No se pudo establecer la conexión con la base de datos.")
        except Exception as e:
            print(f"Error al conectar con la base de datos: {e}")
            print("No se pudo establecer la conexión. Intente más tarde.")
    elif subopcion2 == "2":
        return
    elif subopcion2 == "3":
        exit()
    else:
        print("Opción no válida.")



if __name__ == "__main__":
    menu_principal()
