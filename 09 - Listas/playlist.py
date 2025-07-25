print('*** Playlist de canciones***')

# Creamos una lista vacía
lista_reproduccion = []

# Empezamos a agregar canciones
lista_reproduccion.append('Hotel California - Eagles');
lista_reproduccion.append('Staying alive - Bee Gees')
lista_reproduccion.append('Dream on - Aerosmith')

# Ordenar la lista en orden alfabético. sort
lista_reproduccion.sort()

# Mostrar lista de canciones
print(f'\nLista de reproducción en orden alfabético')
print(lista_reproduccion)

# Ordenar la lista en orden alfabético. sort descendente
lista_reproduccion.sort(reverse=True)

# Mostrar lista de canciones
print(f'\nLista de reproducción en orden alfabético descendente')
print(lista_reproduccion)

# iteramos el playlist
print('\nIteramos la playlist')
# Mostrar la lista iterando sus elementos
for cancion in lista_reproduccion:
    print(f' - { cancion }')