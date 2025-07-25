print('*** Diccionaros en python ***')

# Creamos n dict de persona con clave y valor
persona = {
    'nombre' : 'Roonny',
    'edad' :    44,
    'ciudad' : 'Chetumal'
}

print(f'Direccionario de persona : {persona}')

# acceder a los elementos del diccionario
print(f'Nombre : {persona['nombre']}')
print(f'Edad : { persona.get('edad')}')
print(f'Ciudad : { persona.get('ciudad')} - {persona['ciudad']}')

# Modificar el valor de un diccionario
persona['edad'] = 45
print(f'Direccionario de persona : {persona}')

# Agregar un nuevo elemento
persona['Ocupacion'] = 'Valedor'
print(f'Direccionario de persona : {persona}')

# ELiminar un elemento del diccionario
del persona['edad']
print(f'Direccionario de persona : {persona}')

persona.pop('Ocupacion')
print(f'Direccionario de persona : {persona}')

# Iterar elementos de un dict (llave, valor)
for llave, valor in persona.items():
    print(f'La llave es : { llave} y su valor es : {valor}')

# Obtener los valores
for valor in persona.values():
    print(f'Valor es : {valor}')

# Obtener las llaves
for llave in persona.keys():
    print(f'Llave es : {llave}')