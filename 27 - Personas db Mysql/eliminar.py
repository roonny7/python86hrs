import mysql.connector

personas_db = mysql.connector.connect(
    host='127.0.0.1',
    user = 'root',
    password = '1234567890',
    database = 'nigger_bd'
)
cursor = personas_db.cursor()
sentencia_sql = 'DELETE FROM personas WHERE id=%s'
valores = (5,)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se ha eliminado el registro')
personas_db.close()