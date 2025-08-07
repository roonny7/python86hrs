print('*** Argumentos variables ***')
def superheroes_superpoderes(superheroe, nombre, *args):
    print(f'Superhéroe : {superheroe} - {nombre} - {args}')
    # Iteramos los superpoderes
    for superpoder in args:
        print(f'\tSuper poder : {superpoder}')

# Llamar a la función
superheroes_superpoderes('Spiderman', 'Peter Parker', 'Instinto aráncnido', 'telaraña')
superheroes_superpoderes('Ironman', 'Tony Stark', 'dinero', 'dinero', 'dinero')

# Es opcional enviar argumentos y variables
superheroes_superpoderes('Juan Perez', 'Mi vecino')