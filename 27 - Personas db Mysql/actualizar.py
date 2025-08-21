import mysql.connector

personas_db = mysql.connector.connect(
    host='127.0.0.1',
    user = 'root',
    password = '1234567890',
    database = 'nigger_bd'
)

cursor = personas_db.cursor()
sentencia_sql = 'UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id=%s'
valores = ('Victoria', 'Flores', 45, 5)
cursor.execute(sentencia_sql, valores)
personas_db.commit()
print('Se ha modificado la informacion...')
personas_db.close()
