# PARADIGMA DE PROGRAMACIÓN ORIENTADA A OBJETOS

## CLASES: 
Son los moldes en los que estará basada la estructura de un objeto. En base a a una sola clase pueden crearse muchos objetos iguales. Las clases tienen:
* **IDENTIDAD:** Un nombre único e irrepetible.
* **ESTADO:** Un conjunto de atributos.
* **COMPORTAMIENTO:** Un conjunto de Métodos.

Para definir una clase se utiliza la palabra reservada class, y por convención su nombre comienza con mayúsculas. Dentro de ella se definen los propios atributos y métodos:

    class Persona:
        nombre = None
        edad = None

        def mostrar_datos(self):
            print(f'Nombre:{self.nombre}')
            print(f'Edad:{self.edad}')

## OBJETOS: 
Es el elemento programable que representa algo de la vida real. Pueden ser Objetos Físicos, que son reales y tangibles (Personas, Empresas, Productos, etc) o pueden ser objetos conceptuales que son abstractos e intangibles (Asignatura de Universidad, Impuesto Municipal, Carrito de compras, etc). Para instaciar un objeto, es decir, crearlo a partir de una clase, se lo define como una variable mediante el signo *=* asignándole el nombre de la clase. Luego, cada uno de sus atributos se define de la misma manera, pero especificándolo mediante sintaxis de punto. Finalmente, con la sintaxis de punto podemos llamar a sus métodos:

    personaUno = Persona() # Se instancia el objeto
    personaUno.nombre = 'Alex' # Se asigna su atributo
    personaUno.edad = 25

    personaUno.mostrar_datos() # Se ejecuta su método

## ATRIBUTOS: 
Son las propiedades de un objeto particular. Dentro de la clase se definen como variables, con la sintaxis de asignación de valor mediante el signo *=*. Al momento de ser llamados dentro de la propia clase, los atributos deben especificarse mediante la sintaxis *self.*

## MÉTODOS: 
Son los comportamientos del objeto. Dentro de la clase se definen como las funciones, con la sintaxis *def* y luego del nombre del método, *(self)* lo que indica que es un elemento propio de la clase.

### MÉTODOS DUNDER

#### CONSTRUCTOR:
Es un método de una clase que sirve para simplificar el proceso de creación de sus objetos. Se define con la sintaxis *def __init__(self, )*, especificando tantos parámetros luego de la coma, como atributos quiera asignar. Dentro de este método se procede a la asignación de los atributos, mediante la sintaxis *self.* el nombre del atributo, y luego *=* indicando el parámetro deseado:

    class PersonaCons:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        print(f'Nombre:{self.nombre}')
        print(f'Edad:{self.edad}')
    
Al instaciar el objeto, se deben indicar los valores de sus atributos entre paréntesis, para que los obtenga el constructor, que se ejecutará automáticamente:

    persona3 = PersonaCons('Pepe', 30)
    persona4 = PersonaCons('María', 20)

#### REPRESENTACIÓN LEGIBLE
Si se intenta imprimir el contenido de un objeto mediante la sintaxis *print(objeto)* retornará la referencia al espacio de memoria en que se encuentra alojado. Para que retorne una cadena de texto con los valores de sus atributos,, dentro de la clase se defe definir *def __str__(self)* y especificar que retorne los valores deseados:

    def __str__(self):
        return f'Nombre: {self.nombre}\nEdad: {self.edad}'

Este método se ejecutará cuando se llame al objeto dentro de una función *print()* o *str()*

    print(persona3)

## PILARES

### ABSTRACCIÓN: 
Al momento de crear una clase, se debe analizar qué objetos será necesario crear con ella. La abstracción es el proceso mediante el que se obtienen los atributos y métodos básicos y comunes a una determinada cantidad de objetos, para crear una clase que pueda iniciarlos. Por ejemplo, si necesitamos definir una clase de usuario para un sistema, pero entre ellos habrá alumnos, docentes y directivos, en la clase principal solo definiremos los atributos y métodos que serán generales a todos los usuarios. 

