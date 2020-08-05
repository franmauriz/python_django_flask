class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

# Modificar datos
Persona.nombre ="Juan"
Persona.edad = 12


print(Persona.nombre)
print(Persona.edad)

#crear objetos
persona = Persona("fran",20)

print(persona.nombre)
print(persona.edad)

persona = Persona("esther",40)

print(persona.nombre)
print(persona.edad)