print('*** Sistema de préstamo de libros) ***')
DISTANCIA_PERMITIDA_KM = 3

tiene_credencial = input('Tienes credencial de estudiante (Si, No)?')
distancia_biblioteca_km = int(input('A cuántos kms vives de la biblioteca ? '))

es_elegible_prestamo = (tiene_credencial.strip().lower() == 'si' or
                        distancia_biblioteca_km <= DISTANCIA_PERMITIDA_KM)

print(f'Eres elegible para préstamo? {es_elegible_prestamo}')