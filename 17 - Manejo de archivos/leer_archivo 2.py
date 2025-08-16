print('*** Leer archivo, 2 ***')

archivo = open('prueba.txt', 'r', encoding='utf-8')

for linea in archivo:
    print(linea)

#Leer todas las lineas en un una sola, devuelve como lista
archivo = open('prueba.txt', 'r', encoding='utf-8')
print(archivo.readlines())

#Leer todas las lineas en un una sola, devuelve como lista
archivo = open('prueba.txt', 'r', encoding='utf-8')
print(f'Una sola línea : {archivo.readlines()[0]}')

# Abrimos un nuevo archivo
# a  = anexar infomración
archivo = open('prueba.txt', 'r', encoding='utf-8')
# en modo 'a', agrega líneas al final, si se usa 'w',
# borra to_do lo que tiene
archivo2 = open('copia.txt', 'a', encoding='utf-8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()