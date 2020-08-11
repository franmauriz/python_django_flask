from dispositivo_entrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_ratones = 0
    
    def __init__(self,tipo_entrada,marca):
        Raton.contador_ratones += 1
        self.__id_raton = Raton.contador_ratones
        self._tipo_entrada = tipo_entrada
        self._marca = marca
        
    def __str__(self):
        return(
            f"ID: {self.__id_raton}, "
            f"MARCA: {self._marca}, "
            f"TIPO ENTRADA: {self._tipo_entrada} "   
        )
