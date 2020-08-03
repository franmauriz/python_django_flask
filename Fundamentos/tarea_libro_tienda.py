print("Introduzca los datos del libro:")
titulo = input("Titulo del libro:")
id = int(input("ID del libro:"))
precio = float(input("Precio del libro:"))
envioGratuito = input("¿Envio gratuito?:")

if(envioGratuito=="True"):
    envioGratuito=True
elif(envioGratuito=="False"):
    envioGratuito=False
else:
    envioGratuito="Error, el valor tiene que ser igual a True o False"
    
print("Datos del libro:")
print("Titulo:",titulo)
print("ID:",id)
print("Precio:",precio)
print("Envio gratuito:",envioGratuito)