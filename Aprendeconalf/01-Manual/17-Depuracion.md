# DEPURACIÓN DE CÓDIGO

Es una técnica que permite seguir el flujo de ejecución de un programa, línea a línea, observando el estado de sus variables. Python ofrece el módulo de depuración **pyd**, pero los entornos de desarrollo como VSCode integran herramientas de depuración más sencillas y dinámicas.

## COMANDOS DE DEPURACIÓN

* **Establecer punto de parada:** Detiene la ejecución del programa en una línea concreta de código.
* **Continuar la ejecución:** Continúa la ejecución del programa hasta el siguiente punto de parada o hasta que finalice.
* **Próximo paso:** Ejecuta la siguiente línea de código y para la ejecución.
* **Próximo paso con entrada en función:** Ejecuta la siguiente línea de código. Si se trata de una llamada a una función entonces ejecuta la primera instrucción de la función y para la ejecución.
* **Próximo paso con salida de función:** Ejecuta lo que queda de la función actual y para la ejecución.
* **Terminar la depuración:** Termina la depuración.

## DEPURACIÓN EN VSCODE

* Se debe establecer un punto de parada antes de comenzar la depuración, haciendo click en el margen izquierdo de la ventana en la línea seleccionada. 
* Ejecutar el código en modo Run & Debug (Ctrl+Shift+D)
* VSCode muestra los modos de configuración disponibles, almacenados en ficheros .json. Para programas simples, se debe seleccionar la configuración *Python File*
* Comenzará la ejecución en modo depuración, mostrando una barra de navegación con los comandos para Continuar, saltar paso, detener, etc.
* Durante la ejecución en depuración, se mostrará una ventana con el estado de las variables, paso a paso. El usuario también puede modificar estos valores para experimentar distintas alternativas.