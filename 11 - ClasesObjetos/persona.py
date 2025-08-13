#Definición de una clase
class Persona:

    def inicialiazar_persona(self, nombre, apellido):
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
    persona1 = Persona()  #crea un objeto vacío en memoria
    persona1.inicialiazar_persona('Layla', 'Acosta')
    persona1.mostrar_persona()

    # Creamos un segundo objeto
    persona2 = Persona() # Crea un objeto vacío en memoria
    persona2.inicialiazar_persona('Ian', 'Sanchez0')
    persona2.mostrar_persona() #si se pone así, sin inicializar marca error