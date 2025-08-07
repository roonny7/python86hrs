print ('*** Imprimir del 1 al 5 , pero de forma recursiva')

# definir la función recursiva
def funcion_recursiva(numero):
    #caso base
    if numero == 1 :
        print(numero, end = ' * ')

    else: # caso recursivo
        print(numero, end = ' - ')
        funcion_recursiva(numero - 1)



# Llamar a la función
funcion_recursiva(100)