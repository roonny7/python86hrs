class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    #Sobre escribir el metodo __str__
    def __str__(self):
        return f'''Persona : 
        nombre : {self.nombre}
        Apelldo = {self.apellido}
        Dir. memoria : {super.__str__(self)}'''


# Código principal
persona1 = Persona('Ana', 'Babas')
print(persona1)  # El método __str__ se llama automáticamente desde print
#print(persona1.__str__())  #esto es opcional
