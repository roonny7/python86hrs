print('*** Sistema de administración de cuentas ***')

SALDO_INICIAL = 1000
salir = False
saldo = SALDO_INICIAL
while not salir:
    print(f'''Menú : 
    1. Depositar
    2. Retirar
    3. Consultar saldo
    4. Salir
''')

    opcion = int(input('Escoje una opción : '))
    if opcion == 1:
        deposito = float(input('Importe a depositar : '))
        saldo += deposito

    elif opcion == 2:
        retiro = float(input('Importe a retirar : '))
        saldo -= retiro

    elif opcion == 3:
        print(f'Tu saldo es : {saldo:.2f} ', end = '\n')

    elif opcion == 4:
        print('Saliendo del sistema. Adiós zoquete ', end = '\n')
        salir = True
    else:
        print('No hay esa opción')


