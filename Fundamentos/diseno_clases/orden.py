class Orden:
    contador_ordenes = 0
    
    def __init__(self,productos):
        Orden.contador_ordenes += 1
        self.__id_orden = Orden.contador_ordenes
        self.__productos = productos
        
    def agregarproducto(self,producto):
        self.__productos.append(producto)
        
    def cacular_total(self):
        total = 0
        for producto in self.__productos:
            total += producto.get_precio()
        return total
        
    def __str__(self):
        
        productos_str = ""
        
        for producto in self.__productos:
            productos_str += producto.__str__() + " ,"
        
        return "ID_ORDEN: " + str(self.__id_orden) + ", PRODUCTOS: " + productos_str