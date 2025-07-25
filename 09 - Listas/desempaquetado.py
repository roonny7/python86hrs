print('*** Desempaquetado de Tuplas ***') #unpacking

producto = ('P001', 'Camisa', 20.00)

# Desempaquetado
id, descripcion, precio = producto

# Imprimir valores
print(f'\nTupla completa : { producto}')
# valores independientes ya desempaquetados
print(f'\nProducto : ID = { id }, descripcion = { descripcion }, precio = { precio }')