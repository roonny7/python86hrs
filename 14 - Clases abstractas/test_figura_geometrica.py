from cuadrado import Cuadrado
from rectangulo import Rectangulo
from figura_geometrica import FiguraGeometrica

# no se puede instanciar una clase abstracta
#figura = FiguraGeometrica()


print('Creación objeto cuadrado'.center(50, '-'))
cuadrado1 = Cuadrado(5,'rojo')
#print((cuadrado1.ancho))
#print(cuadrado1.alto)
#print(cuadrado1.color)

print(f'El cálculo del area es : {cuadrado1.calcular_area()}')
print(cuadrado1)
print()
print('Creación objeto rectángulo'.center(50, '-'))
rectangulo1 = Rectangulo(ancho=4, alto=5, color='azul')
print(f'El cálculo del área es : {rectangulo1.calcular_area()}')
#MRO Method Resolution Order
print(Cuadrado.mro())