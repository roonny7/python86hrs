print('*** Cálculo área y perímetro de un rectángulo ***')

# reisar si una variale se encuentra dentro de rango 1 y 10
base = float(input('Proporciona la base : '))
altura = float(input('Proporciona la altura : '))

#Calculamos área
area = base * altura
print(f'El área es : {area}')

#Calculamos parímetro
perimetro = 2 * (base + altura)
print(f'El perimetro es : {perimetro}')