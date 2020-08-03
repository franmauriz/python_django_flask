condicion = False

if condicion == True:
    print("la condicion es verdadera")
elif condicion == False:
    print("la condicion es falsa")
else:
    print("la condicion no es reconocida")
    
    
numero = int(input("Introduce un número del 1 al 3:"))

if numero == 1:
    numeroTexto="UNO"
elif numero == 2:
    numeroTexto="DOS"
elif numero == 3:
    numeroTexto="TRES"
else:
    print("Valor fuera de rango")
    
print("El número es", numeroTexto)