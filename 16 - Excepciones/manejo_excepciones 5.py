from numeros_identicos_excepcion import NumeroIdenticosException
resultado = None

try :
    a = int(input('Valor de a :'))
    b = int(input('Valor de b :'))

    if a == b :
        raise NumeroIdenticosException('Números idénticos')
    resultado = a/b

except ZeroDivisionError as e:
    print(f'División por cero : {e}, {type(e)}')
except TypeError as te:
    print(f'Ocurrió un error de tipo de datos : {te}, {type(te)}')
except ValueError as ve:
    print(f'Ocurrió un error de valores de datos : {ve}, {type(ve)}')
except Exception as eex:
    print(f'Ocurrió un error general : {eex} , {type(eex)}')
else:
    print('No hay ninguna excepción')
finally: #Haya o no error, esta onda se ejecuta
    print('Ya me ejecuté =), soy finally')

print(f'Resultado: {resultado}')
print('Continuamos...')