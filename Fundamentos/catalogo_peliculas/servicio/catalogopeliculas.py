import os

class CatalogoPeliculas:
    ruta_archivo ="peliculas.txt"
    
    @staticmethod
    def agregar_pelicula(pelicula):
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo,"a")
            archivo.write(pelicula.__str__())
        except Exception as e:
            print(e)
        finally:
            archivo.close()
            
    @staticmethod
    def listar_peliculas():
        try:
            archivo = open(CatalogoPeliculas.ruta_archivo,"r")
            print("Catálogo de Películas:\n")
            print(archivo.read())
            print("\n")
        except Exception as e:
            print(e)
        finally:
            archivo.close()
            
    @staticmethod
    def eliminar():
        try:
            os.remove(CatalogoPeliculas.ruta_archivo)
            print("Archivo Eliminado: " + CatalogoPeliculas.ruta_archivo)
        except Exception as e:
            print(e)    