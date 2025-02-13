# Generador de email

nombre = "Jorge Nitales Grande"
empresa = "Opergob solutions"
dominio = 'froy.gob.mx'

#Resultado final debe ser
#jorge.nitales.grande@opergobsolutions.froy.gob.mx

nombre=nombre.lower()
nombre=nombre.replace(' ','.')

empresa=empresa.lower()
empresa=empresa.replace(' ','')
print(empresa)

correo=nombre+'@'+empresa+'.'+dominio
print(correo)


