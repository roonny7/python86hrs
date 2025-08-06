print(('*** Alcance de variables ***'))

# Variable global
contador_global = 0

def incrementar_contador():
    # Declaramos una variable local
    contador_local = 0

    # Usar la variable global
    global contador_global

    # Incrementamos la variable global
    contador_global += 1

    # Incrementamos la variable local
    contador_local += 1

    # Imprimimos ambos contadores
    print(f'Contador local : {contador_local}')
    print(f'Contador global : {contador_global}\n')


# Llamamos varias veces la funcion

contador = 1
while contador <= 5:
    incrementar_contador()
    contador += 1 #contador = contador + 1


# Terminado el programa
print(f'Contador global : {contador_global}')