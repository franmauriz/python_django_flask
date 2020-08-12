import psycopg2

con = psycopg2.connect(user='postgres',
                       password='frandaniel10',
                       host='localhost',
                       port='5432',
                       database='test_db')
cursor = con.cursor()
sql = 'select * from persona where id_persona in %s order by id_persona desc'
entrada = input("Proporciona las pk a buscar (separada por comas):")
tupla = tuple(entrada.split(','))
llaves_primarias = (tupla,)
cursor.execute(sql, llaves_primarias)
registros = cursor.fetchall()
for registro in registros:
    print(registro)
cursor.close()
con.close()