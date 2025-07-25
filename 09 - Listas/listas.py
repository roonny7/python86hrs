print('*** Manejo de listas***')
#[]
mi_lista =  [1,2,3,4,5]
print(f'{mi_lista} ---° Lista original')

#largo de una lista
print(f'Largo de una lista {len(mi_lista)}')

# acceder a los elementos dela lista por indice
print(f'Accedemos al valor del indice 4 : {mi_lista[4]}')
print(f'Accedemos al valor del indice 4 : {mi_lista[-1]}')

#Modificar los elementos de una lista
mi_lista[1] = 200
print(f'{mi_lista} ---° Lista editada')

#Agregar nuevo elemento
mi_lista.append(700)
print(f'{mi_lista} ---° Lista con extra')

#añadir un nuevo elemento en un índice específico
mi_lista.insert(3,900)
print(f'{mi_lista} ---° Lista con indice')

#Eliminar elementos de una lista
mi_lista.remove(900)
print(f'{mi_lista} ---° Lista borrada')

#remover por índica
mi_lista.pop(2) #remueve el elemento del indice 2
print(f'{mi_lista} ---° Lista borrada por índice')

#Eliminar usando la palabra del
del mi_lista[2]
print(f'{mi_lista} ---° Lista borrada por índice')

#obtener sublistas
sub_lista = mi_lista[1:3] #Genera una sublista del indice 1 al 2, (3 no se incluye)
print(f'{sub_lista} ---° Lista borrada por índice')