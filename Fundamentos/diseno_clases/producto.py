class Producto:
    contador_productos = 0
    
    def __init__(self,nombre,precio):
        Producto.contador_productos += 1
        self.__id_producto = Producto.contador_productos
        self.__nombre = nombre
        self.__precio = precio
        
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.nombre = nombre
        
    def get_precio(self):
        return self.__precio
    
    def set_precio(self,precio):
        self.precio = precio
    
    def __str__(self):
        return "ID_PRODUCTO: " + str(self.__id_producto) +" , NOMBRE: " + self.__nombre + " , PRECIO: " + str(self.__precio) 
        