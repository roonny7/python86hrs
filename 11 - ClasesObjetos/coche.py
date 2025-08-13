# Definimos la clase coche
class Coche:

    def __init__(self, marca, modelo, color):
        self.marca = marca # Atributo público
        self._modelo = modelo #Atributo  protegido
        self.__color = color #atributo privado

    def conducir(self):
        print(f'''
        Conduciendo el coche)
        Marca : {self.marca}
        Modelo : {self._modelo}
        Color : {self.__color} ''')

coche1 = Coche('Toyota', 'Celica', 'Negro')
coche1.conducir()

#No deberíamos acceder a los atributos que no sean públicos
coche1.marca = 'Toyota 2'
coche1._modelo = 'Celica 2' #esto no es una buena práctica
coche1.__color = " negro 2" #Ignoró la modificación
coche1._Coche__color = "negro 3" #esto es una mala práctica
coche1.conducir()