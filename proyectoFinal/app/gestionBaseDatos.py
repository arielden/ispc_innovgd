import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ventadejuegos"
        )
        print("La conexión se realizó con éxito!")
        return conexion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

def cerrar_conexion(conexion):
    conexion.close()
    print("Conexión cerrada")

# consultas -----------------------------

def mostrar_usuarios_columnas_especificas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT idUsuario, email, nombre, apellido, Membresia_idMembresia FROM usuario")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conexion.close()

def mostrar_juegos_accion_shooter():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT j.idJuego, j.nombre, c.tipo
        FROM juego j
        JOIN categoria c ON j.Categoria_idCategoria = c.idCategoria
        WHERE c.tipo = 'accion' OR c.tipo = 'shooter'
    """)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conexion.close()

def mostrar_usuarios_id_rango():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT idUsuario, email, nombre, apellido FROM usuario WHERE idUsuario BETWEEN 9 AND 12")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conexion.close()

def mostrar_usuarios_membresia_estandar():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT idUsuario, email, nombre, apellido FROM usuario WHERE Membresia_idMembresia = 2 LIMIT 3")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conexion.close()

def crear_nuevo_usuario():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO usuario (idUsuario, email, password, nombre, apellido, Membresia_idMembresia, fecha_creacion)
        VALUES (16, "Bati@gmail.com", "goleador10", "Gabriel", "Batistuta", 1, CURRENT_TIMESTAMP)
    """)
    conexion.commit()
    print("Usuario creado exitosamente.")
    conexion.close()

def modificar_suscripcion_ultimo_usuario():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuario SET Membresia_idMembresia = 2, fecha_modificacion = CURRENT_TIMESTAMP WHERE idUsuario = 16")
    conexion.commit()
    print("Suscripción modificada exitosamente.")
    conexion.close()

def eliminar_ultimo_usuario():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuario WHERE idUsuario = 16")
    conexion.commit()
    print("Usuario eliminado exitosamente.")
    conexion.close()

def mostrar_nombre_apellido_tipo_suscripcion():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT usuario.nombre, usuario.apellido, membresia.tipo
        FROM usuario
        JOIN membresia ON usuario.Membresia_idMembresia = membresia.idMembresia
    """)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conexion.close()