import psycopg2

con = psycopg2.connect(user='postgres',
                       password='frandaniel10',
                       host='localhost',
                       port='5432',
                       database='test_db')
cursor = con.cursor()
sql = 'select id_persona, nombre from persona where id_persona = %s order by id_persona desc'
id_persona = 1
llave_primaria = (id_persona,)
cursor.execute(sql,llave_primaria)
registros = cursor.fetchall()
print(registros[0][1])
cursor.close()
con.close()
