from logguer_base import logger
from psycopg2 import pool
import sys

class Conexion:
    __HOST = 'localhost'
    __USER = 'postgres'
    __PASSWORD = 'frandaniel10'
    __DATABASE = 'test_db'
    __DB_PORT = '5432'
    __MIN_CON = 1
    __MAx_CON = 5
    __POOL = None
  
    
    @classmethod
    def obtenerPool(cls):
        if cls.__POOL is None:
            try:
                cls.__POOL = pool.SimpleConnectionPool(cls.__MIN_CON, 
                                                       cls.__MAx_CON,
                                                       host=cls.__HOST,
                                                       user=cls.__USER,
                                                       password=cls.__PASSWORD,
                                                       port=cls.__DB_PORT,
                                                       database=cls.__DATABASE)
                logger.debug(f'Creacion de pool exitosa: {cls.__POOL}')
                return cls.__POOL
            except Exception as e:
                logger.error(f'Error al crear el pool de conexiones: {e}')
                sys.exit()
        else:
            return cls.__POOL
    
    @classmethod
    def obtenerConexion(cls):
        # obtener una conexion de tipo pool
        conexion = cls.obtenerPool().getconn()
        logger.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion
    
    @classmethod
    def liberarConexion(cls,conexion):
        # regresar el objeto al pool
        cls.obtenerPool().putconn(conexion)
        logger.debug(f'regresamos la  conexion al pool: conexion')
        logger.debug(f'estado del pool: {cls.__POOL}')
        
    @classmethod
    def cerrarConexiones(cls):
        # cerrar pool y todas sus conexiones
        cls.obtenerPool().closeall()
        logger.debug(f'Cerramos el pool: {cls.__POOL}')

if __name__ == '__main__':
    # obtener una conexion por el pool
    conexion1 = Conexion.obtenerConexion()
    conexion2 = Conexion.obtenerConexion()
    # regresar conexiones al pool
    Conexion.liberarConexion(conexion1)
    Conexion.liberarConexion(conexion2)
    # Cerrar pool
    Conexion.cerrarConexiones() 