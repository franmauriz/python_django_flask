a = 3
valorMinimo = 0
valorMaximo = 5

dentroRango = (a >= valorMinimo) and (a <= valorMaximo)

if(dentroRango):
    print("Dentro del Rango")
else:
    print("Fuera del Rango")
    
vacaciones = True
diaDescanso = False

if(vacaciones or diaDescanso):
    print("Podemos ir al parque")
else:
    print("Teienes que trbajar")
    
print(not(vacaciones)) # invierte el valor