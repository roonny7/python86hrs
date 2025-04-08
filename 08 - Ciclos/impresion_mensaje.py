

print( ' *** Repetición de un mensaje *** ')
mensaje = input('Proporcione un mensaje a repetir :')
numero_repeticiones = int (input (' Proporcione el número de repeticiones '))

#iterar sobr eel rango d repeticiones
for i in range(numero_repeticiones):
    print(f'{i+1} - {mensaje}')