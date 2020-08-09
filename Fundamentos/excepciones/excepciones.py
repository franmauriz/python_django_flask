from numeroidenticoexception import NumeroIdenticoException

resultado = None

numero1 = int(input("Proporcione un número: "))
numero2 = int(input("Proporcione otro número:"))

try:
    if numero1 == numero2:
        raise NumeroIdenticoException("Error, números identicos")
    resultado = numero1 / numero2
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
except ValueError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print("No hubo ningún error")
finally:
    print("Se ejecuta siempre haya error o no")
    
    
print(resultado)
print("continuamos")
    