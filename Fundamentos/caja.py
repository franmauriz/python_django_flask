class Caja:
    def __init__(self,largo,ancho,alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
    
    def calcular_volumen(self):
        return largo * ancho * alto
    
    
largo = float(input("Proporciona el largo de la caja:"))
ancho = float(input("Proporciona el ancho de la caja:"))
alto = float(input("Proporciona el alto de la caja:"))

caja = Caja(largo,ancho,alto)

print("El volumen de la caja es",caja.calcular_volumen())