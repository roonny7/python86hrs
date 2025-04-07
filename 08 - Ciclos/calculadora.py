print('*** Sistema de administración de cuentas ***')

SALDO_INICIAL = 1000
salir = False
saldo = SALDO_INICIAL
while not salir:
    print(f'''Menú : 
    1. Sumar
    2. Restar
    3. Dividir
    4. Multiplicar
    5. Salir
''')

    opcion = int(input('Escoje una opción : '))
    if 1 <= opcion <5:
        operando1 = float(input('Operando 1 : '))
        operando2 = float(input('Operando 2 : '))

    if opcion == 1:
        suma = operando1 + operando2
        print(f'La suma es : {suma:.2f}')

    elif opcion == 2:
        resta = operando1 - operando2
        print(f'La resta es : {resta:.2f}')


    elif opcion == 3:
        multi = operando1 * operando2
        print(f'La multiplicación es : {multi:.2f}')

    elif opcion == 4:
        division = operando1 / operando2
        print(f'La división es : {division:.2f}')

    elif opcion == 5:
         salir = True

    else:
        print('No hay esa opción')


