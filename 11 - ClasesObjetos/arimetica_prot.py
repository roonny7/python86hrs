#Definición de una clase
from logging import raiseExceptions


class Aritmetica:

    # Constructor
    def __init__(self, operando1, operando2):
        #creamos atributos de la clase
        self._operando1 = operando1
        self._operando2 = operando2

    def sumar(self):
        print(f'La suma es : {self._operando1 + self._operando2} ')

    def restar(self):
        resta=self._operando1 - self._operando2
        print(f'La resta es : {resta} ')

    def multiplicar(self):
        print(f'La multiplicación es : {self._operando1 * self._operando2} ')

    def dividir(self):
        print(f'La división es : {self._operando1 / self._operando2} ')

    @property
    def operando1(self):
        return self._operando1

    @operando1.setter
    def operando1(self, operando1):
        self._operando1 = operando1

    @property
    def operando2(self):
        return self._operando2

    @operando2.setter
    def operando2(self, operando2):
        self._operando2 = operando2

# Creación de objetos
if __name__ == '__main__':
    # Creación de un primer objeto
    aritmerica = Aritmetica(40, 30)  #crea un objeto vacío en memoria
    print('Primer objeto')
    print(f'Valor operando1 del objeto aritmetica 1: {aritmerica.operando1}')
    print(f'Valor operando2 del objeto aritmetica 1: {aritmerica.operando2}')
    aritmerica.sumar()
    aritmerica.restar()
    aritmerica.operando1 = 200
    aritmerica.operando2 = 70
    print(f'Valor operando1 del objeto aritmetica 1: {aritmerica.operando1}')
    print(f'Valor operando2 del objeto aritmetica 1: {aritmerica.operando2}')
    aritmerica.dividir()
    aritmerica.multiplicar()
    print()

    # Creación de un Segundo objeto
    aritmerica2 = Aritmetica(50, 50)  #crea un objeto vacío en memoria
    print('Segundo objeto')
    print(f'Valor operando1 del objeto aritmetica 2: {aritmerica2.operando1}')
    print(f'Valor operando2 del objeto aritmetica 2: {aritmerica2.operando2}')
    aritmerica2.sumar()
    aritmerica2.restar()
    aritmerica2.dividir()
    aritmerica2.multiplicar()