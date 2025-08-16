class Persona:
    def __init__(self,nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __add__(self, otro):
        return self.nombre + ' ' + otro.nombre

    def __sub__(self, otro):
        return self.edad - otro.edad
persona1 = Persona("Juan", 50)
persona2 = Persona("Carlos", 90)

print(f'{persona1 + persona2}')
print(f'{persona1 - persona2}')
