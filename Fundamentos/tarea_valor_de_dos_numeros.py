numero1 = int(input("Proporciona en numero1:"))
numero2 = int(input("Proporciona en numero2:"))

if(numero1 > numero2):
    numeroMayor = numero1
elif(numero1<numero2):
    numeroMayor = numero2
else:
    numeroMayor = 0
    
if(numeroMayor==0):
    print("Son Iguales")
else:
    print("El numero mayor es: ",numeroMayor)
