print('*** Operadores de asignación ***')
numero = 5
print(f'Valor de número es : {numero}')
numero = 7
print(f'Valor de número es : {numero}')

cadena = " saludos webas "
print(f'Valor de la cadena es : {cadena}')

#Asignación múltiple
x, y, z = 5, 'Hola', -9.15
print(f'Valor de x : {x}, valor de y : {y}, y el valor de z : {z}')

#Asignación encadenada
a = b = c = 10
print(f'Valor de a : {a}, valor de b : {b}, y el valor de c : {c}')

#intercambio de valores de una variable, sin utilizar variables temporales
x, y = 5, 10
print(f'Valores iniiciales de x y y : {x, y}')
#aplicando el concepto de asignación múltiple, intercambiando valores
x, y = y, x
print(f'Valores iniiciales de x y y : {x, y}')

#Recibir multiples valores de la entrada del usaurio
print()
nombre, apellido = input ('Ingresa tu nombre y apellido separados por coma').split(',')

print(f'Nombre : {nombre.strip()}, Apellido : {apellido.strip()}')
