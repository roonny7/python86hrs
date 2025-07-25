print('*** Manejo de Sets ***')

# Crear un conjunto
mi_set = {1,2,3,4,5,4}
print(mi_set)

# Agregar elementos al set
mi_set.add(6)
mi_set.add(7)
print(f'Mi set modificado es : {mi_set}')

mi_set.add(3)
print(f'Mi set modificado 2 es : {mi_set}')
print(f'Existe el valor de 4 en el set? {4 in mi_set}')

# Eliminar un elemento del conjunto
mi_set.remove(4)
print(f'Mi set modificado 3 es : {mi_set}')

# Iterar los elementos del set
for elemento in mi_set:
    print(elemento, end='*')

# Comprobar si existe un elemento en el set
print(f'Existe el valor de 4 en el set? {4 in mi_set}')

# Obtener la longitud del set
print(f'Longitud del conjunto : {len(mi_set)}')