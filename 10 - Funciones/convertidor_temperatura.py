print ('*** Calcula total de impuestos ***')

def celsius_a_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def fahrenheit_a_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


# Llamar a la función
celsius = float(input('Temperatura en celsius? :'))
resultadoc=celsius_a_fahrenheit(celsius)
fahrenheit = float(input('Temperatura en fahrenheit? :'))
resultadof=fahrenheit_a_celsius(fahrenheit)


print(f'La temperatura en {celsius}C  a fahrenheit es : {resultadoc:.2f}F')
print(f'La temperatura en {fahrenheit}C  a celsius es : {resultadof:.2f}F')
