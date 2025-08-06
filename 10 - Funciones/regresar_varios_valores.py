print('*** Regresar una tupla de valores desde una función ***')

#Definición de la función
def personas_mayusculas(nombre, apellido, edad):
    print(f'Esta función regresa varios valores (tupla)')
    return (nombre.upper(), apellido.upper(), edad)

#Programa principal
nombre, apellido, edad = personas_mayusculas('Sandra', 'Jimenez', 43)
print(f'Resultado persona : nombre = {nombre}, apellido = {apellido}, edad = {edad}')
