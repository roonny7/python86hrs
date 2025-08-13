class Persona:

    atributo_clase = 0

    def __init__(self, atributo_instancia):
        self.atributo_instancia = atributo_instancia

# Programa Principal
print(f'*** Atributos de clase ***')
print(f'Atributo de clase : {Persona.atributo_clase}')

# Modificamos el atributo de clase
Persona.atributo_clase = 7
print(f'Atributo de clase : {Persona.atributo_clase}')

# Creamos el obbjeto personal1
persona1 = Persona(70)
print(f'Atributo de clase desde el objeto persona1 { persona1.atributo_clase}')
print(f'Atributo de instancia desde el objeto persona1 { persona1.atributo_instancia}')

# Creamos el obbjeto personal2
persona2 = Persona(700)
print(f'Atributo de clase desde el objeto persona1 { persona2.atributo_clase}')
print(f'Atributo de instancia desde el objeto persona1 { persona2.atributo_instancia}')
