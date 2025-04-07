print('*** Sistema de administración de cuentas ***')

salir = False
while not salir:
    print(f'''Menú : 
    1. crear cuenta
    2. Eliminar cuenta
    3. Salir
''')
    opcion = int(input('Escoje una opción : '))
    if opcion == 1:
        print('Creando tu cuenta ', end = '\n')

    elif opcion == 2:
        print('Eliminando tu cuenta ', end = '\n')

    elif opcion == 3:
        print('Saliendo del sistema. Adiós zoquete ', end = '\n')
        salir = True
    else:
        print('No hay esa opción')


