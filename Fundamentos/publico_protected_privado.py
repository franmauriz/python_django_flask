class Persona:
    def __init__(self,nombre,apellido,edad):
        self.nombre = nombre # PUBLICA
        self._apellido = apellido # PROTECTED
        self.__edad= edad # EDAD
        
    def get_edad(self):
        return self.__edad
    
    def set_edad(self,edad):
        self.__edad = edad
    

persona = Persona("Fran","Mauriz",4)

print(persona.nombre) # variable publica se puede acceder desde fuera de la clase

print(persona._apellido) # variable protegida se puede acceder desde fuera pero no se deberia

# print(persona.__edad) # variable privada nos se pude acceder desde fuera de la clase para ello se debe llamar a get o a set

print(persona.get_edad())

