#Dada la siguiente tupla, crear una lista que sólo incluya los números menor que 5 utilizando un ciclo for: 
numeros = (13, 1, 8, 3, 2, 5, 8)
numerosLista = []

for numero in numeros:
    if numero < 5:
        numerosLista.append(numero)
        
print(numerosLista, end=" ") 