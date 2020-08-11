from orden import Orden
from computadora import Computadora
from monitor import Monitor
from raton import Raton
from teclado import Teclado

teclado = Teclado("USB", "HP")
raton = Raton("USB", "HP")
monitor = Monitor("HP", "27 pulgadas")
computadora = Computadora("HP", monitor, teclado, raton)


teclado2 = Teclado("USB", "ACER")
raton2 = Raton("USB", "ACER")
monitor2 = Monitor("ACER", "27 pulgadas")
computadora2 = Computadora("ACER", monitor2, teclado2, raton2)

computadoras = [computadora, computadora2]

orden = Orden(computadoras)

print(orden)
