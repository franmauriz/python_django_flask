from usuariodao import UsuarioDao
from usuario import Usuario
from logger_base import logger

opcion=None

while opcion != '5':
    print('GESTION DE USUARIOS')
    print('1- Listar usuarios')
    print('2- Agregar usuarios')
    print('3- Actualizar usuarios')
    print('4- Eliminar usuarios')
    print('5- Salir')
    opcion = input('EScriba una opcion (1-5):')
    print('__________________________________')
    if opcion == '1':
        print('Lista de Usuarios:')
        usuarios = UsuarioDao.select()
        for usuario in usuarios:
            print(usuario)
    elif opcion == '2':
        print('Crear un usuario nuevo:')
        username = input('Indique un nombre de usuairo:')
        password = input('Introduzca un password:')
        usuario = Usuario(username=username,password=password)
        UsuarioDao.insert(usuario)
    elif opcion == '3':
        print('Actualizar un usuario:')
        id_user = input('Indique el id del usuario a actualizar:')
        username = input('Indique un nombre de usuairo a modificar:')
        password = input('Introduzca un password a modificar:')
        usuario = Usuario(id_user=id_user,username=username,password=password)
        UsuarioDao.update(usuario)
    elif opcion == '4':
        print('Eliminar un usuario')
        id_user = input('Indique el id del usuario a eliminar:')
        usuario = Usuario(id_user=id_user)
        UsuarioDao.delete(usuario)
    