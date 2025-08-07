print('*** Factorial del número 5 ***')

# Definimos la función recursiva

def factorial_recursiva(numero):
    # caso base, factorial de 0! es 1, 1! = 1
    if numero == 0 or numero == 1:
        print(f'Resultado factorial parcial {numero} es 1')
        return 1
    else: #Caso recursivo
        factorial_parcial = numero * factorial_recursiva(numero - 1)
        print(f'Resuultado factorial parcial {numero} es : {factorial_parcial}')
        return factorial_parcial

numero = 100
resultado = factorial_recursiva(numero)
print(f'El factorial de {numero} es {resultado}')