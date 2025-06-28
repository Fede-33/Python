# ENTORNO VIRTUAL:
Es el conjunto de lenguajes de programación, aplicaciones y librerías que se van a utilizar en el desarrollo del proyecto. Crear un entorno virtual ayuda a definir las versiones de las herramientas que se utilizan, previendo que en el futuro, pueda seguir actualizándose el software desarrollado, y esas actualizaciones puedan desarrollarse con nuevas versiones de las herramientas. Conocer las previas versiones de los sistemas aplicados, evita conflictos en el futuro.

## PYTHON
Para crear un entorno virtual en Python puede utilizarse la librería *venv*, incluida en el sistema base, ejecutando por consola el comando *pyhton3 -m venv env* en Windows, o *python3 -m venv env* en MAC o Linux, siendo en este caso *env* el nombre que asignaremos al entorno virtual. 
Esto creará un directorio con el mismo nombre del entorno virtual, *env* en este caso. Que contendrá una serie de carpetas:
* **Include**:
* **Lib**: con las librerías que se utilizarán, tanto las que aporta el sistema por defecto como las que se agregarán luego.
* **Scripts** o **bin**: Dónde se encuentran los comandos de activación, desactivación y ejecutables

Luego de este comando debemos activar el entorno, mediante la sintaxis *env\Scripts\activate.bat* en Windows, o *source env/bin/activate* en Linux o Mac. Mientras que el entorno virtual esté activado, las librerías y utilidades estarán en la versión del entorno. Para desactivar el entorno virtual, se reemplaza por *deactivate*, pudiéndose verificar que las versiones volverán a ser las del sistema general. 
