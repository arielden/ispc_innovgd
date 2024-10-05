# Gestión de Usuarios y Accesos en Python

## Descripción

En este proyecto desarrollamos una aplicación de consola en Python para la **gestión de usuarios** y **control de accesos**. Permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) para los usuarios, validar los datos de entrada y gestionar los accesos al sistema de manera segura.
También registramos los intentos fallidos de inicio de sesión y almacenamos la información en archivos binarios.

En un principio desarrollamos todo el código en un sólo archivo main.py pero al necesitar diversas evoluciones y correcciones en diferentes secciones del código, nos decidimos a modularizar para tener un mejor control del desarrollo.

Está modularizado en tres archivos principales:
- **`main.py`**: Contiene el menú principal y las funcionalidades del CRUD.
- **`validacion.py`**: Acá se encuentran las funciones de validación para datos de usuario (nombre de usuario, contraseña y correo).
- **`accesos.py`**: Gestiona los accesos al sistema y el registro de intentos fallidos.

## Funcionalidades

- **Gestión de Usuarios**:
  - Crear un nuevo usuario.
  - Modificar un usuario existente.
  - Eliminar un usuario por nombre de usuario o correo electrónico.
  - Buscar un usuario por nombre de usuario o correo.
  - Mostrar todos los usuarios registrados.

- **Control de Accesos**:
  - Ingresar al sistema con validación de usuario y contraseña.
  - Registrar accesos exitosos y fallidos en archivos separados.
  - Submenú post-ingreso con opciones para regresar al menú principal o salir del sistema.

## Archivos

A continuación detallamos la estructira de archivos que utilizamos en este proyecto:

- **`main.py`**: Script principal que gestiona el menú y la ejecución del programa.
- **`validacion.py`**: Contiene funciones para validar correos electrónicos, contraseñas y nombres de usuario.
- **`accesos.py`**: con este Scrip manejamos la clase `Acceso` y las funciones de registro de accesos.
- **`usuarios.ispc`**: Archivo binario para almacenar los usuarios.
- **`accesos.ispc`**: Archivo binario para almacenar los accesos exitosos.
- **`logs.txt`**: Archivo de texto para registrar los intentos fallidos de inicio de sesión.

## Requisitos

Es necesario tener instalado:

- Python 3.6 o superior

No usamos librerías adicionales más allá de las que se incluyen en la instalación estándard.

## Instrucciones de Ejecución

1. Clonar el repositorio.
2. Asegurarse de tener los siguientes archivos en la misma carpeta:
   - `main.py`
   - `validacion.py`
   - `accesos.py`
   - Si los archivos usuarios.ispc y accesos.ispc no existen, el programa los creará automáticamente.

3. Ejecutar el archivo `main.py` desde la consola o terminal con el siguiente comando:

   ```bash
   python main.py

## Como interactuar con este programa?

1. Interacción con el menú:

- Al iniciar main.py, el programa nos muestra un menú con opciones para agregar, modificar, eliminar y buscar usuarios, así como para ingresar al sistema.
- Si se selecciona la opción "Ingresar al Sistema", se tiene que ingresar un nombre de usuario y una contraseña:
- Si las credenciales son correctas, el sistema nos muestra un submenú con la opción de volver al menú principal o salir del programa.
- Si las credenciales no son correctas, se registra el intento fallido en el archivo logs.txt.

2. Pruebas de validación:

- El programa tiene funciones de validación para el nombre de usuario, la contraseña y el correo electrónico (tomamos la misma forma de validción de la evidencia anterior). Se recomienda probar los siguientes casos para verificar que las validaciones funcionan correctamente:
- Nombres de usuario: Probar nombres de usuario con menos de 6 caracteres, más de 12 caracteres, con caracteres especiales y con espacios en blanco. (DEBE FALLAR)
- Contraseñas: Probar contraseñas con menos de 8 caracteres, sin letras mayúsculas, sin letras minúsculas, sin números o sin caracteres especiales. (DEBE FALLAR)
- Correos electrónicos: Probar direcciones de correo con formatos inválidos (sin @ o sin .xxx). (DEBE FALLAR)

3. Pruebas de acceso:

- Ingresar con un nombre de usuario que no existe o con una contraseña incorrecta. El sistema muestra un mensaje de acceso fallido.
- Revisar el archivo logs.txt para ver los intentos fallidos (hemos realizado algunas pruebas), verificar que los registros se crean correctamente.
- Ingresar con un nombre de usuario válido y su contraseña correcta, y verificar que el sistema te permite acceder y que el acceso se registra en accesos.ispc. (ACCESO EXITOSO)

4. Archivos generados:

Durante la ejecución, se generarán/actualizarán tres archivos:
- usuarios.ispc: con la información de todos los usuarios registrados.
- accesos.ispc: con la información de los accesos exitosos al sistema.
- logs.txt: con el registro de todos los intentos fallidos de inicio de sesión con detalles de la fecha y hora.