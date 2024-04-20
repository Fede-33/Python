#Simulador de programa para imprimir facturas, permitiendo ingresar el tipo de comprobante y establecer entre que fechas se emitieron:

import sys

print ("El programa", sys.argv[0], "está imprimiendo todas las facturas tipo", sys.argv[1], "emitidas desde el", sys.argv[2], "hasta el", sys.argv[3])