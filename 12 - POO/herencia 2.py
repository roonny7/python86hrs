class Animal:
    def comer(self):
        print('Como varias veces al día')
    def dormir(self):
        print('Duermo muchas horas')


class Perro(Animal):
    def hacer_sonido(self):
        print('Puedo ladrar')

    # Sobreescritura del método dormir
    def dormir(self):
        print('Duermo 15 horas al día')

#Programa Principal
print('*** Ejemplo de herencia en Python***')
print('*** Clase padre, soy un animal')
animal1 = Animal()
animal1.comer()
animal1.dormir()
print('\nClase hija, soy un perro')
perro1 = Perro()
perro1.dormir()
perro1.comer()
perro1.hacer_sonido()