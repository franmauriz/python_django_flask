frutas = ("NARANJA","PLATANO","PERA")

print(frutas)

#LARGO
print(len(frutas))

#ACCEDERE A UN ELEMENTO
print(frutas[0])

#NAVEGACION INVERSA
print(frutas[-1])
print(frutas[-2])

#RANGO
print(frutas[0:2])

#MODIFICAR FRUTAS
#1º CONVERTIMOS LA TUPLA A LISTA
frutaLista = list(frutas)
#2º MODIFICAMOS EL ELMENTO
frutaLista[1]="PLATANITO"
#3º VOLVEMOS A CONVERTIRLO EN TUPLA
frutas=tuple(frutaLista)

print(frutas)

#ITERAR TUPLA
for fruta in frutas:
    print(fruta)
    
#ELIMINAR TUPLA
del frutas
