print ('*** Calcula total de impuestos ***')

def calcular_pago(pago_sin_impuesto, impuesto):
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total


# Llamar a la función
pago_sin_impuesto = float(input('Cuanto es el pago? :'))
impuesto = float(input('Cuanto es el impuesto? :'))
total = calcular_pago(pago_sin_impuesto, impuesto)
print(f'El impuesto de {impuesto} de {pago_sin_impuesto} es : {total}')
