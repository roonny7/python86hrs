from typing import get_origin

print('*** Ciclo for ***')

cadena = ' Hola zoquetes, hijos de la guanábana verde'
#iteramos los caracteres

for letra in cadena :
    print(letra, end='-')

print('\nRecorremos la lista de frutas')
frutas = ['Plátano', 'Fresa', 'Mango']

for fruta in frutas :
    print(fruta, end = ' \n')