#Definición de una clase
class Persona:

    # Constructor
    def __init__(self, nombre, apellido):
        #creamos atributos de la clase
        self.nombre = nombre
        self.apellido = apellido

    def mostrar_persona(self):
        print(f'''Persona : 
        Nombre : {self.nombre} 
        Apellido : {self.apellido}
        ''')

# Creación de objetos
if __name__ == '__main__':
    # Creación de un primer objeto
    persona1 = Persona('Layla', 'Acosta')  #crea un objeto vacío en memoria
    persona1.mostrar_persona()
    print(f'Dir mem persona 1 {id(persona1)}' )
    print(f'Dir mem persona 1 {hex(id(persona1))}')

    # Creamos un segundo objeto
    persona2 = Persona('Ian', 'Sanchez0')
    persona2.mostrar_persona() #si se pone así, sin inicializar marca error
    print(f'Dir mem persona 2 {id(persona2)}' )
    print(f'Dir mem persona 2 {hex(id(persona2))}')