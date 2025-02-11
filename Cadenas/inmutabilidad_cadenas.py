#inmutabilidad en cadenas

cadena1= 'Hola mundo'
#cadena1[0]='h'  #no se puede modificar los caracteres
cadena2=cadena1
cadena1='Adios'

print(cadena1)
print(cadena2)