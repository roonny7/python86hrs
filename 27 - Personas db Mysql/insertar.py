import mysql.connector

personas_db = mysql.connector.connect(
    host='127.0.0.1',
    user = 'root',
    password = '1234567890',
    database = 'nigger_bd'
)

cursor = personas_db.cursor()
sentencia_sql = 'INSERT INTO personas (nombre, apellido, edad) VALUES (%s, %s, %s)'
valores = ('Victor', 'Ramos', 46)

cursor.execute(sentencia_sql, valores)
personas_db.commit()
personas_db.close()
