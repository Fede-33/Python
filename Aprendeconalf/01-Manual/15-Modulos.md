# MODULOS

El código Python puede importarse desde otro archivo *.py* como si fiese una librería. Permitiendo así, extraer funciones, variables o clases desde el código de un archivo, de forma parcial o completa.

## IMPORTACIÓN COMPLETA

Se realiza mediante la sintaxis **import** pudiendo establecer un alias para el código importado, o no:
* **import M :** Ejecuta el código que contiene *M* y crea una referencia a él, de manera que pueden invocarse un objeto o función *f* definida en él mediante la sintaxis 

        M.f.

* **import M as N :** Ejecuta el código que contiene *M*, si el nombre de *M* es extenso, incómodo o palabra reservada, se lo importa con el alias *N*, de manera que pueden invocarse un objeto o función *f* definida en él mediante la sintaxis: 

        N.f. 

### Ejemplo:

    >>> import calendar
    >>> print(calendar.month(2019, 4))
    April 2019
    Mo Tu We Th Fr Sa Su
    1  2  3  4  5  6  7
    8  9 10 11 12 13 14
    15 16 17 18 19 20 21
    22 23 24 25 26 27 28
    29 30


## IMPORTACIÓN PARCIAL

* **from M import f, g, ... :** Ejecuta el código que contiene *M* y crea referencias a los objetos *f, g, ...*, de manera que pueden ser invocados por su nombre. De esta manera para invocar cualquiera de estos objetos no hace falta precederlos por el nombre del módulo, basta con escribir su nombre.

* **from M import * :** Ejecuta el código que contiene *M* y crea referencias a todos los objetos públicos (aquellos que no empiezan por el carácter _) definidos en el módulo, de manera que pueden ser invocados por su nombre.

### Ejemplo:

    >>> from math import *
    >>> cos(pi)
    -1.0

## LIBRERÍAS ESTANDAR
Python incluye bibliotecas de módulos predefinidos como:

* **sys:** Funciones y parámetros específicos del sistema operativo.
* **os:** Interfaz con el sistema operativo.
* **os.path:** Funciones de acceso a las rutas del sistema.
* **io:** Funciones para manejo de flujos de datos y ficheros.
* **string:** Funciones con cadenas de caracteres.
* **datetime:** Funciones para fechas y tiempos.
* **math:** Funciones y constantes matemáticas.
* **statistics:** Funciones estadísticas.
* **random:** Generación de números pseudo-aleatorios.

## LIBRERÍAS EXTRA
Existen otras librerías sumamente útiles que se incluyen en otras distribuciones Python, como *Anaconda*, o pueden instalarse mediante el administrador de paquetes *pip*:

* **NumPy:** Funciones matemáticas avanzadas y arrays.
* **SciPy:** Más funciones matemáticas para aplicaciones científicas.
* **matplotlib:** Análisis y representación gráfica de datos.
* **Pandas:** Funciones para el manejo y análisis de estructuras de datos.
* **Request:** Acceso a internet por http.
