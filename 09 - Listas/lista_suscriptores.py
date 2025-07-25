print('*** Lista de suscriptores ***')

suscriptores = {'luisa@gmail.com', 'marcos@gmail.com', 'elena@gmail.com'}
print(f'Lista de suscriptores inicial : {suscriptores}')

# verificar si nuevo suscriptor ya está en la lista
nuevo_suscriptor = 'marcos2@gmail.com'
if (nuevo_suscriptor in suscriptores):
    print(f'El nuevo suscriptor ya está en la lista')
else:
    suscriptores.add(nuevo_suscriptor)
    print(f'El nuevo suscriptor se ha agregado a la lista')


print(f'Lista de suscriptores actualizada : {suscriptores}')

# Eliminar un suscritor
suscriptor_eliminar = 'elena@gmail.com';
suscriptores.remove(suscriptor_eliminar)
print(f'El suscriptor {suscriptor_eliminar} se ha eliminado de la lista')
print(f'Lista de suscriptores actualizada : {suscriptores}')

# Verificar cantidad total de suscriptores
print(f'La cantidad de total de suscriptoes es : {len(suscriptores)}')

# Mostramos total de suscriptores
for suscriptor in suscriptores:
    print(f' - {suscriptor}')