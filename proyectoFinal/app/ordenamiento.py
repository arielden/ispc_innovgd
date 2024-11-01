import pickle
import datetime

def ordenar_por_burbuja(lista_usuarios):
    """Ordena los usuarios usando el método de burbuja por username."""
    n = len(lista_usuarios)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_usuarios[j].get_username() > lista_usuarios[j + 1].get_username():
                lista_usuarios[j], lista_usuarios[j + 1] = lista_usuarios[j + 1], lista_usuarios[j]
    return lista_usuarios

def ordenar_por_seleccion(lista_usuarios):
    """Ordena los usuarios usando el método de selección por username."""
    n = len(lista_usuarios)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lista_usuarios[j].get_username() < lista_usuarios[min_index].get_username():
                min_index = j
        lista_usuarios[i], lista_usuarios[min_index] = lista_usuarios[min_index], lista_usuarios[i]
    return lista_usuarios

def ordenar_usuarios_por_username(usuarios, metodo="burbuja", archivo="usuariosOrdenadosPorUsername.ispc"):
    """Ordena los usuarios por username usando el método especificado y guarda en un archivo separado."""
    lista_usuarios = list(usuarios.values())

    if metodo == "burbuja":
        lista_usuarios = ordenar_por_burbuja(lista_usuarios)
    elif metodo == "seleccion":
        lista_usuarios = ordenar_por_seleccion(lista_usuarios)
    else:
        print("Método de ordenamiento no válido. Usando método por defecto (burbuja).")
        lista_usuarios = ordenar_por_burbuja(lista_usuarios)

    usuarios_ordenados = {usuario.get_username(): usuario for usuario in lista_usuarios}

    with open(archivo, "wb") as file:
        pickle.dump(usuarios_ordenados, file)
    
    print(f"Usuarios ordenados por {metodo} y guardados en {archivo}.")

def buscar_usuario_por_dni(usuarios, dni):
    """Busca un usuario por DNI utilizando búsqueda binaria y genera un archivo de log."""
    dni = int(dni)  # Asegurarse de que `dni` sea un entero
    lista_usuarios = sorted(usuarios.values(), key=lambda usuario: usuario.get_dni())
    izquierda, derecha = 0, len(lista_usuarios) - 1
    log_filename = f"busquedasYordenamientos/buscandoUsuarioPorDNI-{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    
    with open(log_filename, "w") as log_file:
        log_file.write(f"Búsqueda Binaria por DNI: buscando el DNI {dni} en el archivo.\n")
        
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
            dni_actual = lista_usuarios[medio].get_dni()
            log_file.write(f"Intento: DNI en posición {medio} es {dni_actual}.\n")
            
            if dni_actual == dni:
                log_file.write("Usuario encontrado.\n")
                print(lista_usuarios[medio])
                return
            elif dni_actual < dni:
                izquierda = medio + 1
                log_file.write("Buscar en subsecuencia de la derecha.\n")
            else:
                derecha = medio - 1
                log_file.write("Buscar en subsecuencia de la izquierda.\n")
        
        log_file.write("Usuario no encontrado.\n")
        print("No se encontró el usuario con ese DNI.")


def buscar_usuario_por_username(usuarios, username, archivo_ordenado=False):
    """Busca un usuario por username. Usa búsqueda binaria si el archivo está ordenado."""
    if archivo_ordenado:
        lista_usuarios = sorted(usuarios.values(), key=lambda usuario: usuario.get_username())
        izquierda, derecha = 0, len(lista_usuarios) - 1
        log_filename = f"busquedasYordenamientos/buscandoUsuarioPorUsername-{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        
        with open(log_filename, "w") as log_file:
            log_file.write(f"Búsqueda Binaria por username: buscando el username {username} en archivo ordenado.\n")
            
            while izquierda <= derecha:
                medio = (izquierda + derecha) // 2
                username_actual = lista_usuarios[medio].get_username()
                log_file.write(f"Intento: username en posición {medio} es {username_actual}.\n")

                if username_actual == username:
                    log_file.write("Usuario encontrado.\n")
                    print(lista_usuarios[medio])
                    return
                elif username_actual < username:
                    izquierda = medio + 1
                    log_file.write("Buscar en subsecuencia de la derecha.\n")
                else:
                    derecha = medio - 1
                    log_file.write("Buscar en subsecuencia de la izquierda.\n")
            
            log_file.write("Usuario no encontrado.\n")
            print("No se encontró el usuario con ese username.")
    else:
        print("Búsqueda secuencial por username.")
        for intento, usuario in enumerate(usuarios.values(), 1):
            print(f"Intento {intento}: {username} comparado con {usuario.get_username()}")
            if usuario.get_username() == username:
                print(f"Usuario encontrado en intento {intento}.")
                print(usuario)
                return
        print("No se encontró el usuario con ese username.")

def buscar_usuario_por_email(usuarios, email):
    """Busca un usuario por email utilizando búsqueda secuencial."""
    print("Búsqueda secuencial por email.")
    for intento, usuario in enumerate(usuarios.values(), 1):
        print(f"Intento {intento}: {email} comparado con {usuario.get_email()}")
        if usuario.get_email() == email:
            print(f"Usuario encontrado en intento {intento}.")
            print(usuario)
            return
    print("No se encontró el usuario con ese email.")
