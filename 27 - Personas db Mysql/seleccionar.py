import mysql.connector

personas_db = mysql.connector.connect(
    host='127.0.0.1',
    user = 'root',
    password = '1234567890',
    database = 'nigger_bd'
)

cursor = personas_db.cursor()
cursor.execute('SELECT nombre, apellido FROM personas')
resultado = cursor.fetchall()
for persona in resultado:
    print(persona)
