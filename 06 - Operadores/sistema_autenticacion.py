print('*** SISTEMA AUTENTICACIÓN ***')

CUSUARIO = 'aquiles'
CCONTRASENA = 'castro'

usuario = input('Usuiario : ');
contrasenia = input('Contraseña : ');

login_correcto = (usuario.strip().lower() == CUSUARIO
                  and contrasenia.strip().lower() == CCONTRASENA)
print(f'El login es correcto : {login_correcto}')