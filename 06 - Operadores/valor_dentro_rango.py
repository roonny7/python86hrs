VALOR_MINIMO=0
VALOR_MAXIMO=5

# reisar si una variale se encuentra dentro de rango 1 y 10
dato = int(input('Proporciona un dato entero en: '))

#Revisamos si está dentro el rango
esta_dentro_rango = VALOR_MINIMO <= dato <= VALOR_MAXIMO
print(f'Variable está dentro de rango (entre 1 y 5 )? : { esta_dentro_rango}')

#Revisamos la lógica inversa, si el dato está fuera del rango
esta_dentro_rango = not(1 <= dato <= 10)
print(f'Variable está fuera de rango (entre 1 y 10 )? : { esta_dentro_rango}')