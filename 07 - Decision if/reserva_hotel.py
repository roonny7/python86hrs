print('*** Sistema de reserva de hotel ***')

#Constantes
TARIFA_VISTA_AL_MAR = 150.5
TARIFA_SIN_VISTA_AL_MAR = 190.5

#Pedimos los valores al usuario
nombre_cliente = input('Cuál es tu nombre? ')
dias_estadia = int(input('Cuantos días te quedas? '))
vista = input('Con vista al mar? ')

vista_al_mar = True if vista.strip().lower()=='si' else False

#Calorías quemadas
if vista_al_mar:
    tarifa = dias_estadia * TARIFA_VISTA_AL_MAR
    vista_mar_txt = 'Sí'
else:
    tarifa = dias_estadia * TARIFA_SIN_VISTA_AL_MAR
    vista_mar_txt = 'No'

#mostramos la información
print(f'\n Cliente : { nombre_cliente }')
print(f'Días de estadía : {dias_estadia}')
print(f'Costo total : { tarifa:.2f}')
print(f'Habitación con vista al mar? {vista_mar_txt}')
