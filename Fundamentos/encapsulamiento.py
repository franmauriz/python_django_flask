class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre
        self.__edad = edad
    
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self,nombre):
        self.__nombre=nombre
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self,edad):
        self.__edad = edad
        
persona = Persona("Fran","40")

print(persona.get_nombre())
print(persona.get_edad())

persona.set_nombre("Roberto")
persona.set_edad(5)


print(persona.get_nombre())
print(persona.get_edad())
