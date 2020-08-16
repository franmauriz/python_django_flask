
from persona import Persona
from cursor_de_pool import CursorDelPoll
from logguer_base import logger

class PersonaDao:
    __SELECCIONAR = 'SELECT * FROM persona ORDER BY id_persona'
    __INSERTAR = 'INSERT INTO persona(nombre, apellido, email) VALUES (%s,%s,%s)'
    __ACTUALIZAR = 'UPDATE persona SET nombre=%s ,apellido = %s, email=%s WHERE id_persona = %s'
    __ELIMINAR = 'DELETE FROM persona WHERE id_persona = %s'

    @classmethod
    def seleccionar(cls):
         with CursorDelPoll() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECCIONAR))
            cursor.execute(cls.__SELECCIONAR)
            registros = cursor.fetchall()
            personas = []
            for registro in registros:
                persona = Persona(registro[3], registro[0], registro[1], registro[2])
                personas.append(persona)
            return personas
    
    @classmethod
    def insertar(cls, persona):
        with CursorDelPoll() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERTAR))
            logger.debug(f'Person a insertar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email())
            cursor.execute(cls.__INSERTAR,valores)
            return cursor.rowcount
        
    @classmethod
    def actualizar(cls, persona):
       with CursorDelPoll() as cursor:
            logger.debug(cursor.mogrify(cls.__ACTUALIZAR))
            logger.debug(f'Person a actualizar: {persona}')
            valores = (persona.get_nombre(), persona.get_apellido(), persona.get_email(),persona.get_id_persona())
            cursor.execute(cls.__ACTUALIZAR,valores)            
            return cursor.rowcount
       
            
    @classmethod
    def eliminar(cls, persona):
        with CursorDelPoll() as cursor:
            logger.debug(cursor.mogrify(cls.__ELIMINAR))
            logger.debug(f'Person a eliminar: {persona}')
            valores = (persona.get_id_persona(),)
            cursor.execute(cls.__ELIMINAR,valores)           
            return cursor.rowcount       


if __name__ == '__main__':
    personas = PersonaDao.seleccionar()
    for persona in personas:
       logger.debug(persona)
    # persona = Persona(nombre='javier',apellido='perez',email='javi@mail.com')
    # num_registro = PersonaDao.insertar(persona)
    # logger.debug(f'Registros insertados: {num_registro}')
    
    # persona = Persona(12,'fernando','gonzalez','fernando@mail.com')
    # num_reg = PersonaDao.actualizar(persona)
    # logger.debug(f'Registros actualizados: {num_reg}')
    
    # persona = Persona(id_persona=13)
    # num_reg = PersonaDao.eliminar(persona)
    # logger.debug(f'Registros actualizados: {num_reg}')
    