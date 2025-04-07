print('*** Creación y validación de un password ***')

password = input('Ingresa un password, mínimo 6 caracteres :')


#validar el password
while len (password) < 6 :
    print('El password no cumple con los 6 caracteres')
    password = input('Ingresa un nuevo password, mínimo 6 caracteres :')
else:
    print(' El valor del password es válido')