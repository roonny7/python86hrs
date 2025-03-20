print('*** Sistema de Envíos ***')

TARIFA_NACIONAL = 10
TARIFA_INTL = 20

#Pedimos los valores al usuario
destino  = input('¿ Destino del paquete ? : ')
peso  = float(input('¿ peso paquete en kgs ? : '))


costo_envio= None
if destino.strip().lower() == 'nacional':
    costo_envio = peso * TARIFA_NACIONAL
elif destino.strip().lower() == 'internacional':
    costo_envio = peso * TARIFA_INTL
else:
    print('destino mal')

if costo_envio is not None:
    print(f'El costo del envio es : ${costo_envio:.2f}')


