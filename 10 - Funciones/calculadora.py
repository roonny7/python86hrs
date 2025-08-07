print('*** Calculadora con funciones ***')

def mostrar_menu():
    print(f'''\n Operaciones que puedes realizar
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. Salir''')
    return int(input('Escoge una opción : '))

def pedir_valores():
    operando1 = float(input("Dame el valor 1: "))
    operando2 = float(input("Dame el valor 2: "))
    return operando1, operando2

def ejecutar_operacion(opcion, salir):
    #solicitar los valores de operandos
    if 1 <= opcion <=4:
        operando1, operando2 = pedir_valores()
    resultado = 0
    if opcion == 1: #sumar
        resultado = operando1 + operando2
        print(f'El resultado de la suma de {operando1} + { operando2 } es : {resultado}')

    elif opcion == 2: #restar
        resultado = operando1 - operando2
        print(f'El resultado de la resta de {operando1} - { operando2 } es : {resultado}')

    elif opcion == 3: #multiplicar
        resultado = operando1 * operando2
        print(f'El resultado de la multiplicación de {operando1} * { operando2 } es : {resultado}')

    elif opcion == 4: #dividir
        resultado = operando1 / operando2
        print(f'El resultado de la división de {operando1} / { operando2 } es : {resultado}')

    elif opcion == 5: #salir
        print('Saliendo de la calculadora')
        salir = True

    else:
        print('Opción inválida \n')

    return salir


# Programa principal
if __name__ == '__main__':
    salir = False
    while not salir:
        opcion = mostrar_menu()
        salir = ejecutar_operacion(opcion, salir)
