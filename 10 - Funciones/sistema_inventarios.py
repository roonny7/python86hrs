print('*** Sismtema de inventarios ***')

# Inventario del almacén
inventario = [
    {'id' : 1, 'nombre' : 'Camisa', 'precio' : 25.99, 'cantidad' : 50},
    {'id' : 2, 'nombre' : 'Pantalones', 'precio' : 39.99, 'cantidad' : 30},
    {'id' : 3, 'nombre' : 'Zapatos', 'precio' : 49.99, 'cantidad' : 20}

]


# Función para mostrar el inventario
def mostrar_inventario():
    print('--- Inventario del Almacén ---')
    for producto in inventario:
        print(f'Id : { producto.get('id')}, Nombre : { producto.get('nombre')}, Precio : ${ producto.get('precio')}, Cantidad : { producto.get('cantidad')}')

def agregar_producto():
    #pass
    print('--- Agregar nuevo producto ---')
    id = int(input('Id : '))
    nombre = input('Nombre : ')
    precio = float(input('Precio : '))
    cantidad = int(input('Cantidad'))
    nuevo_producto = { 'id' : id, 'nombre' : nombre, 'precio' : precio, 'cantidad' : cantidad}
    inventario.append(nuevo_producto)
    print('Producto agregado al inventario ')

def buscar_producto_por_id():
    print('Buscar producto por id')
    id_buscar = int(input('Ingresa id a buscar : '))
    for producto in inventario:
        if producto.get('id') == id_buscar:
            print(f'Id : { producto.get('id')}, Nombre : { producto.get('nombre')}, Precio : ${ producto.get('precio')}, Cantidad : { producto.get('cantidad')}')
            return
    print('\nProducto no encontrado')


# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n Menú
    1. Mostrar menú
    2. Agregar nuevo producto
    3. Buscar producto por id
    4. Salir''')
        opcion = int(input('Proporciona una opción : '))

        # revisamos las opciones del menú
        if opcion == 1 : # Mostrar inventario
                mostrar_inventario()
        elif opcion == 2 : #Agregar nuevo producto
            agregar_producto()
        elif opcion == 3 :
            buscar_producto_por_id()
        elif opcion == 4:
            print('Hasta luego, zoquete')
            break
        else:
            print('Opción no valida, animal . 1-4')

