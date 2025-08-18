import psycopg2

conexion = psycopg2.connect(user='postgres',password='123456',host='127.0.0.1',port=5432,database='nigger_bd')

print(conexion)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "UPDATE personas set nombre=%s, apellido=%s WHERE id_persona = %s"
            valores = ('Elsa', 'borin', 4)
            cursor.execute(sentencia, valores)
            registros_insertados = cursor.rowcount
            print(f'Se actualizaron : {registros_insertados} registros')


except Exception as e:
    print(f'Ocurrió un error : {e}')
finally:
    conexion.close()
