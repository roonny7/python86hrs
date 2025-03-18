print('*** Bienvenidos al sistema ***')

salir_sistema_txt = input('Desear salir del sistema? (Si / No)')
salir_sistema = salir_sistema_txt.strip().lower() == 'si'

if not salir_sistema:
    print('Continuamos en el sistema')
else:
    print('Salimos del sistema')