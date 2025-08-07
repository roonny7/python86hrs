print('*** Imprimir detalles de una persona usando kwargs ***')

# Función que acepta argumentos variables en forma de llave - valor dict
def imprimir_detalle_persona (**kwargs):
    print('\n Valores recibidos')
    for llave, valor in kwargs.items():
        print(f'{llave} : {valor}')


# Llamar a la función
imprimir_detalle_persona(nombre='Zoquete', edad = 300, ciudad = 'Pakistán')
imprimir_detalle_persona(nombre='Zoquete2', edad = 5000, ciudad = 'Guadalajara', gerente=True)