print('*** Playlist de canciones***')

# Creamos una lista vacía
lista_reproduccion = []

numero_canciones = int(input('Cuantas canciones quieres?'))

# iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_canciones):
    cancion = input(f'Proporciona la cancinón { indice + 1 } : ')
    lista_reproduccion.append(cancion)


# Ordenar la lista en orden alfabético. sort
lista_reproduccion.sort()

# iteramos el playlist
print('\nIteramos la playlist')
# Mostrar la lista iterando sus elementos
for cancion in lista_reproduccion:
    print(f' - { cancion }')