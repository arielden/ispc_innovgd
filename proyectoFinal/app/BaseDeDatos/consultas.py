def listar_usuarios(conexion):
    cursor = conexion.cursor()
    cursor.execute("SELECT idUsuario, email, nombre, apellido FROM usuario")
    usuarios = cursor.fetchall()
    for usuario in usuarios:
        print(usuario)

def agregar_usuario(conexion, email, password, nombre, apellido, membresia_id):
    cursor = conexion.cursor()
    consulta = """
        INSERT INTO usuario (email, password, nombre, apellido, Membresia_idMembresia, fecha_creacion)
        VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
    """
    cursor.execute(consulta, (email, password, nombre, apellido, membresia_id))
    conexion.commit()
    print("Usuario agregado exitosamente")

