print('*** Sistema de calificaciones ***')

#Pedimos los valores al usuario
calificacion  = int(input('¿ Calificación (0-10) ? : '))

calificacionnota= None
if 9 <= calificacion <= 10:
    calificacionnota= 'A'
elif calificacion >= 8 and calificacion < 9:
    calificacionnota = 'B'
elif calificacion >= 7 and calificacion < 8:
    calificacionnota = 'C'
elif calificacion >= 6 and calificacion < 7:
    calificacionnota = 'D'
elif calificacion >= 0 and calificacion < 6:
    calificacionnota = 'F'
else:
    calificacionnota = 'Valor desconocido.'

print(f'Wey, sacaste  : {calificacionnota}')
