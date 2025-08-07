from Python86hrs.Variables.tienda_online import producto

print('*** Sismtema de máquina de snacks ***')

# Lista de snacks inicial
snacks = [
    {'id' : 1, 'nombre' : 'Papas', 'precio' : 25.99},
    {'id' : 2, 'nombre' : 'Refresco', 'precio' : 39.99},
    {'id' : 3, 'nombre' : 'Sandwiche', 'precio' : 49.99}

]

#Lista de productos ( vacía) son los snacks ya comprados
productos = []

def mostrar_snacks():
    print('--- Mostrar snacks ---')
    for snack in snacks:
        print(f'Id : { snack.get('id')}, Nombre : { snack.get('nombre')}, Precio : ${ snack.get('precio')}')

def buscar_snack_por_id(id_buscar):
    for snack in snacks:
        if snack.get('id') == id_buscar:
            return snack
    #si llegamos al final y no se ecnontró , regrsesa none
    return None


def comprar_snacks():
    print('Comprar snack')
    id_snack = int(input('Qué snack quieres comprar?: '))
    snack_encontrado = buscar_snack_por_id(id_snack)
    if snack_encontrado is not None:
        productos.append(snack_encontrado)
        print(f'Snack agregado : {snack_encontrado}')
    else:
        print(f'Snack no encontrado con id  {id_snack}')

def mostrar_ticket():
    ticket = f'--- Ticket de venta ---'
    total = 0
    for producto in productos:
        ticket += f'\n\t - {producto.get('nombre')} - ${producto.get('precio')}'
        total += producto.get('precio')
    ticket += f'\n\tTOTAL -|| ${total:2f} '
    print(ticket)

def agregar_producto():
    #pass
    print('--- Agregar nuevo producto ---')
    id = int(input('Id : '))
    nombre = input('Nombre : ')
    precio = float(input('Precio : '))
    cantidad = int(input('Cantidad'))
    nuevo_producto = { 'id' : id, 'nombre' : nombre, 'precio' : precio, 'cantidad' : cantidad}
    #inventario.append(nuevo_producto)
    print('Producto agregado al inventario ')


# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n Menú
        1. Mostrar snacks
        2. Comprar snack
        3. Mostrar ticket
        4. Salir''')
        opcion = int(input('Proporciona una opción : '))

        # revisamos las opciones del menú
        if opcion == 1 : # Mostrar inventario
            mostrar_snacks()
        elif opcion == 2 : #Agregar nuevo producto
            comprar_snacks()
        elif opcion == 3 :
            mostrar_ticket()
        elif opcion == 4:
            print('Hasta luego, zoquete')
            break
        else:
            print('Opción no valida, animal . 1-4')

