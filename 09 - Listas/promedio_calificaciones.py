print('*** Promedio de calificaciones ***')

# Creamos una lista vacía
Calificaciones = []
Suma = 0
numero_calificaciones = int(input('Cuantas calificaciones a evaluar?'))

# iteramos cada elemento de la lista para agregar un nuevo elemento
for indice in range(numero_calificaciones):
    calificacion = float(input(f'Proporciona la calificación [{ indice + 1 }] : '))
    Calificaciones.append(calificacion)
    Suma = Suma + calificacion

# Sumar lista
suma_calificaciones = sum(Calificaciones)

promedio = Suma / numero_calificaciones
promedio2 = suma_calificaciones / numero_calificaciones

# Promedio
print(f'\nEl promedio es : {promedio:.2f}')
