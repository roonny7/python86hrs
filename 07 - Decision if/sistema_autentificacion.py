print('*** Sistema de Envíos ***')

C_USUARIO = 'a'
C_CONTRASENA = 'b'

#Pedimos los valores al usuario
usuario  = input('¿ Usuario ? : ')
contrasena  = input('¿ Contraseña ? : ')


mensaje = ''
if usuario == C_USUARIO and contrasena == C_CONTRASENA:
    print('Bienvenido al sistema')
elif usuario != C_USUARIO and contrasena == C_CONTRASENA:
    print('no es el usuario')
elif usuario == C_USUARIO and contrasena != C_CONTRASENA:
    print('no es la contraseña')
else:
    print('ni usuario ni contraseña')

