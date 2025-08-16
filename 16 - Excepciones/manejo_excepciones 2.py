resultado = None
a = "10"
b = 0

try :
    resultado = a/b
except ZeroDivisionError as e:
    print(f'División por cero : {e}, {type(e)}')
except TypeError as te:
    print(f'Ocurrió un error de tipo de datos : {te}, {type(te)}')
except Exception as eex:
    print(f'Ocurrió un error general : {eex} , {type(eex)}')

print(f'Resultado: {resultado}')
print('Continuamos...')