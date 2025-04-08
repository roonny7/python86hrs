print('***Dibujar triángulo ***')

numero_filas = int (input ('Proporciona el número de filas: '))

#itrar sobre cada fila del triángulo
for fila in range (numero_filas+1):
    espacios_blanco = ' ' * (numero_filas - fila)
    #astericos = '*' * (fila * 2 - 1)
    astericos = '*' * fila 
    print(f'{espacios_blanco} {astericos}')