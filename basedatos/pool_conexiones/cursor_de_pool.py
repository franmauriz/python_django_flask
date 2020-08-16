from conexion import Conexion
from logguer_base import logger

class CursorDelPoll:
    def __init__(self):
        self.__conn = None
        self.__cursor = None
    
    #inicio de with
    def __enter__(self):
        logger.debug('Inicio de with metodo __enter__')
        self.__conn = Conexion.obtenerConexion()
        self.__cursor = self.__conn.cursor()
        
        return self.__cursor
    
    #fin de with
    def __exit__(self,exception_type,exception_value,exception_traceback):
        logger.debug(f'se ejecuta el metodo __exit__()')
        if exception_value:
            self.__conn.rollback()
            logger.debug(f'Ocurrio una excepcion: {eception_value}')
        else:
            self.__conn.commit()
            logger.debug(f'Commit de la transaccion')
        #cerramos el cursor
        self.__cursor.close()
        #regresara la conexion al pool
        Conexion.liberarConexion(self.__conn)
        
if __name__ == '__main__':
    with CursorDelPoll() as cursor:
        cursor.execute('SELECT * FROM persona')
        logger.debug('Listado de persona')
        logger.debug(cursor.fetchall())
        