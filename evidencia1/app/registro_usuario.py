import datetime
import re
import random
import aritmetica

usuarios = {}
intentos_fallidos = {}

def validar_email(email):
    # regex para validar correo
    regex = r'^\S+@\S+\.\S+$'
    return re.match(regex, email)

def validar_fecha(fecha):
    try:
        # para verificar si la fecha tiene formato AAAA-MM-DD
        datetime.datetime.strptime(fecha, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_clave(clave):
    if len(clave) < 8:
        print("La contraseña debe tener al menos 8 caracteres.")
        return False
    if not any(c.islower() for c in clave):
        print("La contraseña debe tener al menos una letra minúscula.")
        return False
    if not any(c.isupper() for c in clave):
        print("La contraseña debe tener al menos una letra mayúscula.")
        return False
    if not any(c.isdigit() for c in clave):
        print("La contraseña debe tener al menos un número.")
        return False
    if not any(not c.isalnum() for c in clave):
        print("La contraseña debe tener al menos un carácter especial.")
        return False
    return True

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
    
    if 'clave' in datos and not validar_clave(datos['clave']):
        return False

    if 'correo' in datos and not validar_email(datos['correo']):
        print("El correo electrónico no es válido.")
        return False

    if 'fecha_nacimiento' in datos and not validar_fecha(datos['fecha_nacimiento']):
        print("La fecha de nacimiento no es válida. Debe ser AAAA-MM-DD")
        return False

    return True

def ingresar_campo(campo):
    return input(f"Ingrese su {campo}: ")

def registrar_usuario():
    datos_usuario = {}
    campos = ["nombre", "apellido", "dni", "correo", "fecha_nacimiento", "nombre_usuario", "clave"]

    for campo in campos:
        while True:
            valor = ingresar_campo(campo)
            datos_usuario[campo] = valor
            if validar_usuario({campo: valor}):
                break
            else:
                print(f"Error en el campo '{campo}'. Intente nuevamente.\n")

    # acá se pide el captcha para completar el registro
    if solicitar_captcha():
        usuarios[datos_usuario["nombre_usuario"]] = datos_usuario
        print("Usuario registrado exitosamente.")

        # Guardar los datos del usuario en un archivo
        with open("usuariosCreados.txt", "a") as archivo:
            archivo.write(f"Usuario: {datos_usuario['nombre_usuario']}, DNI: {datos_usuario['dni']}, "
                          f"Nombre: {datos_usuario['nombre']} {datos_usuario['apellido']}, "
                          f"Correo: {datos_usuario['correo']}, Fecha de Nacimiento: {datos_usuario['fecha_nacimiento']} "
                          "- Creado correctamente.\n")
        print("Los datos han sido guardados en 'usuariosCreados.txt'")

    else:
        print("Registro no completado.")

def iniciar_sesion():
    nombre_usuario = input("Ingresar nombre de usuario: ")
    clave = input("Ingresar contraseña: ")

    if nombre_usuario in usuarios:
        if usuarios[nombre_usuario]["clave"] == clave:
            print(f"\n¡Bienvenido/a, {usuarios[nombre_usuario]['nombre']}!")
            
            # acá guardamos el ingreso exitoso en un archivo
            fecha_ingreso = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open("ingresos.txt", "a") as archivo_ingresos:
                archivo_ingresos.write(f"Usuario: {nombre_usuario}, Fecha de ingreso: {fecha_ingreso}\n")
            
            print(f"Fecha de ingreso registrada: {fecha_ingreso}")

            # como pudo registrar correctamente lo sacamos del dic "intentos_fallidos"
            if nombre_usuario in intentos_fallidos:
                del intentos_fallidos[nombre_usuario]
        else:
            # acá ingresamos porque el usuario ingresó una contraseña distinta
            intentos_fallidos[nombre_usuario] = intentos_fallidos.get(nombre_usuario, 0) + 1
            if intentos_fallidos[nombre_usuario] < 4:
                print(f"\nContraseña incorrecta. Intento {intentos_fallidos[nombre_usuario]} de 4.")
                print(f"ATENCIÓN: el usuario {nombre_usuario} quedará bloqueado al 4 intento.\n")
                
                # guardamos el intento fallido en un log
                with open("log.txt", "a") as log:
                    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log.write(f"{fecha_actual} - Intento fallido {intentos_fallidos[nombre_usuario]} para el usuario {nombre_usuario}.\n")
            else:
                print("Usuario bloqueado tras 4 intentos fallidos.")
                with open("log.txt", "a") as log:
                    fecha_actual = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log.write(f"{fecha_actual} - Usuario {nombre_usuario} bloqueado tras 4 intentos fallidos.\n")
    else:
        print("\nEl nombre de usuario no existe.")

def generar_captcha():
    """
    Con esta función generamos una operación aleatoria usanto el módulo aritmética.
    """
    operadores = ['+', '-', '*', '/']
    operador = random.choice(operadores)
    num1 = round(random.uniform(1, 10), 2)
    num2 = round(random.uniform(1, 10), 2)

    if operador == '+':
        resultado = aritmetica.sumar(num1, num2)
        operacion = f"{num1} + {num2}"
    elif operador == '-':
        resultado = aritmetica.restar(num1, num2)
        operacion = f"{num1} - {num2}"
    elif operador == '*':
        resultado = aritmetica.multiplicar(num1, num2)
        operacion = f"{num1} * {num2}"
    else:  # acá entramos por defecto, o sea, si el operador = /
        if num2 != 0: 
            resultado = aritmetica.dividir(num1, num2)
            operacion = f"{num1} / {num2}"
        else:
            return generar_captcha()  # si el segundo número es 0 se genera otro captcha

    return operacion, resultado

def solicitar_captcha():
    """
    Solicita al usuario que resuelva un captcha y a continuación valida la respuesta.
    """
    while True:
        operacion, resultado_esperado = generar_captcha()
        print(f"Resuelva la siguiente operación: {operacion}")
        respuesta_usuario = input("Ingrese el resultado (con 2 decimales).  Puede escribir 'salir' para cancelar el registro: ")

        if respuesta_usuario.lower() == 'salir':
            print("Registro cancelado.")
            return False

        try:
            if round(float(respuesta_usuario), 2) == resultado_esperado:
                print("Captcha correcto. Registro completado.")
                return True
            else:
                print("Respuesta incorrecta. Intente nuevamente.")
        except ValueError:
            print("Debe ingresar un número válido.")

def recuperar_pass():
    """
    Función no implementada
    """
    print("No implementado")
    pass

# Menú principal
print("Bienvenido al Sistema Único de Registro (SUR)")
while True:
    print("\nOpciones:")
    print("1. Registrar un nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Olvidé mi contraseña")
    print("4. Salir")
    opcion = input("\nIngrese una opción: ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        iniciar_sesion()
    elif opcion == '3':
        recuperar_pass()
        break
    elif opcion == '4':
        print("\nSaliendo del Sistema Único de Registro (SUR)...\n")
        break
    else:
        print("Opción inválida.")
