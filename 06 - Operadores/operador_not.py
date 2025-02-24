print('*** Operador not) ***')
#Regresa verdadero si cualquiera de los valores a evaluar son verdaderos

condicion1 = True
resultado = not condicion1
print(f'Resultado not sobre : { condicion1} es : {resultado}')

#revisar si una variable es cadena vacía
nombre = '1'
es_cadena_vacia = not nombre
print(f'\n La variable no tienen ningún vvalor {es_cadena_vacia}')

#revisar si una variable no tiene ningún valor asignado
variable = None
es_variable_sin_valor = not variable

print(f'La variable no tiene ningín valor asignado : { es_variable_sin_valor}')