print('*** Apicación de salud y fitness ***')

#Constantes
META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04 #kilocalorias

#Pedimos los valores al usuario
nombre_usuario = input('Cuál es tu nombre? ')
pasos_diarios = int(input('Cuantos pasos has caminado hoy? '))

#verificar meta
meta_alcanzada = pasos_diarios >= META_PASOS_DIARIOS
meta_alcanzada_txt =  'Si' if meta_alcanzada else 'No'

#Calorías quemadas
calorias_quemadas = pasos_diarios * CALORIAS_POR_PASO

#mostramos la información
print(f'\n Usuario : { nombre_usuario }')
print(f'Pasos dados hoy : {pasos_diarios}')
print(f'Calorías quemadas : { calorias_quemadas}')
print(f'Meta alcanzada? {meta_alcanzada_txt}')
