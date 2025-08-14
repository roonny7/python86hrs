class Animal:
    def hacer_sonido(self):
        print('Hago un pitido')

class Perro(Animal):
    #pass #se define la función sin contenido
    def hacer_sonido(self):
        print('Puedo ladrar')

class Gato(Animal):
    def hacer_sonido(self):
        print('Puedo maullar')

# Función polimórfica
def hacer_sonido_animal(animal):
    animal.hacer_sonido()


print('*** Ejemplo polimorfismo***')
print('*** Clase padre animal***')
animal1 = Animal()
hacer_sonido_animal(animal1)

print('*** Clase perro hijo***')
perro1 = Perro()
hacer_sonido_animal(perro1)

print('*** Clase gato hijo***')
gato1 = Gato()
hacer_sonido_animal(gato1)