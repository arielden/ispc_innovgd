import db_connection, consultas

conexion = db_connection.conectar()

if conexion:
    consultas.listar_usuarios(conexion)
    db_connection.cerrar_conexion(conexion)
else:
    print("No se pudo conectar con la base ventadejuegos.")