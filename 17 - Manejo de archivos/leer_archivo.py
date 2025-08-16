print('*** Leer archivo ***')

archivo = open('prueba.txt', 'r', encoding='utf-8')
print(archivo.read())


# Leer sólo algunos caracteres, como llegó al final, hay que volverlo a abrir
archivo = open('prueba.txt', 'r', encoding='utf-8')
print(archivo.read(5))
print(archivo.read(50))


# Leer líneas completas
archivo = open('prueba.txt', 'r', encoding='utf-8')
print(f'Línea completa : {archivo.readline()}')

