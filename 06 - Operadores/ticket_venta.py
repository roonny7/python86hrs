print('*** Generación ticket de venta***')

precio_leche = float(input('Precio leche : '))
precio_pan = float(input('Precio pan : '))
precio_lechuga = float(input('Precio lechuga : '))
precio_platanos = float(input('Precio plátanos : '))

descuento_porcentaje = int(input('Aplicar algún descuento en porcentaje? '))

#Calculo del subtotal (sin impuestos)
subtotal = precio_pan + precio_platanos + precio_leche + precio_lechuga
descuento = subtotal * (descuento_porcentaje/100)

#Subtotal con descuneto
subtotal_con_descuento = subtotal - descuento

#cálculo de impuestos (16%)
impuesto = subtotal_con_descuento * 0.16

#Cálculo total de la compra con impuestos
costo_total_compra = subtotal_con_descuento + impuesto

print(f'''
Subtotal : ${subtotal:.2f}
Descuento : ${descuento} ({descuento_porcentaje:}%)
Impuesto : ${impuesto:.2f}
Costo total de la compra : ${costo_total_compra:.2f}
''')