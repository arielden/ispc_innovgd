import os
import csv
import random
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

matplotlib.use('TkAgg') #Para activar el entorno gráfico en VScodem sin esto no cargan los gráficos en consola.

def generador_reg_leatorio():
    '''
    Genera registro de lluvia aleatorios.
    '''
    meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    registro_pluvial = []
    for dias in meses:
        registro_pluvial.append([random.randint(0, 100) for _ in range(dias)])
    return registro_pluvial


def guardar_registro_en_csv(registro, año):
    '''
    Guarda el registro en un archivo csv
    '''
    archivo_csv = f"registroPluvial{año}.csv"
    with open(archivo_csv, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Mes"] + [f"Día {i+1}" for i in range(31)])
        for mes, datos in enumerate(registro, start=1):
            writer.writerow([f"Mes {mes}"] + datos)
    print(f"Archivo guardado como {archivo_csv}")


def cargar_registro_csv(año):
    """
    Si existen los datos pluviales, los cargamos desde su archivo csv
    """
    archivo_csv = f"registroPluvial{año}.csv"
    
    if os.path.exists(archivo_csv):
        print(f"Cargando datos del registro {archivo_csv}...")
        dataframe = pd.read_csv(archivo_csv)
        dataframe = dataframe.apply(pd.to_numeric, errors='coerce').fillna(0) #que todos los datos sean numéricos, convertimos cualquier na a 0

        return dataframe
    else:
        print(f"El archivo {archivo_csv} no existe. Se procede a generar datos aleatorios...")
        registro_aleatorio = generador_reg_leatorio()
        guardar_registro_en_csv(registro_aleatorio, año)
        return pd.DataFrame(registro_aleatorio)

def mostrar_registros_mes(dataframe, mes):
    """Mostrar los registros pluviales de un mes específico, ajustando la cantidad de días según el mes."""
    
    dias_por_mes = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    
    if 1 <= mes <= 12:
        print(f"Registros del mes {mes}:")
        
        registros_mes = dataframe.iloc[mes-1].dropna().head(dias_por_mes[mes])  #Con esto limitamos sólo a los días válidos.
        
        registros_mes.index = [f"Día {i+1}" for i in range(len(registros_mes))]
        print(registros_mes)
    else:
        print("Mes no válido. Ingrese un número entre 1 y 12.")

# Función para generar gráficos
def generar_graficos(dataframe, año):
    '''
    Genera los tres tipos de gráficos pedidos.
    De barras.
    De dispersión.
    Circular.
    '''
    totales_mensuales = dataframe.sum(axis=1)
    plt.figure()
    plt.bar(range(1, 13), totales_mensuales)
    plt.title(f"Lluvias anuales - {año}")
    plt.xlabel("Mes")
    plt.ylabel("Milímetros")
    plt.show()

    plt.figure()
    for mes in range(1, 13):
        dias = list(range(1, len(dataframe.iloc[mes-1]) + 1))
        plt.scatter([mes] * len(dias), dias, s=dataframe.iloc[mes-1])
    plt.title(f"Dispersión de lluvias por mes - {año}")
    plt.xlabel("Mes")
    plt.ylabel("Día")
    plt.show()

    plt.figure()
    plt.pie(totales_mensuales, labels=[f"Mes {i}" for i in range(1, 13)], autopct='%1.1f%%')
    plt.title(f"Distribución de lluvias por mes - {año}")
    plt.show()

# Menú secuandrio: registros pluviales
def menu_principal_registro_pluvial():
    año = input("Ingrese el año del registro pluvial: ")
    dataframe = cargar_registro_csv(año)

    while True:
        print("\n--- Menú Registro Pluvial ---")
        print("1. Mostrar registros de un mes")
        print("2. Generar gráficos")
        print("3. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mes = int(input("Ingrese el número del mes (1-12): "))
            mostrar_registros_mes(dataframe, mes)
        elif opcion == "2":
            generar_graficos(dataframe, año)
        elif opcion == "3":
            print("Saliendo del menú de registros pluviales.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
