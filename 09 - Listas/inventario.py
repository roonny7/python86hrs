print('*** Sistema de inventarios ***')

inventario = []

numero_productos = int(input("Cuantos productos al inventario?"))
for indice in range(numero_productos):
    print(f'Proporciona los valores del producto {indice+1}');
    nombre  = input('Nombre : ')
    precio = float(input('Precio : '))
    cantidad = int(input('Cantidad :'))

    # Creamos el diccionario, con el detalle del producto
    producto = {
        "id" : indice,
        "nombre" : nombre,
        "precio" : precio,
        "cantidad" : cantidad
    }

    # agregamos el producto
    inventario.append(producto)


# mostrar inventario inicial
print(f'\nInventario inicial {inventario}')

# buscar producto por id
id_buscar = int(input('\n Ingresa el id del producto a buscar : '))
producto_encontrado = None
for producto in inventario:
    if producto.get('id') == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print(f'''El producto encontrado con 
    id : {producto_encontrado.get('id')} 
    nombre: {producto_encontrado.get('nombre')}
    precio: {producto_encontrado.get('precio')}
    cantidad: {producto_encontrado.get('cantidad')}
    ''')
else:
    print(f'Producto con id {id_buscar} no encontrado')

# mostrar el inventario detallado
print(f'''\nInventario detallado''')
for producto in inventario:
    print(f'''
        id : {producto.get('id')} 
        nombre: {producto.get('nombre')}
        precio: {producto.get('precio')}
        cantidad: {producto.get('cantidad')}
        ''')