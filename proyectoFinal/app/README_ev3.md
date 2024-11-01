# Gestión de Usuarios y Registros Pluviales en Python

## Descripción

Para el desarrollo de esta evidencia tomamos como base los archivos utilizados en evidencia2, y los adaptamos a las consignas.
Básicamente se incluyen dos grandes funcionalidades.
1. **Gestión de usuarios** con operaciones CRUD (Crear, Leer, Actualizar, Eliminar) y validación de datos de entrada.
2. **Carga y análisis de registros pluviales** para un año, con generación de gráficos basados en los datos de lluvia.

Tal y como se trabajó en la entrega anteior, se implementaron módulos separados para organizar mejor el código, lo que facilita la evolución y el mantenimiento del proyecto.

---

## Funcionalidades:

### 1. **Gestión de Usuarios**:
   - Crear, modificar, eliminar y buscar usuarios.
   - Validar el nombre de usuario, la contraseña y el correo electrónico.
   - **Ordenar usuarios** por el nombre de usuario utilizando las técnicas de:
     - **Ordenamiento Burbuja**: Implementado manualmente como técnica de ordenamiento.
     - **Método `sort()` de Python**: Utilizando la opción nativa de Python.
   - **Búsqueda de usuarios**: Se puede buscar un usuario utilizando:
     - **Búsqueda secuencial**: Se utiliza si los usuarios no han sido ordenados previamente.
     - **Búsqueda binaria**: Se activa automáticamente si los usuarios han sido ordenados previamente.
   - Registrar accesos exitosos y fallidos al sistema en archivos binarios y logs.

#### Detalle de Ordenamiento y Búsqueda:
El sistema incluye opciones para ordenar a los usuarios según su nombre de usuario. Las opciones de ordenamiento disponibles son:

1. **Ordenamiento Burbuja**: 
   - Es una implementación manual del algoritmo de **burbuja**, donde scomparamos los nombres de usuario dos a la vez y se intercambian si están en el orden incorrecto.
   - Este método es útil para ver el proceso de ordenamiento paso a paso, puede llegar a ser menos eficiente para grandes cantidades de usuarios.

2. **Ordenamiento con `sort()` de Python**: 
   - Utiliza el método nativo de Python `sort()` para ordenar los usuarios de manera más eficiente.
   - El método `sort()` es preferible cuando el número de usuarios es mayor.

3. **Búsqueda de Usuarios**:
   - **Búsqueda secuencial**: Si los usuarios no han sido ordenados, se realiza una búsqueda secuencial revisando uno por uno.
   - **Búsqueda binaria**: Si los usuarios han sido ordenados mediante alguna técnica de ordenamiento, se puede hacer una búsqueda binaria mucho más rápida.

### 2. **Registros Pluviales**:
   - Cargar o generar aleatoriamente registros de lluvia por año.
   - Visualizar los registros de lluvia de un mes específico.
   - Generar gráficos de barras, dispersión y circulares para analizar los datos anuales.

---

## Archivos del Proyecto

- **`main.py`**: Script principal que contiene el menú principal y el flujo de ejecución de la aplicación.
- **`validacion.py`**: Módulo que maneja la validación de datos de usuario, como el correo, la contraseña y el nombre de usuario.
- **`accesos.py`**: Módulo para la gestión de accesos y el registro de accesos exitosos y fallidos.
- **`ordenamiento.py`**: Módulo que implementa las técnicas de ordenamiento (burbuja y `sort()`) y los métodos de búsqueda (secuencial y binaria).
- **`registros_pluviales.py`**: Módulo que gestiona la carga de registros pluviales, su visualización y la generación de gráficos con `matplotlib`.
- **`usuarios.ispc`**: Archivo binario que almacena los datos de los usuarios.
- **`accesos.ispc`**: Archivo binario que guarda los accesos exitosos al sistema.
- **`logs.txt`**: Archivo de texto que registra los intentos fallidos de acceso.
- **`registroPluvial<año>.csv`**: Archivo CSV que almacena los registros pluviales generados o cargados para un año específico.

---

## Requisitos

- **Python 3.6 o superior**
- Librerías:
  - `pandas`
  - `matplotlib`

Para instalar las dependencias necesarias, ejecutar:

```bash
pip install pandas matplotlib
```

## Instrucciones de Ejecución

1. Clonar el repositorio.
2. Asegurarse de tener los archivos `.py` en la misma carpeta. (evidencia3)
3. Ejecutar el archivo principal `main.py` (dentrro de la carpeta evidencia3)