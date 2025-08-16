print('*** Manejo de archivos ***')

try:
    archivo = open ('prueba.txt', 'w', encoding='utf-8')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adiós mugrosos\n')
except Exception as error:
    print(error)
finally:
    archivo.close()
    print('El archivo ya está cerrado')
