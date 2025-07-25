print('*** Lista de suscriptores ***')

# Definimos el set inicial
suscriptores = set()

numero_suscriptores = int(input('Cuantos sucriptores?'))
for _ in range(numero_suscriptores-1):
    suscriptores.add(input('Nuevo suscriptor'))

print(f'Lista de suscriptores inicial : {suscriptores}')

# verificar si nuevo suscriptor ya está en la lista
nuevo_suscriptor = input('Nuevo suscriptor?')
if (nuevo_suscriptor in suscriptores):
    print(f'El nuevo suscriptor ya está en la lista')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado a la lista')


print(f'Lista de suscriptores actualizada : {suscriptores}')

# Eliminar un suscritor
suscriptor_eliminar = input('Proporciona el suscriptor a eliminar')

suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} se ha eliminado de la lista')
print(f'Lista de suscriptores actualizada : {suscriptores}')

# Verificar cantidad total de suscriptores
print(f'La cantidad de total de suscriptoes es : {len(suscriptores)}')

# Mostramos total de suscriptores
for suscriptor in suscriptores:
    print(f' - {suscriptor}')