from gerente import Gerente
from empleado import Empleado

def imprimir_detalle(tipo_clase):
    print(tipo_clase,end="\n\n")
    

empleado = Empleado("fran",200.00)
print(empleado)

empleado = Gerente("daniel",300.0,"facturacion")
print(empleado)