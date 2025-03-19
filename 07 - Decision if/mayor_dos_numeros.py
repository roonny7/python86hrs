print('*** Mayor de dos números ***')

#Pedimos los valores al usuario
numero1  = int(input('Número 1 : ? '))
numero2  = int(input('Número 2 : ? '))

numero_mayor = numero1 if numero1 >= numero2 else numero2

print(f'el mayor es : {numero_mayor}')
