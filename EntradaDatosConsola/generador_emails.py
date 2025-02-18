print('*** Sistema generador de emails ***')
nombre = input('Nombre : ')
apellidos = input('Apellidos')
empresa = input('Empresa : ')
extension_dominio = input('Extensión : ')

#normalizadr los valores recibidos
nombre = nombre.strip().lower().replace(' ','.')
apellidos = apellidos.strip().lower().replace(' ','.')
empresa = empresa.strip().lower().replace(' ','.')
extension_dominio = extension_dominio.strip().lower().replace(' ','')

#generar el email
email = f'{nombre}.{apellidos}@{empresa}{extension_dominio}'

print(f'''
Tu nuevo email generado por sistema es : 
    {email}
    Felicidades puto!!!!!!
''')