from cliente_dao import ClienteDAO
from cliente import Cliente

print('*** Clientes de zona fit Gym')
opcion = None
while opcion != 5:
    print('''Menú
    1. Listar clientes
    2. Agregar cliente
    3. Modificar cliente
    4. Eliminar cliente
    Salir
    ''')
    opcion = int(input('Escribe tu opcion'))

    if opcion == 1: #Listar clientes
        clientes = ClienteDAO.seleccionar()
        print('\n***Listado de clientes ***')
        for cliente in clientes:
            print(cliente)
        print()

    elif opcion == 2 : #Agregar cliente
        nombre_var = input('Escribe el nombre : ')
        apellido_var = input('Escribe el apellido : ')
        membresia_var = input('Escribe la membresía : ')
        cliente = Cliente(nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        clientes_insertados = ClienteDAO.insertar(cliente)
        print(f'Clientes insertados : {clientes_insertados}\n')

    elif opcion == 3 : #Actualizar
        id_cliente_var = int(input('Escribe el id : '))
        nombre_var = input('Escribe el nombre : ')
        apellido_var = input('Escribe el apellido : ')
        membresia_var = input('Escribe la membresía : ')
        cliente = Cliente(id=id_cliente_var, nombre=nombre_var, apellido=apellido_var, membresia=membresia_var)
        clientes_actualizados = ClienteDAO.ACTUALIZAR(cliente)
        print(f'Clientes actualizados : {clientes_actualizados}\n')

    elif opcion == 4 : #Actualizar
        id_cliente_var = int(input('Escribe el id : '))
        cliente = Cliente(id=id_cliente_var)
        clientes_eliminados = ClienteDAO.ELIMINAR(cliente)
        print(f'Clientes eliminados : {clientes_eliminados}\n')

else:
    print('Salimos de la aplicación')
