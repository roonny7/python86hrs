# *args - arguments tupla
# **kwargs keyword arguments (key, value) como un dict

print('*** Argumentos variables en forma de dict ***')

def superheroes_superpoderes(nombre, *args, **kwargs):
    print(f'Superhéroe : {nombre} - {args} - Mas info : {kwargs}')
    # Iteramos los superpoderes
    #for superpoder in args:
    #    print(f'\tSuper poder : {superpoder}')

# Llamar a la función
superheroes_superpoderes('Peter Parker', 'Instinto aráncnido', edad=17, empresa='Marvel')
superheroes_superpoderes('Ironman', 'armadura', 'playboy', dinero='mucho')

# Es opcional enviar argumentos y variables
superheroes_superpoderes('Mi vecino', personalidad='buena onda')