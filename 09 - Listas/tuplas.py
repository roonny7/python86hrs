print('*** Manejo de Tuplas ***')

mi_tupla = (1,2,3,4,5)
print(mi_tupla)

# No podemos modificar una tupla
#mi_tupla[2] = 10 # error
#mi_tupla.append() # error

#iterar elementos de tupla
for elemento in mi_tupla:
    print(elemento, end=' ')

# crear una tupla para una coordenada x y y
coordenadas = (3,5)

# accedemos a cada elemento de una tupla
print(f'\nCoordenada en el eje x { coordenadas[0]}')
print(f'\nCoordenada en el eje y { coordenadas[1]}')

# Crear una tupla unitaria
tupla_un_elemento = 10,
print(f'\nTupla de un elemento { tupla_un_elemento}')

# tupla anidadad
tupla_anidada = (1, (2,3), (4,5), 25)
print(f'\nTupla anidada { tupla_anidada}')
print(f'\nSegundo elemento de tupla anidada { tupla_anidada[1]}')