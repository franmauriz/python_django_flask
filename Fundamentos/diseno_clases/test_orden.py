from producto import Producto
from orden import Orden


producto1 = Producto("camisa",100)
producto2 = Producto("pantalon",300)
producto3 = Producto("calcetin",50)

productos = [producto1,producto2]

orden1 = Orden(productos)
print(orden1)
print("Total pedido: ",str(orden1.cacular_total()))

orden2 = Orden(productos)
orden2.agregarproducto(producto3)

print(orden2)

print("Total pedido: ",str(orden2.cacular_total()))