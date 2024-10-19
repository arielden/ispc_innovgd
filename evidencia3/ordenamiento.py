def ordenar_por_burbuja(usuarios):
    """
    Se ordenan los usuarios usando técnica de burbuja
    """
    lista_usuarios = list(usuarios.values())
    n = len(lista_usuarios)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista_usuarios[j].username > lista_usuarios[j+1].username:
                lista_usuarios[j], lista_usuarios[j+1] = lista_usuarios[j+1], lista_usuarios[j]
    
    usuarios_ordenados = {usuario.username: usuario for usuario in lista_usuarios}
    print("Usuarios ordenados por Burbuja y guardados correctamente.")
    return usuarios_ordenados


def ordenar_por_python(usuarios):
    """
    Ordena los usuarios por username usando el método sort() de Python.
    """
    lista_usuarios = sorted(usuarios.values(), key=lambda usuario: usuario.username)
    
    usuarios_ordenados = {usuario.username: usuario for usuario in lista_usuarios}
    print("Usuarios ordenados con sort() de Python y guardados correctamente.")
    return usuarios_ordenados

def buscar_usuario_secuencial(usuarios):
    """
    Busca un usuario por nombre usando búsqueda secuencial.
    """
    identificador = input("Ingrese el nombre de usuario para buscar: ")
    for usuario in usuarios.values():
        if usuario.username == identificador:
            print(usuario)
            print("Búsqueda realizada por técnica de búsqueda secuencial.")
            return
    print(f"No se encontró ningún usuario con el identificador: {identificador}")

def buscar_usuario_binaria(usuarios_ordenados):
    """
    Busca un usuario por nombre usando búsqueda binaria.
    """
    identificador = input("Ingrese el nombre de usuario para buscar: ")
    lista_usuarios = list(usuarios_ordenados.values())
    izquierda = 0
    derecha = len(lista_usuarios) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_usuarios[medio].username == identificador:
            print(lista_usuarios[medio])
            print("Búsqueda realizada por técnica de búsqueda binaria.")
            return
        elif lista_usuarios[medio].username < identificador:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    print(f"No se encontró ningún usuario con el identificador: {identificador}")
