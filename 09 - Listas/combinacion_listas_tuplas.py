print('*** Combinación de Listas y Tuplas ***') #unpacking

# Definir una lista que almacena tuplas de productos.

productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jeans', 30.00),
    ('P003', 'Sudadera', 40.00)
]

# imrpimir la informcación de cada producto
#y además calculamos el precio total
precio_total = 0

print(f'\nInformación de los productos')
for producto in productos:
    id, descripcion, precio = producto
    print(f'\nProducto : ID = { id }, descripcion = { descripcion }, precio = ${ precio }')
    precio_total += precio # producto[2]

print(f'\nPrecio total es : ${ precio_total}')
