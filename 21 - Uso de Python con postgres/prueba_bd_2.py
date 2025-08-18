import psycopg2

conexion = psycopg2.connect(user='postgres',password='123456',host='127.0.0.1',port=5432,database='nigger_bd')

print(conexion)

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = "SELECT * FROM personas WHERE id_persona IN %s"
            #llaves_primarias = ((1,2,3),)
            entrada = input('Proporciona los id a buscar : ')
            llaves_primarias = (tuple(entrada.split(',')), )
            cursor.execute(sentencia, llaves_primarias)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
            #print(registros)

except Exception as e:
    print(f'Ocurrió un error : {e}')
finally:
    conexion.close()