### ENCAPSULAMIENTO:
Al definir una clase, seguramente será necesario que algunos de sus atributos y métodos no sean accesibles o modificables externamente, es decir, que no puedan leerse o editables desde afuera de la propia clase. De esta forma quedarán definidos los *atributos públicos* y *métodos públicos* y los *atributos privados* y *metodos privados*, los cuales se definirán agregando doble guión bajo a su sintaxis *__nombre*. Por ejemplo, el siguiente código simula la creación de un usuario, con dos atributos privados (contraseña y palabra clave), que solo pueden ser accedidos o modificados dentro de la propia clase:

    class Usuario:

    def __init__(self, nombre, contras, palabra):
        self.nombre = nombre
        self.__contras = contras
        self.__palabraclave = palabra

    def __ver_contras(self, palabra):
        if self.__palabraclave == palabra:
            print(f'Contraseña: {self.__contras}')
        else:
            print('Palabra clave incorrecta.')

    def __cambiar_contras(self, contras):
        if self.__contras == contras:
            nuevacont = str(input('Ingrese nueva contraseña: '))
            self.__contras = nuevacont
            print('Contraseña cambiada.')
        else:
            print('Contraseña incorrecta.')

    def __str__(self, contras):
        if self.__contras == contras:
            return f'Nombre: {self.nombre}\nContraseña: {self.__contras}\nPalabra Clave: {self.__palabraclave}'
        else:
            print('Contraseña incorrecta.')

    def menu(self):
        while True:
            print('''---MENU---
                  1 - Ver contraseña.
                  2 - Cambiar contraseña.
                  3 - Ver todos los datos.
                  4 - Salir.''')
            try:
                opc = int(input('Ingrese Opción: '))
                if opc < 1 or opc > 4:
                    raise ValueError
                elif opc == 1:
                    palabra = str(input('Ingrese palabra clave: '))
                    self.__ver_contras(palabra)
                elif opc == 2:
                    contras = str(input('Ingrese contraseña: '))
                    self.__cambiar_contras(contras)
                elif opc == 3:
                    contras = str(input('Ingrese contraseña: '))
                    print(self.__str__(contras))
                else:
                    print('Adios.')
                    break
            except ValueError:
                print('Opción incorrecta:')

En ese código, tanto los atributos como los métodos que los muestran y los modifican, son privados. En el código principal, tan solo se instanciará un objeto de esa clase, y se llamará al método *menu()*, puesto que no sería posible llamar a los métodos desde allí:

    from user import Usuario

    usuario1 = Usuario('Juan', 'abc123', 'Key')

    usuario1.menu()

Este ejemplo, si bien funciona, no es una buena práctica, ya que Python tan solo aplica el *Name Mangling* sobre los atributos y métodos privados. Es decir, no los oculta realmente sino que "mutila" sus nombres para que no sean confundidos con otros nombres del código global, tan solo agregándole internamente el nombre de la clase delante. En este caso, por ejemplo, el método *__ver_contras()*, es reasignado a nivel sistema como *_Usuario__ver_contras()* con lo que, si se utiliza ese nombre en el código global, puede accederse al método. Es decir, no es completamente seguro a nivel privacidad.

#### ATRIBUTOS Y MÉTODOS PROTEGIDOS:
En Python, existe un tipo de encapsulamiento no restrictivo que se realiza definiendo los atributos y métodos con un simple guión bajo por delante *_atributo* / *_método()*. Si bien pueden ser accedidos desde otros ficheros o desde el código global, esta particularidad indica a desarrolladores posteriores que intentar llamarlos desde fuera de la propia clase podría generar conflictos innecesarios. Se trata de una convención y de buena práctica.

