print( '*** Operaciones con set ***')

a = {1,2,3,4}
b = {3,4,5,6}

union = a | b
print(f'Unión de a | b {union}')

interseccion = a & b
print(f'Intersección de a & b {interseccion}')

diferencia = a - b
print(f'Intersección de a - b {diferencia}')