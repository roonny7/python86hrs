class Persona:
    #atributo clase
    contador_personas = 0

    def __init__(self, nombre, apellido):
        #incrementamos el valor del atributo de clase
        Persona.contador_personas += 1
        self.id = Persona.contador_personas
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'Persona : {self.id}.- {self.nombre}, {self.apellido} ')

    @staticmethod
    def get_contador_persona_estatico():
        print('Método estático')
        return Persona.contador_personas

    @classmethod
    def get_contador_personas_clase(cls):
        print('Método class')
        return cls.contador_personas


if __name__ == '__main__':
    print(f'*** Ejemplo contador de objetos de tipo Persona ***')
    persona1 = Persona('Gerardo', 'Perez')
    persona1.mostrar_persona()

    persona2 = Persona('Juan', 'Sanchez')
    persona2.mostrar_persona()

    # Imprimir el valor del contador de objetos personas
    print(f'Contador objetos persona : {Persona.contador_personas}')
    print(f'Contador objetos persona (objeto) : {persona1.contador_personas}')
    print(f'Contador objetos persona (static): {Persona.get_contador_persona_estatico()}')
    print(f'Contador objetos persona (class): {Persona.get_contador_personas_clase()}')
