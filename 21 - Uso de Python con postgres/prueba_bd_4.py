import psycopg2

conexion = psycopg2.connect(user='postgres',password='123456',host='127.0.0.1',port=5432,database='nigger_bd')

print(conexion)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "INSERT INTO personas (nombre, apellido, email) VALUES (%s, %s, %s)"
            valores = (('Marta', 'Legas', 'martalegas@gmail.com'),
                       ('Mosco', 'verde', 'mosquito@gmail.com'),
                       ('Babas', 'muchas', 'babitas@gmail.com'))
            cursor.executemany(sentencia, valores)
            #conexion.commit() con with no es necesario hacer el comit
            registros_insertados = cursor.rowcount
            print(f'Se insertaron : {registros_insertados} registros')


except Exception as e:
    print(f'Ocurrió un error : {e}')
finally:
    conexion.close()
