from teclado import Teclado
from raton import Raton
from monitor import Monitor
from computadora import Computadora
from orden import Orden
print('**** Mundo PC ****')
#COmputadora1
teclado1 = Teclado('HP', 'USB')
raton1 = Raton('HP', 'BT')
monitor1 = Monitor('DELL', '27')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)

teclado2 = Teclado('Gamer', 'USB')
raton2 = Raton('MC', 'USB')
monitor2 = Monitor('Gamer', '32')
computadora2 = Computadora('DELL', monitor2, teclado2, raton2)

# Crear lista de computadoras
computadoras1 = [computadora1, computadora2]
orden1 = Orden(computadoras1)
#print(orden1)

teclado3 = Teclado('C', 'PS2')
raton3 = Raton('CC', 'BT2')
monitor3 = Monitor('DELL', '34')
computadora3 = Computadora('HP', monitor3, teclado3, raton3)
orden1.agregar_computadora(computadora3)
print(orden1)