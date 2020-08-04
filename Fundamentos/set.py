planetas = {"Marte","Jupiter","Venus"}

#Largo
print(len(planetas))

#Comprobar si existe un elmento
print("Marte" in planetas)

#Agregar
planetas.add("Tierra")

print(planetas)

#Eliminar
planetas.remove("Tierra")

print(planetas)

#Limpiar
planetas.clear()

#Eliminar planetas
del planetas