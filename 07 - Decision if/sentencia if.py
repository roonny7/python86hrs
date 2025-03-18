from random import random

print(f'*** Sentencia if ***')

edad  = random()*7+5+5
edad = 20
if edad >=18:
    print(f'Eres mayor de edad. Tienes {edad} años')
elif 13<= edad <18:
    print(f'Eres un adolescente. Tienes {edad} años')
else:
    print(f'Eres menor de edad. Tienes {edad} años')