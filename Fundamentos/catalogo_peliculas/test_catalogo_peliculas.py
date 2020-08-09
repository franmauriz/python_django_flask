from dominio.pelicula import Pelicula
from servicio.catalogopeliculas import CatalogoPeliculas

opcion = None

while opcion != "4":
    print("Opciones del Catalogo de Pelicula:")
    print("1- Agregar pelicula.")
    print("2- Listar peliculas.")
    print("3- Eliminar catalogo")
    print("4- Salir")
    print("__________________________________")
    opcion = input("Escribe tu opcion (1-4):")
    if opcion == "1":
        nombre_pelicula = input("Indique el nombre de la pelicula:")
        pelicula = Pelicula(nombre_pelicula)
        CatalogoPeliculas.agregar_pelicula(pelicula)
    elif opcion == "2":
        CatalogoPeliculas.listar_peliculas()
    elif opcion == "3":
        CatalogoPeliculas.eliminar()
    elif opcion == "4":
        pass
    else:
        print("Opcion desconocida")
else:
    print("Salir del programa")

