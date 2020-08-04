nombres = ["fran","esther","roberto","daniel"]

print(nombres)

# largo de la lista
print(len(nombres))

#Acceder a un elemento
print(nombres[0])

#Navegacion inversa
print(nombres[-1])
print(nombres[-2])

#Recuperar un rango de la lista
print(nombres[0:3]) # sin incluir el indice 3

print(nombres[:3]) # mostar la lista hasta el indice indicado sin incluirlo

print(nombres[2:]) # mostrar la lista hasta el final desde el indice indicado

#Cambiar un elemento de la lista
nombres[0]="francisco"
print(nombres)

#Iterar la lista
for nombre in nombres:
    print(nombre)
    
#Comprobar si existe un elmento en la lista
if "esther" in nombres:
    print("Si esther existe en la lista")
else:
    print("No existe esther en la lista")
    
#Agregar un nuevo elemento en la lsita

nombres.append("Juan")
print(nombres)

#Agregar un nuevo elemento en el indice indicado

nombres.insert(1,"Alberto")
print(nombres)

#Borrar un elmento
nombres.remove("Alberto")

#Borrar el ultimo elemento de la lista
nombres.pop()

#Borrar un elemento indicando el indice
del nombres[0]

#Limpiar todos los elementos de la lista
nombres.clear()

#Eliminar por completo la lista
del nombres