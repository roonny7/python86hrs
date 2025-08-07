print('*** Función par ***')

# FUnción para saber si es par
def es_par(numero):
    if numero % 2 == 0 :
        return True
    else:
        return False

# Llamamos a la función
if __name__ == '__main__':
    numero = int(input('Teclea un número : '))
    print(f'Número par : { es_par(numero) } ')