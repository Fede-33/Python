from sys import argv

try:
    print(f'Nombre: {argv[1]}\nEdad: {int(argv[2])}\nAltura: {float(argv[3])}')
    print('Nombre: {}\nEdad: {}\nAltura: {}'.format(argv[1], int(argv[2]), float(argv[3])))
    print('Nombre: {n}\nEdad: {e}\nAltura: {a}'.format(e=int(argv[2]), a=float(argv[3]), n=argv[1]))
    print('Nombre: {%s}\nEdad: {%i}\nAltura: {%f}'%(argv[1],int(argv[2]), float(argv[3])))
except IndexError:
    print ('Error, ingrese nombre, edad y altura')