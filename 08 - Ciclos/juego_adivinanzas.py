from random import randint

print(' *** Juego de adivinanzas ***')

numero_secreto = randint(1,50)
intentos = 0
adivinanza = None
print(f'El número secreto es : { numero_secreto}')

while adivinanza != numero_secreto:
    adivinanza=int(input('Adivina el número secreto (1 - 50):'))
    #agregamos ayuda al usuario
    if adivinanza < numero_secreto:
        print(' el número es mayor ')
    elif adivinanza > numero_secreto:
        print(' el número secreto es menor')

    intentos += 1