# PYINSTALLER:
Es una librría que permite crear archivos ejecutables de nuestros código .py, inscluyendo también módulos, multimedia, bases de datos, y todo lo necesario para el funcionamiento del programa.

## INSTALACIÓN:
El paquete de instalación de la librería **pyinstaller** se instala mediante el comando *pip install pyinstaller*, tanto en el entorno virtual en que se está trabajando, como puede ser en el sistema python base de nuestro equipo. Siempre mediante CMD, Powershell, Terminal o similar.

## COMPILACIÓN:
Para crear un archivo ejecutable de un solo script de código se puede utilizar el comando *pyinstaller /path/script.py*, indicando la dirección del script con nuestro código completo. Pero cuando se debe compilar un programa modular, con elementos multimedia, bases de datos, etc, es necesario crear un fichero de especificaciones mediante el comando *pyi-makespec /path/script.py*. En el ejemplo actual el comando sería:

    pyi-makespec catalogo_peliculas.py

Que retornará el siguiente mensaje:

    Wrote D:\Estudio\Programación\04 - Python\Udemy\13 - Proyecto\catalogo-peliculas\catalogo_peliculas.spec.
    Now run pyinstaller.py to build the executable.

Y habrá creado el archivo *catalogo_peliculas.spec*. Este archivo de especificaciones contiene:

    # -*- mode: python ; coding: utf-8 -*-

    a = Analysis(
        ['catalogo_peliculas.py'],
        pathex=[],
        binaries=[],
        datas=[],
        hiddenimports=[],
        hookspath=[],
        hooksconfig={},
        runtime_hooks=[],
        excludes=[],
        noarchive=False,
        optimize=0,
    )
    pyz = PYZ(a.pure)

    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='catalogo_peliculas',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=True,
        disable_windowed_traceback=False,
        argv_emulation=False,
        target_arch=None,
        codesign_identity=None,
        entitlements_file=None,
    )
    coll = COLLECT(
        exe,
        a.binaries,
        a.datas,
        strip=False,
        upx=True,
        upx_exclude=[],
        name='catalogo_peliculas',
    )

Este contenido debe ser editado, en la línea 7, en la etiqueta *datas* debería contener los elementos necesarios para el funcionamiento del sistema, debiendo especificar para cada uno el 'path de la rchivo','directorio que debe crear el compilador', el nombre del directorio deberá ser el mismo para que funcionen los paths del código. Por ejemplo, en este caso debería modificarse así:

    datas=[('./img/*.ico', 'img'),('./database/*.db', 'database')]

Finalmente, será necesario ejecutar el comando principal *pyinstaller* pero sobre el archivo de especificaciones:

    pyinstaller catalogo_peliculas.spec

Se crearán dos directorios build y dist. En esta última se encontrará nuestro programa en versión portable. Build contiene todos los archivos temporales que PyInstaller genera durante el proceso de compilación, como archivos .pyc (versiones compiladas de los scripts), archivos .dll o .so (bibliotecas de sistema o de terceros). Build puede eliminarse y PyInstaller simplemente lo recreará la próxima vez que se ejecute una compilación. Inclusive, es una buena práctica eliminar build y dist antes de una nueva compilación.

## MULTIPLATAFORMA:
PyInstaller funciona en Windows, Linux y macOS. Cada vez que se compila una aplicación, se crea un ejecutable en el mismo sistema operativo y la misma arquitectura del que se está trabajando. Por ejemplo, en un entorno Windows creará un ejecutable .exe.

## ERROR:
Puede suceder que *pyinstaller* cree una carpeta adicional *_internal* al compilar el programa. Si eso sucede, deberían realizarse modificaciones a los paths dentro del código. Es engorroso y molesto. Lo más sencillo es mover todos los directorios incluidos como *data*, a la misma raiz del ejecutable.