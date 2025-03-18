print('*** Sistema tienda en línea con descuentos ***')

#Condiciones
MONTO_COMPRA_DESC=1000

monto_compra = float(input('¿Cuál es el monto de la copra?'))
es_miembro = input('¿Eres miembro de la tienda? (Si/No)')

descuento = 0

#verificar cada caso, con los datos proporcionados
if monto_compra >= MONTO_COMPRA_DESC and es_miembro.strip().lower() == 'si':
    descuento = 0.1 #Descuento del 10%
elif es_miembro.strip().lower() == 'si':
    descuento = 0.05 #Descuento del 5%
elif monto_compra >= MONTO_COMPRA_DESC:
    descuento = 0.03  # Descuento del 3%
else:
    descuento = 0

#Hacemos los cálculos
if descuento != 0:
    monto_descuento = monto_compra * descuento
    monto_final = monto_compra - monto_descuento
    print(f'Has obtenido un descuento del {descuento * 100:.0f}%')
    print(f'Monto de la compra : {monto_compra:.2f}')
    print(f'Monto del descuento : {monto_descuento:.2f}')
    print(f'Monto final de la compra : {monto_final:.2f}')
else:
    print(f'\nNo obtuviste ningún tipo de descuento')
    print(f'Te invitamos a hacerte miembro de la tienda')
    print(f'Monto de la compra : {monto_compra:.2f}')
