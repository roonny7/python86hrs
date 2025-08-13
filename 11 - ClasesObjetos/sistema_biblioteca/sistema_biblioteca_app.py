from biblioteca import Biblioteca
from libro import Libro
biblioteca = Biblioteca('Oscura')
print(f'*** Bienvenidos a la biblioteca {biblioteca.nombre}')

#Definicion de libros
libro1 = Libro('Necronomicon', 'Sin autor', 'Terror2')
libro2 = Libro('Libro de los condenados', 'Sin autor', 'Terror')
libro3 = Libro('Libro de Ra', 'Sin autor', 'Terror')

# Agregar los libros
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)

# Buscar libros por autor
print()
autor = 'Sin autor'
biblioteca.buscar_libros_por_autor(autor)
print()
# Buscar libros por genero
print()
genero = 'Terror'
biblioteca.buscar_libros_por_genero(genero)
print()
print('*Mostrar todos los libros*')
biblioteca.mostrar_todos_los_libros()