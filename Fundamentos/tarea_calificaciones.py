#El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:

# El usuario proporcionará un valor entre 0 y 10.

# Si está entre 9 y 10: imprimir una A

# Si está entre 8 y menor a 9: imprimir una B

# Si está entre 7 y menor a 8: imprimir una C

# Si está entre 6 y menor a 7: imprimir una D

# Si está entre 0 y menor a 6: imprimir una F

# cualquier otro valor debe imprimir: Valor desconocido

calificacion = int(input("Proporciona un valor entre 0 y 10: "))
nota=None

if calificacion >= 0 and calificacion < 6:
    nota = "F"
elif calificacion >= 6 and calificacion < 7:
    nota = "D"
elif calificacion >= 7 and calificacion < 8:
    nota = "C"
elif calificacion >= 8 and calificacion < 9:
    nota = "B"
elif calificacion >= 9 and calificacion <=10:
    nota = "A"
else:
    nota = "Valor desconocido"
    
print(nota)