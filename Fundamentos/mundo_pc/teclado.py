from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclados = 0
    
    def __init__(self,tipo_entrada,marca):
        Teclado.contador_teclados += 1
        self.__id_teclado = Teclado.contador_teclados
        self._tipo_entrada = tipo_entrada
        self._marca = marca
        
    
    def __str__(self):
        return(
            f"ID: {self.__id_teclado}, "
            f"MARCA: {self._marca}, "
            f"TIPO ENTRADA: {self._tipo_entrada} "
        )
