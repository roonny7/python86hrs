#Valores aleatorios con la función randint
#import random así ya no

from random import randint

# Generar número aleatorio entre 1 y 10
numero = randint(1,10)

print(f'El número es : {numero}')

#Simular un dado de 6 caras
dado = randint(1,6)
print(f'El resultado de lanzar el dado es : {dado}')