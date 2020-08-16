from cursor_de_pool import CursorDelPool
from usuario import Usuario
from logger_base import logger

class UsuarioDao:
    __SELECT = 'SELECT id_user, username, password FROM usuario ORDER BY id_user'
    __INSERT = 'INSERT INTO usuario(username,password) values (%s,%s)'
    __UPDATE = 'UPDATE usuario SET username=%s, password=%s WHERE id_user=%s'
    __DELETE = 'DELETE FROM usuario WHERE id_user=%s'
    
    @classmethod
    def select(cls):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__SELECT))
            cursor.execute(cls.__SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios
    
    @classmethod
    def insert(cls, usuario):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__INSERT))
            logger.debug(f'Usuario a insertar: {usuario}')
            valores = (usuario.get_username(), usuario.get_password())
            cursor.execute(cls.__INSERT,valores)
            return cursor.rowcount
        
    @classmethod
    def update(cls, usuario):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__UPDATE))
            logger.debug(f'Usuario a actualizar: {usuario}')
            valores = (usuario.get_username(), usuario.get_password(),usuario.get_id_user())
            cursor.execute(cls.__UPDATE,valores)
            return cursor.rowcount
        
    @classmethod
    def delete(cls, usuario):
        with CursorDelPool() as cursor:
            logger.debug(cursor.mogrify(cls.__DELETE))
            logger.debug(f'Usuario a borrar: {usuario}')
            valores = (usuario.get_id_user(),)
            cursor.execute(cls.__DELETE,valores)
            return cursor.rowcount

if __name__ == "__main__":
    usuarios = UsuarioDao.select()
    for usuario in usuarios:
       logger.debug(usuario)