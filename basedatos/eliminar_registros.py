import psycopg2

con = psycopg2.connect(user='postgres',
                       password='frandaniel10',
                       host='localhost',
                       port='5432',
                       database='test_db')
cursor = con.cursor()
sql = 'DELETE FROM persona WHERE id_persona = %s'

valores = (10,)

cursor.execute(sql, valores)

# guardamos la informacin en la base de datos
con.commit()
registros_eliminados = cursor.rowcount
print(f'Registros eliminados: {registros_eliminados}')
cursor.close()
con.close()