import psycopg2

con = psycopg2.connect(user='postgres',
                       password='frandaniel10',
                       host='localhost',
                       port='5432',
                       database='test_db')
cursor = con.cursor()
sql = 'select * from persona'
cursor.execute(sql)
registros = cursor.fetchall()
print(registros)
cursor.close()
con.close()
