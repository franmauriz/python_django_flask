diccionario = {
    "IDE":"Integrated develoment",
    "OOP":"Object oriente p",
    "DBMS":"Database"
}

#largo
print(len(diccionario));

#Acceder a un elemento
print(diccionario["IDE"])

#otra forma de acceder
print(diccionario.get("IDE"))

#Modificar un elmento
diccionario["IDE"]="INTEGRATED DEVELOMENT"

#Iterar los elementos

for termino in diccionario:
    print(termino)
    
for termino in diccionario:
    print(diccionario[termino])
    
for valor in diccionario.values():
    print(valor)
    
#Comprobar si un elemento existe
print("IDE" in diccionario)

#Agregar elemento
diccionario["PK"]="Primary Key"

#Borrar elementos
diccionario.pop("DBMS")

#Limpiar elementos
diccionario.clear()

#Eliminar diccionario
del diccionario


