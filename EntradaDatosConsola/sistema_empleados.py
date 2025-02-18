print('*** Sistema de empleados ***')
nombre_empleado = input('Nombre del empleado :')
edad_empleado = int(input('Edad del empleado : '))
salario_empleado = float(input('Salario del empleado : '))
es_jefe_departamento = input(' Es jefe departamento (Si/No)?')

# Vamos a convertir a ipo bool la variable es_jefe_departamento
es_jefe_departamento = es_jefe_departamento.lower() == 'si'

#Imprimir los valores del empleado
print('\nDatos del empleado ')
print(f'Nombre : {nombre_empleado}')
print((f'Edad del empleado : {edad_empleado}'))
print(f'fSalario del empleado : {salario_empleado:.2f}')
print(f'es Jefe de departamento : {es_jefe_departamento}')