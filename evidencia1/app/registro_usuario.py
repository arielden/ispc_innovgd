import datetime
import re

usuarios = {}

def validar_email(email):
    regex = r'\S+@\S+'
    return re.match(regex, email)

def validar_fecha(fecha):
    try:
        datetime.datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_usuario(datos):
    if 'dni' in datos:
        for usuario in usuarios.values():
            if usuario['dni'] == datos['dni']:
                print("El DNI ya está registrado.")
                return False
    
    if 'nombre_usuario' in datos:
        for usuario in usuarios.values():
            if usuario['nombre_usuario'] == datos['nombre_usuario']:
                print("El nombre de usuario ya está registrado.")
                return False
        if not 6 <= len(datos['nombre_usuario']) <= 12:
            print("Ingresar un nombre de usuario válido (entre 6 y 12 caracteres)")
            return False
    
    if 'clave' in datos:
        clave = datos['clave']
        if len(clave) < 8 or not any(c.islower() for c in clave) or not any(c.isupper() for c in clave) or not any(c.isdigit() for c in clave) or not any(not c.isalnum() for c in clave):
            print("La contraseña no cumple con los requisitos.")
            return False

    if 'correo' in datos and not validar_email(datos['correo']):
        print("El correo electrónico no es válido.")
        return False

    if 'fecha_nacimiento' in datos and not validar_fecha(datos['fecha_nacimiento']):
        print("La fecha de nacimiento no es válida. Debe ser AAAA-MM-DD")
        return False

    return True

def solicitar_dato(campo):
    return input(f"Ingrese su {campo}: ")

def registrar_usuario():
    datos_usuario = {}
    campos = ["nombre", "apellido", "dni", "correo", "fecha_nacimiento", "nombre_usuario", "clave"]

    for campo in campos:
        while True:
            valor = solicitar_dato(campo)
            datos_usuario[campo] = valor
            if validar_usuario({campo: valor}):
                break
            else:
                print(f"Error en el campo '{campo}'. Intente nuevamente.\n")

    usuarios[datos_usuario["nombre_usuario"]] = datos_usuario
    print("Usuario registrado exitosamente.")

def iniciar_sesion():
    nombre_usuario = input("Ingrese su nombre de usuario: ")
    clave = input("Ingrese su contraseña: ")

    if nombre_usuario in usuarios and usuarios[nombre_usuario]["clave"] == clave:
        print(f"¡Bienvenido/a, {usuarios[nombre_usuario]['nombre']}!")
    else:
        print("Nombre de usuario o contraseña incorrectos.")

# Menú principal
print("Bienvenido al sistema de registro de usuarios.")
while True:
    print("\nOpciones:")
    print("1. Registrar un nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        iniciar_sesion()
    elif opcion == '3':
        print("Saliendo del sistema. ¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
