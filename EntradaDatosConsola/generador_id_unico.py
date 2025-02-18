#Sistema generador id único
from random import randint

nombre = str(input('Introduce tu nombre : '))
apellido = str(input('Introduce tu apellido : '))
anio_nacimiento = str(input('Introduce tu año de nacimiento : '))
aleatorio = str(randint(1000, 9999))

nom = nombre[0:2]
ap = apellido[0:2]
anio = anio_nacimiento[-2:]


id = nom+ap+anio+aleatorio
print(f'esto vale : {id}')