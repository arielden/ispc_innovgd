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

def mostrar_todos_los_usuarios():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuario")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conexion.close()

def mostrar_id_nombre_apellido():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT idUsuario, nombre, apellido FROM usuario")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conexion.close()

def mostrar_juegos_accion_shooter():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM categoria WHERE tipo = 'accion' OR tipo = 'shooter'")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conexion.close()

def mostrar_usuarios_id_rango():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuario WHERE idUsuario BETWEEN 9 AND 12")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conexion.close()

def mostrar_usuarios_membresia_estandar():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM usuario WHERE Membresia_idMembresia = 2 LIMIT 3")
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conexion.close()

def crear_nuevo_usuario():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        INSERT INTO usuario (idUsuario, email, password, nombre, apellido, Membresia_idMembresia)
        VALUES (16, 'Bati@gmail.com', 'goleador10', 'Gabriel', 'Batistuta', 1)
    """)
    conexion.commit()
    print("Usuario creado exitosamente.")
    conexion.close()

def modificar_suscripcion_ultimo_usuario():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("UPDATE usuario SET Membresia_idMembresia = 2 WHERE idUsuario = 16")
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
        FROM usuario INNER JOIN membresia 
        ON usuario.Membresia_idMembresia = membresia.idMembresia
    """)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conexion.close()

def mostrar_usuarios_membresia_plus():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT usuario.nombre, usuario.apellido, membresia.tipo 
        FROM usuario INNER JOIN membresia 
        ON usuario.Membresia_idMembresia = membresia.idMembresia 
        WHERE membresia.tipo = 'plus'
    """)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conexion.close()

def mostrar_compras_por_usuario():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT compra.idCompra, usuario.nombre, usuario.apellido, compra.fecha 
        FROM compra INNER JOIN usuario 
        ON compra.Usuario_idUsuario = usuario.idUsuario
    """)
    resultados = cursor.fetchall()
    for fila in resultados:
        print(fila)
    conexion.close()