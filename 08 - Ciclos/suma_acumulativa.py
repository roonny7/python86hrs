print(' *** Suma acumulativa ***')

#sumar los primeros cinco números

MAXIMO = 5
numero = 1
acumulador_suma = 0

#empezamos a iterar
while numero < MAXIMO:
    #imprimir lo que se va a sumar
    print(f' ( acumulador_suma + numero =| { acumulador_suma} + {numero}')
    acumulador_suma += numero
    numero += 1
    print(f'Suma parcial acumulada : { acumulador_suma}')

print(f'El resultado de la suma acumulada es { acumulador_suma}', end = ' \nFin')
