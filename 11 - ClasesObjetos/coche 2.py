# Definimos la clase coche
class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca # Atributo público
        self._modelo = modelo #Atributo  protegido
        self._color = color #atributo privado

    def conducir(self):
        print(f'''
        Conduciendo el coche)
        Marca : {self._marca}
        Modelo : {self._modelo}
        Color : {self._color} ''')

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca= marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return self._color

    def set_color(self, color):
        self.color = color

coche1 = Coche('Toyota', 'Celica', 'Negro')
coche1.conducir()

#No deberíamos acceder a los atributos que no sean públicos
coche1.set_marca('Toyota 2')
coche1.set_modelo('Celica 2')
coche1.set_color("negro 2")
coche1.conducir()