# PROGRAMACIÓN ORIENTADA A OBJETOS

Es un paradigma de programación en la que los datos y las operaciones que pueden realizarse con esos datos se agrupan en unidades lógicas llamadas **objetos**.
Suelen representar etidades del programa, y están conformados por **atributos** y **métodos**. 

### Atributos
Son la parte estática del objeto, y describen sus características.
Por ejemplo, si definimos una tarjeta de crédito como un objeto, sus atributos serían el banco emisor, el número, su titular, fecha de vencimiento, verificación, etc.

### Métodos
Son las operaciones dinámicas del objeto, y resuelven su comportamiento. En el ejemplo de la tarjeta de crédito, sus operaciones posibles serían pagar, rechazar, anular, denunciar, etc.

## CONSULTA
La función *dir()* permite conocer los atributos y métodos de un objeto:

    dir(obj)

    Retorna una lista de atributos y métodos del objeto "obj"

Para consultar específicamente, se utiliza la función *hasattr()*:

    hasattr(obj, elem)

    Si "elem" es un atributo o método del objeto "obj" la función retorna True, de lo contrario False.

Para acceder a lso atributos o métodos de un objeto, se utiliza la sintaxis de punto:

    obj.atr

    Accede al atributo "atr" del objeto "obj"

    obj.met(parámetros)
    Ejecuta el método "met" del objeto "obj", indicándole los parámetros necesarios.

### Objetos primitivos

Un ejemplo de objetos de Python son los tipos de datos primitivos. Es por ello que poseen métodos definidos para asumir ciertos comportamientos.
Por ejemplo, las cadenas tienen el método *upper()*:

    >>> c = 'Python'
    >>> print(c.upper())
    PYTHON

Otro ejemplo es el método *append()* en las listas:

    >>> lista = [1,2,3]
    >>> lista.append(14)
    >>> print(lista)
    [1,2,3,14]

## CLASES
Agrupan objetos que comparten los mismos atributos y métodos. Son los moldes a partir de los que se crean algunos objetos que tengan las mismas características y comportamientos.
Para definir una clase, se utiliza la palabra clave *class* y el nombre de la misma, como buena práctica, comenzando con mayúsculas:

    class Nombre:
        pass
    
    Crea la clase "Nombre" y en este caso queda vacía, sin definir atributos o métodos.

### Clases primitivas

Son las clases predefinidas para los tipos de datos primitivos de Python, y podemos consultarlo mediante la función *type()*:

* int: Números enteros.
* float: Números reales.
* str: Cadenas de texto.
* list: Listas.
* tuple: Tuplas.
* dict: Diccionarios.

### Definición de atributos y métodos

Los atributos se definen como variables, mediante la sintaxis del signo = 

    atr = "atributo"

Los métodos se utiliza la palabra reservada *def* como las funciones, pero con la particularidad de que su primer parámetro se denomina *self*, ya que hace referencia al objeto donde se está creando el método. Es por ello que al llamar al método dentro del objeto, se utiliza la sintaxis *self.método*:

    >>> class Saludo:
        mensaje = "Bienvenido "    # Atributo   
        def saludar(self, nombre):    # Método
            print(self.mensaje + nombre)
            return
    >>> s = Saludo()
    >>> s.saludar('Alf')
    Bienvenido Alf

### Instanciar clases
Para crear un objeto de una determinada clase, se debe instanciar la misma. Para ello se invoca la clase por su nombre y se especifican los parámetros entre paréntesis:

   obj = Cla(par)

   El objeto "obj" es de la clase "Cla" y contiene los parámetros "par"

### Método inicializador

En la definición de una clase suele estar el método *_ _ init _ _* que será llamado cada vez que esa clase sea instanciada para crear un nuevo objeto. Este método establece los atributos básicos y generales de la clase. 

    >>> class Tarjeta:
        def __init__(self, id, cantidad = 0):    
            self.id = id
            self.saldo = cantidad                
            return
        def mostrar_saldo(self):
            print('El saldo es', self.saldo, '€')
            return
    >>> t = Tarjeta('1111111111', 1000)     
    >>> t.muestra_saldo()
    El saldo es 1000 €

Los atributos que se crean dentro del método *_ _ init _ _* se conocen como atributos de instancia, mientras que los que se crean fuera de él se conocen como atributos de la clase. Mientras que los primeros son propios de cada objeto y por tanto pueden tomar valores distintos, los valores de los atributos de la clase son constantes para cualquier objeto de la clase.

    >>> class Circulo:
        pi = 3.14159  # Atributo de clase
        def __init__(self, radio):
            self.radio = radio   # Atributo de instancia
        def area(self):
            return Circulo.pi * self.radio ** 2 
    >>> c1 = Circulo(2)
    >>> c2 = Circulo(3)
    >>> print(c1.area())
    12.56636
    >>> print(c2.area())
    28.27431
    >>> print(c1.pi)
    3.14159
    >>> print(c2.pi)
    3.14159

### Método identificador

El método especial *_ _ str _ _* permite crear un mensaje predeterminado para describir al objeto cada vez que se lo invoque con las funciones *print()* o *str()*. Si no está definido, la descripción retornará la posición de memoria del objeto:

    >>> class Tarjeta:
        def __init__(self, numero, cantidad = 0):
            self.numero = numero
            self.saldo = cantidad
            return
        def __str__(self):
            return 'Tarjeta número {} con saldo {:.2f}€'.format(self.numero, str(self.saldo))
    >>> t = tarjeta('0123456789', 1000) 
    >>> print(t)
    Tarjeta número 0123456789 con saldo 1000.00€

## HERENCIA