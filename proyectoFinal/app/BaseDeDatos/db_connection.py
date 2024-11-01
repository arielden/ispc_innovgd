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