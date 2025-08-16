from manejo_archivos import ManejoArchivos
with open('prueba.txt', 'r', encoding='utf-8') as archivo:
    print(archivo.read())

with ManejoArchivos('prueba.txt') as archivo:
    print(archivo.read())