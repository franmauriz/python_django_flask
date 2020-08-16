from conexion import Conexion
from logger_base import logger

class CursorDelPool:
    def __init__(self):
        self.__conn = None
        self.__cursor = None
        
    #inicio del with
    def __enter__(self):
        logger.debug('Inicio de __enter__')
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()
        return self.__cursor
    #fin del with
    def __exit__(self,exception_type,exception_value,exception_traceback):
        logger.debug('incio de __exit__')
        if exception_value:
            self.__conn.rollback()
            logger.debug('Ocurrio una excepcion: {exception_value}')
        else:
            self.__conn.commit()
            logger.debug('Commit')
        
        self.__cursor.close()
        Conexion.liberarConexion(self.__conn)
        