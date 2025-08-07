print ('*** potencia de un número usando funciones recursivas ***')

def potencia(base, exponente):
    #caso base
    if exponente == 0:
            return 1
    else:  #caso recursivo
        return base * potencia(base, exponente - 1)


# Llamamos a la función
base = 4
exponente = 5

print(f'El exponente de {base} elevado a la {exponente} es : {potencia(base, exponente)}')
