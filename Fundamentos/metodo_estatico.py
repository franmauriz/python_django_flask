class MiClase:
    
    variable_clase = "Variable Clase"
    
    def __init__(self):
        self.variable_instancia = "Variable instancia"
    
    @staticmethod
    def metodo_estatico():
        print("Metodo estatico")
        print(MiClase.variable_clase)
        # desde un metodo estatico no podemos acceder a una variable de instancia
        #print(MiClase.variable_instancia)
        
    @classmethod
    def metodo_clase(cls):
        print("Metodo de Clase:" + str(cls))
        print(cls.variable_clase)
        # desde un metodo estatico no podemos acceder a una variable de instancia
        #print(cls.variable_instancia)
        
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()


MiClase.metodo_estatico()
MiClase.metodo_clase()
print("_______")

obj1 = MiClase()

obj1.metodo_instancia()