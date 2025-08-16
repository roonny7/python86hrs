from dominio.peliculas import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as pelis


opcion = None


while opcion != 4:
    try:
        print('Opciones: ')
        print('1. Agregar película')
        print('2. Listar película')
        print('3. Eliminar catálogo de películas')
        print('4. Salir')
        opcion = int(input('Escribe tu opción (1-4) : '))

        if opcion == 1:
            nombre_pelicula = input('Proporciona el nombre de la película')
            pelicula = Pelicula(nombre_pelicula)
            pelis.agregar_peliculas(pelicula)

        elif opcion == 2:
            pelis.listar_peliculas()

        elif opcion == 3:
            pelis.eliminar_peliculas()

    except Exception as e:
        print(f'Ocurrión un error {e}')
        opcion = None
else:
     print('Salimos del programa')