print('*** Función con argumentos por nombre')

def imprimir_persona(nombre, apellido='West', edad='0'):
    print(f'Persona : nombre = {nombre}, apellido = {apellido}, edad = {edad}')

#Primero llamamos la función pasando los argumentos de manera posicional
imprimir_persona('Bruno', 'Diaz', 30)

#llamar la función usando argumentos por nombre
imprimir_persona(nombre='Pedro', apellido='Parques', edad='23')

#llamar la función cmaibnado el orden
imprimir_persona(nombre='Miguel', edad='40', apellido='O\'hara' )

#argumentos con valor por default
imprimir_persona(nombre='Wallace', apellido='West' )
