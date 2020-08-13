from logguer_base import logger
import psycopg2 as db
import sys

class Conexion:
    __HOST = 'localhost'
    __USER = 'postgres'
    __PASSWORD = 'frandaniel10'
    __DATABASE = 'test_db'
    __DB_PORT = '5432'
    __conexion = None
    __cursor = None
    
    @classmethod
    def obtenerConexion(cls):
        if cls.__conexion is None:
            try:
                cls.__conexion = db.connect(host=cls.__HOST,
                                            user=cls.__USER,
                                            password=cls.__PASSWORD,
                                            port=cls.__DB_PORT,
                                            database=cls.__DATABASE)
                logger.debug(f'Conexion existosa: {cls.__conexion}')
                return cls.__conexion
            except Exception as e:
                logger.error(f'Error al conectar a la base de datos: {e}')
                sys.exit()
        else:
            return cls.__conexion
        
    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.obtenerConexion().cursor()
                logger.debug(f'Se abrio el cursor con exito: {cls.__cursor}')
                return cls.__cursor
            except Exception as e:
                logger.error(f'Error al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls.__cursor
        
    @classmethod
    def cerrar(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
            except Exception as e:
                logger.error(f'Error al cerrar el cursor: {e}')
        
        if cls.__conexion is not None:
            try:
                cls.__conexion.close()
            except Exception as e:
                logger.error(f'Error al cerrar la conexion: {e}')
        
        logger.debug(f'Se han cerrado los objetos de Cursor y conexion')

if __name__ == '__main__':
    logger.info(Conexion.obtenerCursor())
    Conexion.cerrar()