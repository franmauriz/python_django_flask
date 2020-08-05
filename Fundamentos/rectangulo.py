class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return self.base * self.altura
    
base = float(input("Proporciona la base del Rectangulo:"))
altura = float(input("Proporciona la altura del Rectangulo:"))

rectangulo = Rectangulo(base,altura)
print("El area del rectangulo es",rectangulo.calcularArea())