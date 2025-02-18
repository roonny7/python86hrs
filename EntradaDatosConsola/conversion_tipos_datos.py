#Conversión de tipos de datos

#Convertir de cadena a número
numero_cadena = '10'

numero_entero = int(numero_cadena)
print(f'Valor numérico en cadena: {numero_cadena}')
print(f'Cadena a entero : {numero_cadena}')

#convetir de cadena a flotante
numero_cadena = '3.14'
numero_flotante = float(numero_cadena)
print(f'Cadena a flotante {numero_flotante}')

#convertir de número a cadena
numero_entero = 25
numero_cadena = str(numero_entero)
print(f'Número a cadena : {numero_cadena}')

#convertir a boolean
#Tipo bool es False en los siguientes casos
#Si el valor 0, cadena vacía, o None, entonces regresa False
#Regresa verdadero, si el valor es distinto de 0, si es distinto
#de cadena vacío y si es distnto de None

numero_entero = 0
booleano = bool(numero_entero)
print(f'Valor booleano de 0 es : {booleano}')

numero_entero = 5
booleano = bool(numero_entero)
print(f'Valor booleano de 5 es : {booleano}')

cadena = '' # el largo de la cadena es 0
booleano = bool(cadena)
print(f'Valor booleano de cadena vacía es : {booleano}')#falso,
#incluye colecciones vacías

cadena = 'Cadena con valor '
booleano = bool(cadena)
print(f'Valor booleano de cadena no vacía es : {booleano}')

variable = None
booleano=bool(variable)
print(f'El valor booleano de None es : {booleano}')