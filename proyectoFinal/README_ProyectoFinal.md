# Gestión de Usuarios y Registros Pluviales en Python

## Descripción

Este proyecto es una aplicación de consola para la gestión de usuarios, accesos y análisis de datos de lluvia. Implementa funcionalidades de CRUD para usuarios, registros de acceso, y un sistema de análisis de datos pluviales.
Se incluye un sistema de búsqueda y ordenamiento de usuarios por DNI y username, y la posibilidad de realizar consultas SQL sobre la base de datos de ventas de juegos (generada como proyecto del primer cuatrimestre y optimizada en base a devoluciones de evidencias anteriores).
1. **Gestión de Usuarios**:
   - CRUD de usuarios almacenados en un archivo binario usuarios.ispc.
   - Los usuarios se almacenan y muestran ordenados por DNI.
   - Implementación de búsquedas y ordenamientos por DNI y username.
2. **Registro de Accesos**
   - Registra los accesos exitosos de usuarios en accesos.ispc.
   - Guarda intentos fallidos en un archivo de texto logs.txt.
3. **Análisis de Datos Pluviales**
   - Carga o genera datos de lluvias diarias para un año específico en archivos CSV.
   - Permite visualizar datos de lluvia y generar gráficos usando matplotlib.


## Estructura de Archivos y Carpetas
```
proyectoFinal/
├── app/
│   ├── __pycache__/            # archivos de caché
│   ├── BaseDeDatos/            # onexiones y consultas SQL
│   ├── busquedasYordenamientos/ # logs de búsqueda y ordenamiento
│   ├── datosAnalizados/        # para almacenar resultados de análisis
│   ├── accesos.ispc            # archivo binario de accesos registrados
│   ├── gestionAcceso.py        # Gestión de accesos y logs de intentos fallidos
│   ├── gestionBaseDatos.py     # Conexión y consultas con la base de datos SQL
│   ├── gestionUsuario.py       # CRUD de usuarios y almacenamiento en `usuarios.ispc`
│   ├── logs.txt                # Registros de intentos fallidos de inicio de sesión
│   ├── main.py                 # Ejecuta el menú y funcionalidades de la aplicación
│   ├── ordenamiento.py         # Código de funciones de ordenamiento y búsqueda de usuarios
│   ├── README.md               # Readme general
│   ├── registros_pluviales.py  # Código para análisis y visualización de datos pluviales
│   ├── usuarios.ispc           # Archivo binario con los datos de usuarios
│   ├── usuariosOrdenadosPorUsername.ispc # Archivo binario con usuarios ordenados por `username`
│   └── validacion.py           # Funciones para validación de datos de usuarios (username, email, etc.)
├── sql/
│   └── ventadejuegos_structure_and_data.sql # Archivo SQL para consultas de base de datos de venta de juegos
├── README_ProyectoFinal.md     # Documentación general del proyecto

```


---

## Requisitos

- **Python 3.6 o superior**
- Librerías:
  - `pandas`
  - `matplotlib`
  - `mysql-connector`

Para instalar las dependencias necesarias, ejecutar:

```bash
pip install -r requirements.txt
```

## Instrucciones de Ejecución

1. Clonar el repositorio.
2. Asegurarse de tener los archivos `.py` en la misma carpeta. (proyectoFinal/app)
3. Ejecutar el archivo principal `main.py` (proyectoFinal/app)