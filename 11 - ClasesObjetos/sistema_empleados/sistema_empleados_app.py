from empresa import Empresa
from empleado import Empleado
print(f'*** Sistema de empleados ***')
# Crear una instancia de una empresa
empresa1 = Empresa('Roonny Corporaation')

#Contratar algunos empleados
empresa1.contratar_empleados('Jorge', 'Ventas')
empresa1.contratar_empleados('María', 'Compras')
empresa1.contratar_empleados('Pedro', 'Ventas')
empresa1.contratar_empleados('Ana', 'RH')

# Obtener el total de objetos de tipo empleado
print(f'Total de empleados {Empleado.obtener_total_empleados()}')

# Obtner el número de empleados en el depto de ventas
print(f'Empleado del depto de ventas : '
    f' {empresa1.obtener_numero_empleados_departamento('Ventas')} ')

# mostrar todos los empleados
empresa1.obtener_total_empleados()