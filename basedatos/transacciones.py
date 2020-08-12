import psycopg2

con = psycopg2.connect(user='postgres',
                       password='frandaniel10',
                       host='localhost',
                       port='5432',
                       database='test_db')
try:
    # con.autocommit = False
    cursor = con.cursor()
    sql = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'
    valores = ('Maria', 'Gonzalez', 'maria@mail.com')
    cursor.execute(sql, valores)

    sql = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'
    valores = ('fran', 'mauriz', 'fran@mail.com', 1)
    cursor.execute(sql, valores)
    # guardamos la informacin en la base de datos
    con.commit()
except Exception as e:
    print(e)
    con.rollback()
finally:
    cursor.close()
    con.close()
