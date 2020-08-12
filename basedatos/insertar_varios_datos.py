import psycopg2

con = psycopg2.connect(user='postgres',
                       password='frandaniel10',
                       host='localhost',
                       port='5432',
                       database='test_db')
cursor = con.cursor()
sql = 'INSERT INTO persona(nombre,apellido,email) VALUES (%s,%s,%s)'

valores = (('Aida', 'Mauriz', 'aida@mail.com'),
           ('Sonia', 'Mauriz', 'sonia@mail.com'),
           ('Santi', 'Mauriz', 'santi@mail.com'))

cursor.executemany(sql, valores)

# guardamos la informacin en la base de datos
con.commit()
registros_insertados = cursor.rowcount
print(f"Registros insertados: {registros_insertados}")
cursor.close()
con.close()