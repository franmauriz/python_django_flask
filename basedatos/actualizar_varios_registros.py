import psycopg2

con = psycopg2.connect(user='postgres',
                       password='frandaniel10',
                       host='localhost',
                       port='5432',
                       database='test_db')
cursor = con.cursor()
sql = 'UPDATE persona SET nombre = %s, apellido = %s, email = %s WHERE id_persona = %s'

valores = (
    ('Francisco', 'Mauriz', 'francisco@mail.com', 1),
    ('Esther', 'Jaime', 'EstherJaime@mail.com', 2)
)

cursor.executemany(sql, valores)

# guardamos la informacin en la base de datos
con.commit()
registros_actualizados = cursor.rowcount
print(f'Registros actualizados: {registros_actualizados}')
cursor.close()
con.close()
