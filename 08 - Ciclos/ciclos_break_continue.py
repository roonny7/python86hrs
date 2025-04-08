print('*** break y continue')

#ejemplo con break
for numero in range (1,10):
    if numero % 2 == 0 :
        print(numero)
        break #salir del ciclo inmediatamente


#ejemplo con continue
for numero in range (1,10):
    if numero % 2 == 1 :
        continue

    print(numero)  #números pares