### HERENCIA: 
Las clases poseen la facultad de ser modelos para la creación de otras clases, es decir, subclases. La Herencia es todo lo que una subclase obtendrá de la clase padre. Para definir una subclase, se utiliza la misma sintaxis *class*, pero se especifica entre paréntesis la clase padre. Por ejemplo, para crear una clase *Persona* y una subclase *Cliente* que herede sus atributos y métodos. Así como también una subclase *Empleado* que tenga un atributo adicional para almacenar su sueldo:

    class Usuario:

        def __init__(self, nombre, edad):
            self.nombre = nombre
            self.edad = edad
        def detalle_usuario(self):
            print(f'Nombre: {self.nombre}\nEdad: {self.edad}')

    class Cliente(Usuario):
        pass

    class Empleado(Usuario):

        def __init__(self, nombre, edad, sueldo):
            super().__init__(nombre, edad) #FUNCIÓN SUPER
            self.sueldo = sueldo
        def detalle_empleado(self):
            Usuario.detalle_usuario(self) #LLAMADO A CLASE PADRE
            print(f'Sueldo: {self.sueldo}') 

Para agregar detalles a la sublcase existen dos formas; La función *super()* indica cuál es específicamente el método o atributo que se debe heredar, y posteriormente se agregan los detalles que la subclase aportará al objeto; Llamando a la clase padre dentro de la definición, en vez de utilizar *super()*, en este caso se debe recordar utilizar el argumento *self* junto con el resto de los parámetros.

#### HERENCIA MÚLTIPLE:
En Python, las sublcases pueden heredar atributos y métodos de diferentes clases padre. Al definir la subclase, se especifican las clases padre entre paréntesis, en orden de importancia de izquierda a derecha. Es decir, que si dos clases padre contienen el mismo atributo o método, la clase hija heredará el que corresponda a la clase padre que se haya asignado primero. Por ejemplo:

    class Pc:
        def __init__(self):
            print('PC')
        def ram(self):
            print('32 GB')
        def cpu(self):
            print('Ryzen 9')

    class Laptop:
        def __init__(self):
            print('Laptop')

    class Monitor:
        def __init__(self):
            print ('Monitor')
        def pant(self):
            print ('Monitor Externo')
        def touch(self):
            print ('No touchscreen')
        def resol (self):
            print('4K')

    class Pantalla:
        def pant(self):
            print ('Pantalla Integrada')
        def touch(self):
            print ('Touchscreen')
        def resol (self):
            print('Ful HD')

    class Perif:
        def mouse (self):
            print('Mouse incluído')
        def teclado (self):
            print('teclado incluído')
        def parlantes (self):
            print('parlantes incluídos')        

    class Msi (Laptop, Pc, Pantalla, Perif):
        def resol(self):
            print('4K')

    class Pc_Gamer (Pc, Monitor, Perif):
        def parlantes (self):
            print('parlantes no incluídos')

En el ejemplo anterior, se definieron dos sublcases. Una *Msi*, que se polimorfó tan solo la resolución de pantalla, y una *Pc_Gamer* que se polimorfó solo los parlantes. Ambas clases padre (*Pc* y *Laptop*) Tienen un método constructor, por ello se asignó primero la clase padre *Laptop* en la subclase *Msi*, ya que el resto de las prestaciones prevalecen, pero el constructor indica que es una Laptop.

### POLIMORFISMO: 
Es la posibilidad de reescribir los métodos de las clases padres, dentro de la definición de una clase hija. Es la variabilidad que puede realizarse sobre la Herencia. Por ejemplo, si creamos una clase padre llamada persona y luego dos clases hijas para diferentes actividades que pueden realizar esas personas según deportes:

    class Persona(object):
        def __init__(self, nombre):
            self.nombre = nombre
        def moverse(self):
            print('Caminando')

    class Atleta(Persona):
        def moverse(self):
            print('Corriendo')

    class Ciclista(Persona):
        def moverse(self):
            print('Pedaleando')

