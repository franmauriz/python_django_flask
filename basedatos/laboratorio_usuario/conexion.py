from logger_base import logger
from  psycopg2 import pool
import sys

class Conexion:
    __HOST = 'localhost'
    __USER = 'postgres'
    __PASSWORD = 'frandaniel10'
    __DATABASE = 'laboratorio_usuarios'
    __DB_PORT = '5432'
    __MIN_CON = 1
    __MAx_CON = 5
    __pool = None
    
    @classmethod
    def obtenerPool(cls):
        if cls.__pool is None:
            try:
                cls.__pool = pool.SimpleConnectionPool(cls.__MIN_CON, 
                                                       cls.__MAx_CON,
                                                       host=cls.__HOST,
                                                       user=cls.__USER,
                                                       password=cls.__PASSWORD,
                                                       port=cls.__DB_PORT,
                                                       database=cls.__DATABASE)
                logger.debug('Creacion del pool exitosa: {cls.__pool}')
                return cls.__pool
            except Exception as e:
                logger.error('Error al crear el pool: {e}')
                sys.exit()
        else:
            return cls.__pool
        
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
        logger.debug(f'estado del pool: {cls.__pool}')
        
    @classmethod
    def cerrarConexiones(cls):
        # cerrar pool y todas sus conexiones
        cls.obtenerPool().closeall()
        logger.debug(f'Cerramos el pool: {cls.__pool}')