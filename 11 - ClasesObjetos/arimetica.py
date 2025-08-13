#Definición de una clase
from logging import raiseExceptions


class Aritmetica:

    # Constructor
    def __init__(self, operando1, operando2):
        #creamos atributos de la clase
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        print(f'La suma es : {self.operando1 + self.operando2} ')

    def restar(self):
        resta=self.operando1 - self.operando2
        print(f'La resta es : {resta} ')

    def multiplicar(self):
        print(f'La multiplicación es : {self.operando1 * self.operando2} ')

    def dividir(self):
        print(f'La división es : {self.operando1 / self.operando2} ')

# Creación de objetos
if __name__ == '__main__':
    # Creación de un primer objeto
    aritmerica = Aritmetica(40, 30)  #crea un objeto vacío en memoria
    aritmerica.sumar()
    aritmerica.restar()
    aritmerica.dividir()
    aritmerica.multiplicar()
    print()
    # Creación de un Segundo objeto
    aritmerica2 = Aritmetica(50, 50)  #crea un objeto vacío en memoria
    aritmerica2.sumar()
    aritmerica2.restar()
    aritmerica2.dividir()
    aritmerica2.multiplicar()