import psycopg2

conexion = psycopg2.connect(user='postgres',password='123456',host='127.0.0.1',port=5432,database='nigger_bd')

print(conexion)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "DELETE FROM personas WHERE id_persona IN %s"
            entrada = input('Proporciona los id a borrar, separados por comas  :')
            valores  = (tuple(entrada.split(',')),)

            cursor.execute(sentencia, valores)
            registros_insertados = cursor.rowcount
            print(f'Se eliminaron : {registros_insertados} registros')


except Exception as e:
    print(f'Ocurrió un error : {e}')
finally:
    conexion.close()
