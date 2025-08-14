class Animal:
    def hacer_sonido(self):
        print('Hago un pitido')

class Perro(Animal):
    pass #se define la función sin contenido
    #def hacer_sonido(self):
    #    print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')


print('*** Ejemplo polimorfismo***')
print('*** Clase padre animal***')
animal1 = Animal()
animal1.hacer_sonido()

print('*** Clase perro hijo***')
perro1 = Perro()
perro1.hacer_sonido()

print('*** Clase gato hijo***')
gato1 = Gato()
gato1.hacer_sonido()