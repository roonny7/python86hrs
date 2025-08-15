from color import Color
from figura_geometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, ancho, alto, color):
        #super().__init__()
        FiguraGeometrica.__init__(self, ancho, alto)
        Color.__init__(self, color)

    def calcular_area(self):
        return self.ancho * self.alto

    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'